CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS poste (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    rua TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS problema (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    descricao TEXT NOT NULL
);
