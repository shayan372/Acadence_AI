
import sqlite3
import pandas as pd


import os

DB_NAME = os.path.join(
    os.path.dirname(__file__),
    "acadence.db"
)

def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_NAME)


def initialize_database():
    """Create the tasks table if it does not exist."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            course TEXT NOT NULL,
            task_type TEXT NOT NULL,
            deadline TEXT NOT NULL,
            estimated_hours REAL NOT NULL,
            progress INTEGER DEFAULT 0,
            importance TEXT NOT NULL,
            status TEXT DEFAULT 'Not Started',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_task(
    task_name,
    course,
    task_type,
    deadline,
    estimated_hours,
    progress,
    importance,
    status
):
    """Add a new academic task."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (
            task_name,
            course,
            task_type,
            deadline,
            estimated_hours,
            progress,
            importance,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        task_name,
        course,
        task_type,
        deadline,
        estimated_hours,
        progress,
        importance,
        status
    ))

    conn.commit()
    conn.close()


def get_tasks():
    """Return all tasks as a Pandas DataFrame."""

    conn = get_connection()

    query = """
        SELECT * FROM tasks
        ORDER BY deadline ASC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def delete_task(task_id):
    """Delete a task using its ID."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()
