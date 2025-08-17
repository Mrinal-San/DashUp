from flask import Blueprint, redirect, url_for, request, render_template
from werkzeug.security import generate_password_hash, check_password_hash

import dbconfig

# Separate blueprints for register and login
register_bp = Blueprint("register", __name__, url_prefix="/register")
login_bp = Blueprint("login", __name__, url_prefix="/login")

# ------------------- REGISTER -------------------
@register_bp.route("/")
def display_users():
    users = dbconfig.fetch_users()
    return render_template("views/register.html", my_users=users)

@register_bp.route("/add", methods=["POST"])
def add_users():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    user_email = request.form.get("user_email")
    password = request.form.get("password")

    # Hash the password before saving
    password_hash = generate_password_hash(password)

    # Insert user with all fields together
    success, message = dbconfig.insert_users(first_name, last_name, user_email, password_hash)

    if success:
        return redirect(url_for("register.display_users"))
    else:
        # Pass error message to template
        return render_template("views/register.html", error=message, my_users=dbconfig.fetch_users())

@register_bp.route("/delete/<int:user_id>", methods=["POST"])
def delete_users(user_id):
    dbconfig.delete_users(user_id)
    return redirect(url_for("register.display_users"))

# ------------------- LOGIN -------------------
@login_bp.route("/")
def login_page():
    return render_template("views/login.html")

@login_bp.route("/auth", methods=["POST"])
def login_auth():
    user_email = request.form.get("user_email")
    password = request.form.get("password")

    user = dbconfig.get_user_by_email(user_email)
    if not user:
        return render_template("views/login.html", error="User not found")

    # Assuming table schema: id, first_name, last_name, user_email, password_hash
    password_hash = user[4]  

    if check_password_hash(password_hash, password):
        return redirect(url_for("home"))  # or wherever you want to go
    else:
        return render_template("views/login.html", error="Invalid password")

