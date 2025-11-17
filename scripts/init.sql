-- Criação da tabela de ranking para o jogo
CREATE TABLE IF NOT EXISTS ranking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    apples INTEGER NOT NULL CHECK (apples >= 0),
    time REAL NOT NULL CHECK (time >= 0),
    score REAL NOT NULL CHECK (score >= 0)
);
