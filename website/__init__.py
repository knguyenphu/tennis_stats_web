from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .notes import notes_page
    from .auth import auth
    from .landing import landing
    from .about import about
    from .stats import stats
    from .plan import plan

    app.register_blueprint(notes_page, name="notes",url_prefix='/')
    app.register_blueprint(auth, name="auth",url_prefix='/')
    app.register_blueprint(landing, name="landing",url_prefix='/')
    app.register_blueprint(about, name="about",url_prefix='/')
    app.register_blueprint(stats, name="stats",url_prefix='/')
    app.register_blueprint(plan, name="plan",url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
