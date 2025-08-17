import sqlite3

#reset daily checks
from datetime import date

db_tasks = "instance/tasks.db"
db_users = "instance/users.db"

# TASKS
def create_tasks():
    with sqlite3.connect(db_tasks) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks(
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0,
                last_updated DATE
            )
        ''')
        conn.commit()

def insert_tasks(task_name, is_done=0):
    with sqlite3.connect(db_tasks) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (task_name, is_done) VALUES (?, ?)",
            (task_name, is_done)
        )
        conn.commit()

def delete_tasks(task_id):
    with sqlite3.connect(db_tasks) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
        conn.commit()

def fetch_tasks():
    with sqlite3.connect(db_tasks) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()

def mark_tasks_done(task_id):
    conn = sqlite3.connect(db_tasks)
    cursor = conn.cursor()
    # Update is_done to 1 for the given task_id
    cursor.execute('''
        UPDATE tasks
        SET is_done = 1
        WHERE task_id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
        
def update_tasks_status(task_id, is_done):
    conn = sqlite3.connect(db_tasks)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET is_done=? WHERE task_id=?', (is_done, task_id))
    conn.commit()
    conn.close()



#reset function
def reset_tasks_status_daily():
    today = date.today()
    conn = sqlite3.connect(db_tasks)
    cursor = conn.cursor()

    # Reset all tasks that are not updated today
    cursor.execute('''
        UPDATE tasks
        SET is_done = 0, last_updated = ?
        WHERE last_updated != ? OR last_updated IS NULL
    ''', (today, today))

    conn.commit()
    conn.close()
    
    
#USERS
def create_users():
    with sqlite3.connect(db_users)as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name VARCHAR(50) NOT NULL,
                        last_name VARCHAR(50) NOT NULL,
                        user_email VARCHAR(100) UNIQUE NOT NULL,
                        password_hash VARCHAR(255) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                       ''')
        conn.commit()

def insert_users(first_name, last_name, user_email, password_hash):
    try:
        with sqlite3.connect(db_users) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO users (first_name, last_name, user_email, password_hash)
                VALUES (?, ?, ?, ?)
                """,
                (first_name, last_name, user_email, password_hash)
            )
            conn.commit()
        return True, "User added successfully"

    except sqlite3.IntegrityError:
        return False, "Email already registered"
    except Exception as e:
        return False, f"Database error: {str(e)}"
    
def delete_users(user_id):
    with sqlite3.connect(db_users) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE user_id = ?",(user_id,))
        conn.commit()
        return f"deleted user {user_id}"

def fetch_users():
    with sqlite3.connect(db_users) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()


def get_user_by_email(user_email):
    try:
        with sqlite3.connect(db_users) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE user_email = ?", (user_email,))
            user = cursor.fetchone()  # returns None if not found
        return user
    except Exception as e:
        print("Database error:", e)
        return None