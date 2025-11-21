import os
import sqlite3
from typing import TYPE_CHECKING, Optional

#if TYPE_CHECKING:
#    from ..entities.player import Player


class Database:

    def __init__(self, dbPath: str = "database.db") -> None:

        self._dbPath = dbPath
        self._connection: Optional[sqlite3.Connection] = None
        self._cursor: Optional[sqlite3.Cursor] = None

        if not os.path.exists(self._dbPath):
            try:
                self._create(scriptPath="scripts/init.sql")
            except Exception as e:
                raise RuntimeError(f"Erro ao criar o banco de dados: {e}")

        try:
            self._connection = self._connect()
        except Exception as e:
            raise RuntimeError(f"Erro ao conectar ao banco de dados: {e}")

    def _connect(self) -> sqlite3.Connection:
        try:
            if not self._connection:
                self._connection = sqlite3.connect(self._dbPath)
                self._connection.execute("PRAGMA foreign_keys = ON")
                self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            raise RuntimeError(f"Falha ao abrir conexão com o database: {e}")
        return self._connection

    def _create(self, scriptPath: str) -> None:
        try:
            with open(scriptPath, 'r', encoding='utf-8') as scriptFile:
                script = scriptFile.read()
        except FileNotFoundError:
            raise RuntimeError(f"Arquivo de criação do banco não encontrado: {scriptPath}")
        except Exception as e:
            raise RuntimeError(f"Erro ao ler script SQL: {e}")

        try:
            with self._connect() as connection:
                cursor = connection.cursor()
                cursor.executescript(script)
                connection.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao criar tabelas: {e}")

    def insertScore(self, playerName: str, playerApples: int, playerTime: int, playerScore: int) -> None:
        query = "INSERT INTO ranking (name, apples, time, score) VALUES (?, ?, ?, ?)"
        params = (playerName, playerApples, playerTime, playerScore)

        try:
            self._cursor.execute(query, params)
            self._connection.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao inserir score no ranking: {e}")

    def getHighScores(self) -> list:
        query = "SELECT id, name, apples, time, score FROM ranking ORDER BY score DESC, id ASC LIMIT 10"

        try:
            self._cursor.execute(query)
            return self._cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao obter os high scores: {e}")

    def close(self) -> None:
        try:
            if self._cursor:
                self._cursor.close()
            if self._connection:
                self._connection.close()
        except Exception:
            pass
