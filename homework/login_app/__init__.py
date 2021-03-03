import click
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    api = Api(app=app)

    app.config['SECRET_KEY'] = 'my_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import Login, SignUp, LogOut
    api.add_resource(Login, '/login')
    api.add_resource(SignUp, '/signup')
    api.add_resource(LogOut, '/logout')

    # from .auth import Test
    # api.add_resource(Test, '/test')
    #
    # blueprint for non-auth parts of app
    from .main import MainPage, Profile, OrderPage
    api.add_resource(MainPage, '/')
    api.add_resource(Profile, '/profile')
    api.add_resource(OrderPage, '/order')

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    @app.cli.command('create-db')
    def create_db():
        db.create_all()

    return app
