-- CRIAÇÃO DO BANCO DE DADOS --
CREATE TABLE SalaDeAula (
    Predio VARCHAR(50),
    NumeroSala VARCHAR(10),
    Capacidade INT,
    PRIMARY KEY (Predio, NumeroSala)
);

CREATE TABLE Departamento (
    NomeDept VARCHAR(100) PRIMARY KEY,
    Predio VARCHAR(50),
    Orcamento DECIMAL(15, 2)
);

CREATE TABLE Curso (
    IdCurso INT PRIMARY KEY,
    Titulo VARCHAR(200),
    NomeDept VARCHAR(100),
    Creditos INT,
    FOREIGN KEY (NomeDept) REFERENCES Departamento(NomeDept)
);

CREATE TABLE Instrutor (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    NomeDept VARCHAR(100),
    Salario DECIMAL(15, 2),
    FOREIGN KEY (NomeDept) REFERENCES Departamento(NomeDept)
);

CREATE TABLE Periodo (
    IdPeriodo INT PRIMARY KEY,
    Dia VARCHAR(20),
    HoraInicial TIME,
    HoraFinal TIME
);

CREATE TABLE Secao (
    IdCurso INT,
    IdSec INT,
    Semestre VARCHAR(10),
    Ano INT,
    Predio VARCHAR(50),
    NumeroSala VARCHAR(10),
    IdPeriodo INT,
    PRIMARY KEY (IdCurso, IdSec, Semestre, Ano),
    FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
    FOREIGN KEY (Predio, NumeroSala) REFERENCES SalaDeAula(Predio, NumeroSala),
    FOREIGN KEY (IdPeriodo) REFERENCES Periodo(IdPeriodo)
);

CREATE TABLE Ministra (
    ID INT,
    IdCurso INT,
    IdSec INT,
    Semestre VARCHAR(10),
    Ano INT,
    PRIMARY KEY (ID, IdCurso, IdSec, Semestre, Ano),
    FOREIGN KEY (ID) REFERENCES Instrutor(ID),
    FOREIGN KEY (IdCurso, IdSec, Semestre, Ano) REFERENCES Secao(IdCurso, IdSec, Semestre, Ano)
);

CREATE TABLE Aluno (
    ID INT PRIMARY KEY,
    Nome VARCHAR(100),
    NomeDept VARCHAR(100),
    TotCred INT,
    FOREIGN KEY (NomeDept) REFERENCES Departamento(NomeDept)
);

CREATE TABLE Realiza (
    ID INT,
    IdCurso INT,
    IdSec INT,
    Semestre VARCHAR(10),
    Ano INT,
    Nota DECIMAL(4, 2),
    PRIMARY KEY (ID, IdCurso, IdSec, Semestre, Ano),
    FOREIGN KEY (ID) REFERENCES Aluno(ID),
    FOREIGN KEY (IdCurso, IdSec, Semestre, Ano) REFERENCES Secao(IdCurso, IdSec, Semestre, Ano)
);

CREATE TABLE Mentor (
    IdEst INT,
    IdInst INT,
    PRIMARY KEY (IdEst, IdInst),
    FOREIGN KEY (IdEst) REFERENCES Aluno(ID),
    FOREIGN KEY (IdInst) REFERENCES Instrutor(ID)
);

CREATE TABLE Prereq (
    IdCurso INT,
    IdPrereq INT,
    PRIMARY KEY (IdCurso, IdPrereq),
    FOREIGN KEY (IdCurso) REFERENCES Curso(IdCurso),
    FOREIGN KEY (IdPrereq) REFERENCES Curso(IdCurso)
);

-- POVOANDO BANCO --
INSERT INTO SalaDeAula (Predio, NumeroSala, Capacidade) VALUES
('PredioA', '101', 30),
('PredioA', '102', 25),
('PredioB', '201', 40),
('PredioB', '202', 35),
('PredioC', '301', 20);

INSERT INTO Departamento (NomeDept, Predio, Orcamento) VALUES
('Ciencia da Computacao', 'PredioA', 500000),
('Matematica', 'PredioB', 300000),
('Fisica', 'PredioC', 200000),
('Quimica', 'PredioA', 250000),
('Biologia', 'PredioB', 150000);

