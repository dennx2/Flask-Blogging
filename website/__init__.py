from flask import Flask
from os import path
from .config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(database_uri=f"sqlite:///{DB_NAME}"):

    # App config
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    # Import Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Import db models
    from .models.users import User
    from .models.posts import Post
    from .models.comments import Comment
    from .models.likes import Like
    
    # Init Database
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app
