from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models.posts import db, Post

views = Blueprint("views", __name__)

@views.route("/") 
@views.route("/home")
@login_required
def home():
    return render_template("home.html")

@views.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("Post cannot be empty.", category="error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created!", category="success")
    return render_template("create_post.html")