INSERT INTO Curso (IdCurso, Titulo, NomeDept, Creditos) VALUES
(101, 'Algoritmos', 'Ciencia da Computacao', 4),
(102, 'Calculo I', 'Matematica', 4),
(103, 'Fisica I', 'Fisica', 4),
(104, 'Quimica Geral', 'Quimica', 4),
(105, 'Biologia Geral', 'Biologia', 4);

INSERT INTO Instrutor (ID, Nome, NomeDept, Salario) VALUES
(1, 'Ana Silva', 'Ciencia da Computacao', 70000),
(2, 'Carlos Souza', 'Matematica', 65000),
(3, 'Pedro Almeida', 'Fisica', 60000),
(4, 'Maria Pereira', 'Quimica', 55000),
(5, 'Joao Costa', 'Biologia', 50000);

INSERT INTO Secao (IdCurso, IdSec, Semestre, Ano, Predio, NumeroSala, IdPeriodo) VALUES
(101, 1, '2024-1', 2024, 'PredioA', '101', 1),
(102, 1, '2024-1', 2024, 'PredioA', '102', 2),
(103, 1, '2024-1', 2024, 'PredioB', '201', 3),
(104, 1, '2024-1', 2024, 'PredioB', '202', 4),
(105, 1, '2024-1', 2024, 'PredioC', '301', 5);

INSERT INTO Ministra (ID, IdCurso, IdSec, Semestre, Ano) VALUES
(1, 101, 1, '2024-1', 2024),
(2, 102, 1, '2024-1', 2024),
(3, 103, 1, '2024-1', 2024),
(4, 104, 1, '2024-1', 2024),
(5, 105, 1, '2024-1', 2024);

INSERT INTO Aluno (ID, Nome, NomeDept, TotCred) VALUES
(1, 'Bruno Lima', 'Ciencia da Computacao', 20),
(2, 'Fernanda Oliveira', 'Matematica', 15),
(3, 'Gabriela Santos', 'Fisica', 18),
(4, 'Marcos Silva', 'Quimica', 16),
(5, 'Renata Ferreira', 'Biologia', 14);

INSERT INTO Realiza (ID, IdCurso, IdSec, Semestre, Ano, Nota) VALUES
(1, 101, 1, '2024-1', 2024, 9.5),
(2, 102, 1, '2024-1', 2024, 8.0),
(3, 103, 1, '2024-1', 2024, 7.5),
(4, 104, 1, '2024-1', 2024, 6.0),
(5, 105, 1, '2024-1', 2024, 8.5);

INSERT INTO Mentor (IdEst, IdInst) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO Periodo (IdPeriodo, Dia, HoraInicial, HoraFinal) VALUES
(1, 'Segunda-feira', '08:00:00', '10:00:00'),
(2, 'Terca-feira', '10:00:00', '12:00:00'),
(3, 'Quarta-feira', '13:00:00', '15:00:00'),
(4, 'Quinta-feira', '15:00:00', '17:00:00'),
(5, 'Sexta-feira', '17:00:00', '19:00:00');

-- Inserir tuplas na tabela Prereq
INSERT INTO Prereq (IdCurso, IdPrereq) VALUES
(101, 102),
(102, 103),
(103, 104),
(104, 105),
(105, 101);

-- CONSULTAS --
--a 
SELECT nome
FROM instrutor
WHERE nomedept = 'ADM'

--b 
FROM instrutor
WHERE nomedept = 'ADM' and salario >= 3000

--c
SELECT COUNT(nomedept)
FROM departamento

--d
SELECT predio, SUM(orcamento) AS soma_orcamento
FROM departamento
GROUP BY predio

--e 
SELECT nomedept, orcamento
FROM departamento
ORDER BY nomedept ASC
LIMIT 1

--f
SELECT nomedept, MAX(orcamento) as maior
FROM departamento
GROUP BY nomedept
ORDER BY maior DESC
LIMIT 1

--g Verifique qual a média salarial dos instrutores da universidade.
SELECT ROUND(AVG(salario),2) as media_salario
FROM instrutor

--h Para cada aluno, liste seu Id, nome, id_curso.
SELECT id, nome
FROM aluno