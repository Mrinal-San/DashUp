from flask import Flask, render_template, redirect, url_for
from task import task_bp  #importing the task module
import dbconfig  #importing the database configuration
from datetime import date

app = Flask(__name__)

#creating a table using the module(dbconfig)
dbconfig.create_table()

#register the task.py
app.register_blueprint(task_bp)

@app.route("/")
def home():
    username="REN"
    return render_template("views/home.html", user=username)

@app.route("/finance")
def finance_home():
    return render_template("views/finance.html")

@app.route("/dashboard")
def dashboard():
    tasks = dbconfig.fetch_task()  # Fetch all tasks
    
    # Make sure each tuple has 3 elements
    tasks_clean = []
    for t in tasks:
        if len(t) == 3:
            tasks_clean.append(t)
        else:
            # If is_done is missing, assume 0
            task_id, task_name = t
            tasks_clean.append((task_id, task_name, 0))

    total = len(tasks_clean)
    completed = sum(task[2] for task in tasks_clean)
    pending = total - completed
    completion_percent = round((completed / total) * 100, 2) if total else 0

    return render_template(
        "views/dashboard.html",
        total=total,
        completed=completed,
        pending=pending,
        completion_percent=completion_percent
    )
    
if __name__ =="__main__":
    app.run(debug=True)