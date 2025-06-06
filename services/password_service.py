from typing import Optional
from database.db_config import db_conn
from utils import egypt_timezone
from sqlite3 import IntegrityError, Error, Cursor
import logging


logger = logging.getLogger(__name__)


def add_password(
    user_id: int,
    site_id: int,
    username: str,
    password: str,
    description: Optional[str] = None,
) -> Optional[int]:
    """
    Inserts a new password record into the 'passwords' table for a specific user and site.

    Args:
        user_id (int): The foreign key ID referencing the 'users' table.
        site_id (int): The foreign key ID referencing the 'sites' table.
        username (str): The username associated with the site login.
        password (str): The plain-text password (consider hashing in future).
        description (Optional[str]): Optional description or note for the password entry.

    Returns:
        Optional[int]: The auto-generated ID (primary key) of the inserted password record,
                    or None if an error occurred during insertion.
    """

    # Get the current time in Egypt's timezone as an ISO 8601 string (e.g., "2025-06-06T12:30:45")
    created_at: str = egypt_timezone()

    # Use context manager to ensure the connection is safely opened and closed
    with db_conn() as conn:
        # Create a cursor object to execute SQL queries
        cursor: Cursor = conn.cursor()

        try:
            # Insert the new password record into the 'passwords' table
            cursor.execute(
                """
                INSERT INTO passwords (
                    user_id,
                    site_id,
                    username,
                    password,
                    created_at,
                    description
                ) VALUES (?, ?, ?, ?, ?, ?);
                """,
                (user_id, site_id, username, password, created_at, description),
            )

            # Commit the transaction to make changes permanent
            conn.commit()

            # Return the ID of the newly inserted row
            return cursor.lastrowid

        except IntegrityError as e:
            # Raised when a foreign key or unique constraint is violated
            logging.error(f"[ERROR] Integrity Error: {e}")
            return None

        except Error as e:
            # Catches other database-related errors such as SQL syntax issues
            logging.error(f"[ERROR] Database error occurred: {e}")
            return None
