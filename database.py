import sqlite3
from datetime import datetime
from config import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                first_name TEXT,
                username TEXT,
                score INTEGER DEFAULT 0,
                quizzes_taken INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS quiz_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                question_id INTEGER,
                is_correct INTEGER,
                points INTEGER,
                answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def register_user(user_id: int, first_name: str, username: str = None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (user_id, first_name, username)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                first_name = excluded.first_name,
                username = excluded.username
            """,
            (user_id, first_name, username),
        )
        conn.commit()


def record_quiz_answer(user_id: int, question_id: int, is_correct: bool, points: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO quiz_logs (user_id, question_id, is_correct, points)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, question_id, 1 if is_correct else 0, points),
        )
        cursor.execute(
            """
            UPDATE users
            SET score = score + ?,
                quizzes_taken = quizzes_taken + 1,
                correct_answers = correct_answers + ?
            WHERE user_id = ?
            """,
            (points, 1 if is_correct else 0, user_id),
        )
        conn.commit()


def get_user_stats(user_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT user_id, first_name, username, score, quizzes_taken, correct_answers, joined_at
            FROM users
            WHERE user_id = ?
            """,
            (user_id,),
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None


def get_top_users(limit: int = 10):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT user_id, first_name, username, score, correct_answers, quizzes_taken
            FROM users
            ORDER BY score DESC, correct_answers DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [dict(row) for row in cursor.fetchall()]
