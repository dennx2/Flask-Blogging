from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models.posts import Post
from .models.users import User
from .models.comments import Comment
from .models.likes import Like
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    posts = Post.query.all()
    comments = Comment.query.all()
    return render_template("home.html", posts=posts)


@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("Post cannot be empty.", category="error")
        else:
            post = Post(text=text, author_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created!", category="success")
            return redirect(url_for("views.home"))
    return render_template("create_post.html")


@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post does not exist", category="error")
    elif current_user.id != post.author_id:
        flash("You don't have permission to delete this post.", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.", category="success")
    return redirect(url_for("views.home"))


@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("No user with that username exist.", category="error")
        return render_template(url_for("views.home"))

    posts = user.posts
    return render_template("posts.html", posts=posts, username=username)


@views.route("/create-comment/<post_id>", methods=["POST"])
@login_required
def create_comment(post_id):
    text = request.form.get("text")
    if not text:
        flash("Comment cannnot be empty.", category="error")
    else:
        post = Post.query.filter_by(id=post_id).first()
        if post:
            comment = Comment(
                text=text, author_id=current_user.id, post_id=post.id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash("Post doesn't exist.", category="error")
    return redirect(url_for("views.home"))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if not comment:
        flash("Comment does't exist.", category="error")
    elif current_user.id != comment.author_id and current_user.id != comment.post.author_id:
        flash("You don't have permission to delete this comment.", category="error")
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for("views.home"))

@views.route("/like-post/<post_id>")
def like_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    like = Like.query.filter_by(author_id=current_user.id, post_id=post_id).first()

    if post is None:
        flash("Post does not exist.", category="error")
    elif like is None:
        like = Like(author_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
    else:
        db.session.delete(like)
        db.session.commit()
        
    return redirect(url_for("views.home"))





