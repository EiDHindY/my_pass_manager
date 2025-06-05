# db_schema
from db_config import db_conn


def db_init() -> None:

    with db_conn() as conn:

        cursor = conn.cursor()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL UNIQUE
                        )
            """
        )

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS sites(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    site_name TEXT NOT NULL UNIQUE
                )
            """
        )

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS passwords(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    site_id INTEGER NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    description TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id), 
                    FOREIGN KEY(site_id) REFERENCES sites(id)
                ) 
            """
        )
        conn.commit()


if __name__ == "__main__":
    db_init()
