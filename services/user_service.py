# user_service.py

from typing import Optional
from sqlite3 import IntegrityError, Error, Cursor
from database.db_config import db_conn


def add_user(name: str) -> Optional[int]:
    """
    Adds a new user to the database.

    Args:
        name (str): The name of the user to add. Must be unique.

    Returns:
        Optional[int]: The ID of the newly added user if successful,
                    or None if the user already exists or an error occurred.
    """
    try:
        with db_conn() as conn:
            cursor: Cursor = conn.cursor()

            # Insert the user name into the users table
            cursor.execute("INSERT INTO users (user_name) VALUES (?)", (name,))

            # Commit the transaction and return the inserted user ID
            conn.commit()
            return cursor.lastrowid

    except IntegrityError:
        print(f"[ERROR] Username '{name}' already exists.")
        return None

    except Error as e:
        print(f"[ERROR] Database error occurred: {e}")
        return None
