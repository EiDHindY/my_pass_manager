# db_schema.py

from database.db_config import db_conn


def db_init() -> None:
    """
    Initializes the database by creating the required tables:
    - users: holds unique user names.
    - sites: holds unique site names.
    - passwords: holds login credentials linking users and sites.

    Ensures tables are created only if they don't already exist.
    """

    with db_conn() as conn:
        cursor = conn.cursor()

        # Table for storing users
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL UNIQUE
            );
            """
        )

        # Table for storing sites (e.g., Facebook, Gmail)
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site_name TEXT NOT NULL UNIQUE
            );
            """
        )

        # Table for storing passwords linked to a user and a site
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                site_id INTEGER NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,  -- Store as ISO 8601 string
                description TEXT,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE
            );
            """
        )

        # Commit changes explicitly (redundant in context manager but good practice)
        conn.commit()


# Optional: Run this script directly to initialize the DB
if __name__ == "__main__":
    db_init()
