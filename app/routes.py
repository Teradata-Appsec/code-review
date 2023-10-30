from flask import render_template, request, redirect, url_for
import flask_login
from sqlalchemy import select
from app import app
from app.models.todo import Todo

from app.models.user import User
from app import db


@app.route("/")
def index():
    return redirect(url_for("profile"))


@app.route("/login")
def login():
    msg = request.args.get("msg")
    return render_template("login.html", msg=msg)


@app.route("/login", methods={"POST"})
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()

    if not user:
        return redirect(url_for("login", msg="User not found"))

    if user.password_hash == password:
        flask_login.login_user(user)
        return redirect(url_for("index"))

    return redirect(url_for("login", msg="Invalid login credentials"))


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("login", msg="You have been logged out"))


@app.route("/profile")
def profile():
    user = flask_login.current_user
    if user.is_authenticated:
        todos = Todo.query.filter_by(user_id=user.id).all()
        return render_template("profile.html", user=user, todos=todos)
    return redirect(url_for("login"))


@app.route("/profile", methods=["POST"])
@flask_login.login_required
def profile_post():
    user = flask_login.current_user
    todo_text = request.form.get("todoText")
    print("Got todoText", todo_text)

    todo = Todo(user.id, todo_text)

    db.session.add(todo)
    db.session.commit()

    return redirect(url_for("profile"))
