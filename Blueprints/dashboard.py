from flask import Blueprint, render_template
import dbconfig

dashboard_bp = Blueprint("dashboard",__name__,url_prefix="/dashboard")

@dashboard_bp.route("/")
def daily_chart():
    tasks = dbconfig.fetch_tasks()  # Fetch all tasks
    
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