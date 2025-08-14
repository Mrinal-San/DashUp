from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    username="REN"
    return render_template("views/home.html", user=username)

@app.route("/finance")
def finance_home():
    return render_template("views/finance.html")

@app.route("/task")
def task_home():
    tasks=['workout','meditation','homework']
    return render_template("views/task.html",my_tasks=tasks)
    
if __name__ ==("__main__"):
    app.run(debug=True)