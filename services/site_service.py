# site_service.py

from typing import Optional
from sqlite3 import IntegrityError, Error, Cursor
from database.db_config import db_conn
from utils import logging_config
import logging

logging_config()
logger = logging.getLogger(__name__)

def add_site(site: str) -> Optional[int]:
    """
    Adds a new site to the 'sites' table in the database.

    Args:
        site (str): The name of the site to add (e.g., "Gmail", "YouTube").
                    This name must be unique.

    Returns:
        Optional[int]: The ID of the newly added site if insertion is successful,
                    or None if the site already exists or a database error occurred.
    """

    try:
        with db_conn() as conn:
            cursor: Cursor = conn.cursor()

            # Attempt to insert the site name into the database
            cursor.execute("INSERT INTO sites (site_name) VALUES (?);", (site,))

            # Commit the transaction to finalize the insert
            conn.commit()

            # Return the unique ID of the inserted row
            return cursor.lastrowid

    except IntegrityError:
        logging.error(f"[ERROR] Site name already exists: '{site}'")
        return None

    except Error as e:
        logging.error(
            f"[ERROR] Database error occurred while adding site '{site}': {e}"
        )
        return None
