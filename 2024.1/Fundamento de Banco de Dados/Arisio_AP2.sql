CREATE TABLE Professor (
    Matricula INT PRIMARY KEY,
    CPF VARCHAR(11) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Data_nascimento DATE NOT NULL,
    Salario FLOAT NOT NULL,
    Endereco VARCHAR(200) NOT NULL,
    Sexo CHAR(1) NOT NULL,
    Contato VARCHAR(15) NOT NULL
);

CREATE TABLE Disciplina (
    Id_disciplina SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL
);

CREATE TABLE Curso (
    Id_curso SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL
);

CREATE TABLE Aluno (
    Matricula INT PRIMARY KEY,
    CPF VARCHAR(11) NOT NULL,
    Nome VARCHAR(100) NOT NULL,
    Sexo CHAR(1) NOT NULL,
    Endereco VARCHAR(200) NOT NULL,
    Contato VARCHAR(15) NOT NULL,
    Data_matricula DATE NOT NULL,
    Id_curso INT,
    FOREIGN KEY (Id_curso) REFERENCES Curso(Id_curso)
);

CREATE TABLE Turma (
    Id_turma SERIAL PRIMARY KEY,
    Id_disciplina INT,
    Matricula_aluno INT,
    Matricula_professor INT,
    FOREIGN KEY (Id_disciplina) REFERENCES Disciplina(Id_disciplina),
    FOREIGN KEY (Matricula_aluno) REFERENCES Aluno(Matricula),
    FOREIGN KEY (Matricula_professor) REFERENCES Professor(Matricula)
);

INSERT INTO Curso (Nome) VALUES ('Sistemas de Informação'), 
('Medicina'), ('Fisiterapia');

INSERT INTO Professor (Matricula, CPF, Nome, Data_nascimento, Salario, Endereco, Sexo, Contato) 
VALUES 
(1, '20210101512', 'Professor A', '1970-01-01', 7000, 'Rua 1, 123', 'M', '88998075912'),
(2, '93147124253', 'Professor B', '1980-02-02', 7000, 'Rua 2, 123', 'F', '88998092959'),
(3, '34567892123', 'Professor C', '1990-03-03', 10000, 'Rua 3, 123', 'M', '8513941231');

INSERT INTO Aluno (Matricula, CPF, Nome, Sexo, Endereco, Contato, Data_matricula, Id_curso) 
VALUES 
(1, '20210101531', 'Arisio', 'M', 'Rua A, 123', '444444444', '2022-01-01', 1),
(2, '20210101532', 'Andrade', 'M', 'Rua B, 123', '555555555', '2022-02-02', 2),
(3, '20210101533', 'Junior', 'M', 'Rua C, 123', '666666666', '2022-03-03', 3);

INSERT INTO Disciplina (Nome) VALUES ('Matemática'),
('Biologia'), ('História');

INSERT INTO Turma (Id_disciplina, Matricula_aluno, Matricula_professor) 
VALUES (1, 1, 1),(2, 2, 2),(3, 3, 3),(1, 3, 1);

UPDATE Aluno SET Id_curso = 3 WHERE Matricula = 1;
UPDATE Aluno SET Id_curso = 1 WHERE Matricula = 2;

DELETE FROM Turma WHERE Matricula_professor = 3;
DELETE FROM Professor WHERE Matricula = 3;

INSERT INTO Professor (Matricula, CPF, Nome, Data_nascimento, 
					   Salario, Endereco, Sexo, Contato) 
VALUES (4, '45678901234', 'Professor D', '1985-04-04', 8000, 
		'Rua 4, 456', 'F', '777777777');


