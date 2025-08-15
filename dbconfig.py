import sqlite3

#reset daily checks
from datetime import date

db_name = "instance/tasks.db"

def create_table():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks(
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()

def insert_task(task_name, is_done=0):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task_name, is_done) VALUES (?, ?)",
            (task_name, is_done)
        )
        conn.commit()

def delete_task(task_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
        conn.commit()

def fetch_task():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

def mark_task_done(task_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Update is_done to 1 for the given task_id
    cursor.execute('''
        UPDATE tasks
        SET is_done = 1
        WHERE task_id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
        
def update_task_status(task_id, is_done):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET is_done=? WHERE task_id=?', (is_done, task_id))
    conn.commit()
    conn.close()



#reset function
def reset_task_status_daily():
    today = date.today()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Reset all tasks that are not updated today
    cursor.execute('''
        UPDATE tasks
        SET is_done = 0, last_updated = ?
        WHERE last_updated != ? OR last_updated IS NULL
    ''', (today, today))

    conn.commit()
    conn.close()