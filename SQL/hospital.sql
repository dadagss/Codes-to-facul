- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hospital
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hospital
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS hospital DEFAULT CHARACTER SET utf8 ;
USE hospital ;

-- -----------------------------------------------------
-- Table hospital.Pacientes
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS hospital.Pacientes (
  CPF CHAR(11) NOT NULL,
  nome VARCHAR(100) NOT NULL,
  Telefone VARCHAR(15) NOT NULL,
  Endereço VARCHAR(200) NOT NULL,
  Historico VARCHAR(244) NOT NULL,
  UNIQUE INDEX Pacientescol1_UNIQUE (Telefone ASC) VISIBLE,
  PRIMARY KEY (CPF),
  UNIQUE INDEX CPF_UNIQUE (CPF ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table hospital.Medicos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS hospital.Medicos (
  CRM CHAR(10) NOT NULL,
  Nome VARCHAR(144) NOT NULL,
  especialidade VARCHAR(50) NOT NULL,
  Telefone VARCHAR(15) NOT NULL,
  UNIQUE INDEX crm_UNIQUE (CRM ASC) VISIBLE,
  UNIQUE INDEX Telefone_UNIQUE (Telefone ASC) VISIBLE,
  PRIMARY KEY (CRM))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table hospital.Consultas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS hospital.Consultas (
  ID_consulta INT NOT NULL AUTO_INCREMENT,
  Medicos_CRM CHAR(10) NOT NULL,
  Pacientes_CPF CHAR(11) NOT NULL,
  Descconsulta VARCHAR(100) NOT NULL,
  DataConsulta DATETIME NOT NULL,
  status TINYINT NOT NULL DEFAULT '1',
  PRIMARY KEY (ID_consulta),
  UNIQUE INDEX ID_consulta_UNIQUE (ID_consulta ASC) VISIBLE,
  INDEX fk_Consultas_Medicos1_idx (Medicos_CRM ASC) VISIBLE,
  INDEX fk_Consultas_Pacientes1_idx (Pacientes_CPF ASC) VISIBLE,
  CONSTRAINT fk_Consultas_Medicos1
    FOREIGN KEY (Medicos_CRM)
    REFERENCES hospital.Medicos (CRM)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_Consultas_Pacientes1
    FOREIGN KEY (Pacientes_CPF)
    REFERENCES hospital.Pacientes (CPF)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table hospital.tratamentos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS hospital.tratamentos (
  ID_consulta INT NOT NULL,
  Desctratamento VARCHAR(244) NOT NULL,
  Custo DECIMAL NOT NULL,
  Duração DATETIME NOT NULL,
  INDEX fk_tratamentos_Consultas1_idx (ID_consulta ASC) VISIBLE,
  CONSTRAINT fk_tratamentos_Consultas1
    FOREIGN KEY (ID_consulta)
    REFERENCES hospital.Consultas (ID_consulta)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table hospital.internacoe
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS hospital.internacoe (
  idinternação INT NOT NULL AUTO_INCREMENT,
  Pacientes_CPF CHAR(11) NOT NULL,
  datainternacao DATETIME NOT NULL,
  datasaida DATETIME NOT NULL,
  descinternacao VARCHAR(100) NOT NULL,
  quarto VARCHAR(20) NOT NULL,
  PRIMARY KEY (idinternação),
  INDEX fk_internações_Pacientes1_idx (Pacientes_CPF ASC) VISIBLE,
  CONSTRAINT fk_internações_Pacientes1
    FOREIGN KEY (Pacientes_CPF)
    REFERENCES hospital.Pacientes (CPF)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;