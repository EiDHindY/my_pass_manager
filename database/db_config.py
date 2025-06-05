import sys
import os
import sqlite3
from typing import Final


def base_path() -> str:
    """
    Determine the base directory path where the database file should be stored.

    This function handles two scenarios:
    1. When the script is 'frozen' (e.g., packaged with PyInstaller), it uses the directory
        containing the executable.
    2. When running normally, it uses the directory containing the source file.

    Returns:
        str: The base directory path where the database folder (`data/`) will be created.

    Example:
        If frozen -> 'C:/Program Files/MyApp/'
        If not frozen -> 'C:/Users/username/my_project/'
    """
    if getattr(sys, "frozen", False):
        # The application is frozen (e.g., packaged with PyInstaller).
        # Use the folder where the executable is located.
        return os.path.dirname(sys.executable)

    # The application is running normally.
    # Use the folder where this source file resides.
    return os.path.dirname(__file__)


def db_path() -> str:
    """
    Constructs the full file path to the SQLite database.

    - Ensures a 'data' subdirectory exists inside the base path.
    - Creates the subdirectory if it does not already exist.
    - Appends the database filename 'passwords.db' inside the 'data/' directory.

    Returns:
        str: Absolute path to the SQLite database file.

    Example return value:
        'C:/Users/username/my_project/data/passwords.db'
    """
    # Create path to a 'data' directory inside the base path
    my_db_path: Final[str] = os.path.join(base_path(), "data")

    # Create the 'data' folder if it doesn't exist
    os.makedirs(my_db_path, exist_ok=True)

    # Return the complete path to the SQLite database file
    return os.path.join(my_db_path, "passwords.db")


def db_conn() -> sqlite3.Connection:
    """
    Establishes and returns a connection to the SQLite database.

    - Connects to the database file located at the path returned by `db_path()`.
    - Ensures that foreign key constraints are enabled using a PRAGMA statement.

    Returns:
        sqlite3.Connection: An active connection object to interact with the database.

    Note:
        SQLite does not enforce foreign keys by default. The PRAGMA command enables them.
    """
    # Create a connection to the SQLite database
    conn: sqlite3.Connection = sqlite3.connect(db_path())

    # Enable foreign key constraints (important for relational integrity)
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn
