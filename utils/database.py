import os
import sqlite3
from typing import TYPE_CHECKING, Optional

#if TYPE_CHECKING:
#    from ..entities.player import Player


class Database:

    def __init__(self, db_path: str = "database.db") -> None:

        self._db_path = db_path
        self._connection: Optional[sqlite3.Connection] = None
        self._cursor: Optional[sqlite3.Cursor] = None

        if not os.path.exists(self._db_path):
            try:
                self._create(script_path="scripts/init.sql")
            except Exception as e:
                raise RuntimeError(f"Erro ao criar o banco de dados: {e}")

        try:
            self._connection = self._connect()
        except Exception as e:
            raise RuntimeError(f"Erro ao conectar ao banco de dados: {e}")

    def _connect(self) -> sqlite3.Connection:
        try:
            if not self._connection:
                self._connection = sqlite3.connect(self._db_path)
                self._connection.execute("PRAGMA foreign_keys = ON")
                self._cursor = self._connection.cursor()
        except sqlite3.Error as e:
            raise RuntimeError(f"Falha ao abrir conexão com o database: {e}")
        return self._connection

    def _create(self, script_path: str) -> None:
        try:
            with open(script_path, 'r', encoding='utf-8') as script_file:
                script = script_file.read()
        except FileNotFoundError:
            raise RuntimeError(f"Arquivo de criação do banco não encontrado: {script_path}")
        except Exception as e:
            raise RuntimeError(f"Erro ao ler script SQL: {e}")

        try:
            with self._connect() as connection:
                cursor = connection.cursor()
                cursor.executescript(script)
                connection.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao criar tabelas: {e}")

    def insert_score(self, player_name: str, player_apples: int, player_time: float, player_score: float) -> None:
        query = "INSERT INTO ranking (name, apples, time, score) VALUES (?, ?, ?, ?)"
        params = (player_name, player_apples, player_time, player_score)

        try:
            self._cursor.execute(query, params)
            self._connection.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Erro ao inserir score no ranking: {e}")

    def get_high_scores(self) -> list:
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
