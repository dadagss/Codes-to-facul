-- Inserts para tabela Pacientes
INSERT INTO hospital.Pacientes (CPF, nome, Telefone, Endereço, Historico) 
VALUES ('12345678901', 'João Silva', '555-1234', 'Rua A, 123', 'Sem histórico'),
       ('23456789012', 'Maria Santos', '555-5678', 'Rua B, 456', 'Historico de cirurgia'),
       ('34567890123', 'Pedro Oliveira', '555-9012', 'Rua C, 789', 'Historico de alergia');

-- Inserts para tabela Medicos
INSERT INTO hospital.Medicos (CRM, Nome, especialidade, Telefone)
VALUES ('CRM123456', 'Dra. Mariana', 'Cardiologista', '555-1111'),
       ('CRM234567', 'Dr. Daniel', 'Dermatologista', '555-2222'),
       ('CRM345678', 'Dr. Maria', 'Pediatra', '555-3333');

-- Inserts para tabela Consultas
INSERT INTO hospital.Consultas (Medicos_CRM, Pacientes_CPF, Descconsulta, DataConsulta, status)
VALUES ('CRM123456', '12345678901', 'Consulta de rotina', '2024-06-04 10:00:00', 1),
       ('CRM234567', '23456789012', 'Exame dermatológico', '2024-06-05 14:30:00', 1),
       ('CRM345678', '34567890123', 'Consulta pediátrica', '2024-06-06 11:15:00', 1);

-- Inserts para tabela tratamentos
INSERT INTO hospital.tratamentos (ID_consulta, Desctratamento, Custo, Duração)
VALUES (1, 'Medicação prescrita', 50.00, '2024-06-04 10:30:00'),
       (2, 'Aplicação de pomada', 30.00, '2024-06-05 15:00:00'),
       (3, 'Vacinação', 80.00, '2024-06-06 11:45:00');

-- Inserts para tabela internacoes
INSERT INTO hospital.internacoe (Pacientes_CPF, datainternacao, datasaida, descinternacao, quarto)
VALUES ('12345678901', '2024-06-07 08:00:00', '2024-06-10 12:00:00', 'Cirurgia de apendicite', '101'),
       ('23456789012', '2024-06-08 10:00:00', '2024-06-12 14:00:00', 'Tratamento de acne', '202'),
       ('34567890123', '2024-06-09 09:00:00', '2024-06-11 11:00:00', 'Observação por febre', '303');