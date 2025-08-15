from flask import Flask, render_template, redirect, url_for
from task import task_bp  #importing the task module
import dbconfig  #importing the database configuration


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
    
if __name__ =="__main__":
    app.run(debug=True)