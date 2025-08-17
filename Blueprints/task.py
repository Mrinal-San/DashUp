from flask import Blueprint, redirect, url_for, render_template, request
import dbconfig

task_bp = Blueprint("task", __name__, url_prefix="/task")

@task_bp.route("/")
def display_tasks():
    tasks=dbconfig.fetch_tasks()
    return render_template("views/task.html",my_tasks=tasks)

# Add task
@task_bp.route("/add",methods=["POST"])
def add_tasks():
    task_name = request.form.get("task_name")
    dbconfig.insert_tasks(task_name)
    return redirect(url_for("task.display_tasks", my_tasks=task_name))

# Delete task
@task_bp.route("/delete/<int:task_id>", methods=["POST"])
def delete_tasks(task_id):
    dbconfig.delete_tasks(task_id)
    return redirect(url_for("task.display_tasks"))

# Mark task done
@task_bp.route("/done/<int:task_id>", methods=["POST"])
def mark_done(task_id):
    data = request.get_json()  # This reads JSON payload
    if not data:
        return {"error": "Invalid data"}, 400
    
    is_done = data.get("is_done", 0)
    dbconfig.update_tasks_status(task_id, is_done)
    return {"success": True}





