from flask import Flask, render_template, redirect, url_for
from Blueprints.task import task_bp  #importing the task module
from Blueprints.dashboard import dashboard_bp  #importing the task module
import dbconfig  #importing the database configuration
from datetime import date


app = Flask(__name__)

#creating a table using the module(dbconfig)
dbconfig.create_tasks()

#register the task.py
app.register_blueprint(task_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    username="REN"
    return render_template("views/home.html", user=username)

@app.route("/login")
def login():
    return render_template("views/login.html")

@app.route("/register")
def register():
    return render_template("views/register.html")
    
@app.route("/loading")
def slow():
    import time
    time.sleep(3)  # simulate heavy work
    return render_template("views/loader.html") 

@app.route("/finance")
def finance_home():
    return render_template("views/finance.html")


if __name__ =="__main__":
    app.run(debug=True)