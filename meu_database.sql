CREATE TABLE Aluno (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    data_ingresso DATE NOT NULL
);

---

CREATE TABLE Curso (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria VARCHAR(50) NOT NULL,
    valor_inscricao DECIMAL(8, 2) NOT NULL,
    status BOOLEAN NOT NULL DEFAULT 1
);

---

CREATE TABLE Matricula (
    id INTEGER PRIMARY KEY,
    aluno_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    status BOOLEAN NOT NULL DEFAULT 1,
    data_matricula DATE NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES aluno(id) ON DELETE CASCADE,
    FOREIGN KEY (curso_id) REFERENCES curso(id) ON DELETE CASCADE
);

---Valor Total Devido
SELECT
    T1.nome AS aluno_nome,
    SUM(T3.valor_inscricao) AS total_devido
FROM
    aluno AS T1
JOIN
    matricula AS T2 ON T1.id = T2.aluno_id
JOIN
    curso AS T3 ON T2.curso_id = T3.id
WHERE
    T2.status = 0
GROUP BY
    T1.nome
HAVING
    total_devido > 0;