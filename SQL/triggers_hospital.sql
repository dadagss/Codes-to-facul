use hospital;

DELIMITER //

CREATE PROCEDURE InserirConsulta (
    IN medico_crm VARCHAR(10),
    IN paciente_cpf VARCHAR(11),
    IN desc_consulta VARCHAR(255),
    IN data_consulta DATETIME
)
BEGIN
    INSERT INTO hospital.Consultas (Medicos_CRM, Pacientes_CPF, Descconsulta, DataConsulta, status)
    VALUES (medico_crm, paciente_cpf, desc_consulta, data_consulta, 1);
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER AtualizarStatusConsulta AFTER INSERT ON hospital.tratamentos
FOR EACH ROW
BEGIN
    UPDATE hospital.Consultas
    SET status = 2
    WHERE ID = NEW.ID_consulta;
END //

DELIMITER ;