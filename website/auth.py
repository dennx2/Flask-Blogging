from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models.users import db, User

auth = Blueprint("auth", __name__)


@auth.app_context_processor
def inject_user():
    return dict(user = current_user)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash("Logged in!", category="success")
                print("Log in success!")
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect.", category="error")
        else:
            flash("Email does not exist.", category="error")

    return render_template("login.html")


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if email_exists:
            flash("Email is already taken.", category="error")
        elif username_exists:
            flash("Username is already taken.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(username) < 2:
            flash("Username is too short.", category="error")
        elif len(password1) < 6:
            flash("Password is too short.", category="error")
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(
                password1, method="scrypt"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("User created!", category="success")
            print("Sign up success!")
            return redirect(url_for("views.home"))

    return render_template("signup.html")

@login_required
@auth.route("/logout")
def logout():
    logout_user()
    flash("Logout successfully.", category="success")
    print("Log out success!")
    return redirect(url_for("views.home"))
