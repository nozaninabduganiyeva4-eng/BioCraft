import sqlite3
import hashlib
import time
from datetime import datetime, date
from config import DB_PATH, COOLDOWN_SECONDS, DAILY_REQUEST_LIMIT


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
                selected_style TEXT DEFAULT 'aesthetic',
                requests_today INTEGER DEFAULT 0,
                last_request_date TEXT,
                last_request_timestamp REAL DEFAULT 0,
                total_requests INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ai_cache (
                cache_key TEXT PRIMARY KEY,
                response_text TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()


def register_or_update_user(user_id: int, first_name: str, username: str = None):
    today_str = date.today().isoformat()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO users (user_id, first_name, username, last_request_date)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
                first_name = excluded.first_name,
                username = excluded.username
            """,
            (user_id, first_name, username, today_str),
        )
        conn.commit()


def get_user_style(user_id: int) -> str:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT selected_style FROM users WHERE user_id = ?", (user_id,))
        row = cursor.fetchone()
        if row and row["selected_style"]:
            return row["selected_style"]
        return "aesthetic"


def set_user_style(user_id: int, style: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET selected_style = ? WHERE user_id = ?",
            (style, user_id),
        )
        conn.commit()


def check_rate_limit(user_id: int) -> tuple[bool, str, int]:
    """
    Foydalanuvchi so'rov yubora oladimi yoki yo'qligini tekshiradi.
    Qaytaradi: (mumkinmi: bool, sabab: str, kutish_soniyasi: int)
    """
    now = time.time()
    today_str = date.today().isoformat()

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT requests_today, last_request_date, last_request_timestamp
            FROM users WHERE user_id = ?
            """,
            (user_id,),
        )
        row = cursor.fetchone()

        if not row:
            return True, "", 0

        last_date = row["last_request_date"]
        requests_today = row["requests_today"] or 0
        last_time = row["last_request_timestamp"] or 0

        # Yangi kun bo'lsa kunlik hisoblagichni yangilaymiz
        if last_date != today_str:
            requests_today = 0
            cursor.execute(
                "UPDATE users SET requests_today = 0, last_request_date = ? WHERE user_id = ?",
                (today_str, user_id),
            )
            conn.commit()

        # 1. Cooldown tekshiruvi (soniya)
        elapsed = now - last_time
        if elapsed < COOLDOWN_SECONDS:
            remaining = int(COOLDOWN_SECONDS - elapsed) + 1
            return False, f"⏳ Iltimos, {remaining} soniya kuting (spamlardan himoya).", remaining

        # 2. Kunlik limit tekshiruvi
        if requests_today >= DAILY_REQUEST_LIMIT:
            return (
                False,
                f"🛑 Sizning kunlik bepul so'rov limitingiz ({DAILY_REQUEST_LIMIT} ta) tugadi.\nErtaga yangilanadi!",
                0,
            )

        return True, "", 0


def record_successful_request(user_id: int):
    now = time.time()
    today_str = date.today().isoformat()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE users
            SET requests_today = requests_today + 1,
                total_requests = total_requests + 1,
                last_request_timestamp = ?,
                last_request_date = ?
            WHERE user_id = ?
            """,
            (now, today_str, user_id),
        )
        conn.commit()


def make_cache_key(task_type: str, user_input: str, style: str) -> str:
    raw = f"{task_type.strip().lower()}:{style.strip().lower()}:{user_input.strip().lower()}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def get_cached_response(cache_key: str) -> str | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT response_text FROM ai_cache WHERE cache_key = ?",
            (cache_key,),
        )
        row = cursor.fetchone()
        if row:
            return row["response_text"]
        return None


def save_cached_response(cache_key: str, response_text: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO ai_cache (cache_key, response_text)
            VALUES (?, ?)
            ON CONFLICT(cache_key) DO UPDATE SET response_text = excluded.response_text
            """,
            (cache_key, response_text),
        )
        conn.commit()


def get_user_profile(user_id: int) -> dict:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT user_id, first_name, username, selected_style,
                   requests_today, total_requests, created_at
            FROM users WHERE user_id = ?
            """,
            (user_id,),
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return {
            "user_id": user_id,
            "first_name": "Foydalanuvchi",
            "username": "",
            "selected_style": "aesthetic",
            "requests_today": 0,
            "total_requests": 0,
            "created_at": "Hozir",
        }
