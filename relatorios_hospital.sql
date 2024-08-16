use hospital;

-- Objetivo do relatório: Listar todas as consultas agendadas com detalhes sobre o médico, paciente e status da consulta.
SELECT c.DataConsulta, m.Nome AS Medico, p.nome AS Paciente, c.Descconsulta, 
       CASE 
           WHEN c.status = 1 THEN 'Agendada'
           WHEN c.status = 2 THEN 'Cancelada'
           ELSE 'Concluída'
       END AS Status
FROM hospital.Consultas c
INNER JOIN hospital.Medicos m ON c.Medicos_CRM = m.CRM
INNER JOIN hospital.Pacientes p ON c.Pacientes_CPF = p.CPF;


-- Objetivo do relatório: Listar todos os tratamentos realizados com detalhes sobre a consulta associada, paciente e custo do tratamento.
SELECT t.ID_consulta, t.Desctratamento, t.Custo, p.nome AS Paciente, c.DataConsulta AS Data_Consulta
FROM hospital.tratamentos t
INNER JOIN hospital.Consultas c ON t.ID_consulta = c.ID
INNER JOIN hospital.Pacientes p ON c.Pacientes_CPF = p.CPF;


-- Objetivo do relatório: Listar todas as internações com detalhes sobre o paciente, motivo da internação e período de internação.
SELECT i.Pacientes_CPF, p.nome AS Paciente, i.datainternacao, i.datasaida, i.descinternacao
FROM hospital.internacoes i
INNER JOIN hospital.Pacientes p ON i.Pacientes_CPF = p.CPF;

-- Objetivo do relatório: Listar todas as consultas agendadas e os tratamentos associados a cada consulta, com detalhes sobre o médico, paciente e tratamento.
SELECT c.DataConsulta, m.Nome AS Medico, p.nome AS Paciente, c.Descconsulta, t.Desctratamento, t.Custo
FROM hospital.Consultas c
INNER JOIN hospital.Medicos m ON c.Medicos_CRM = m.CRM
INNER JOIN hospital.Pacientes p ON c.Pacientes_CPF = p.CPF
LEFT JOIN hospital.tratamentos t ON c.ID = t.ID_consulta;
