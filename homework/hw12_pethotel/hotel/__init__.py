from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import Flask

from .middleware import OurMiddleware

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.wsgi_app = OurMiddleware(app.wsgi_app)
    api = Api(app=app)

    app.config['SECRET_KEY'] = 'my_secret'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://svyatoslav:pass@localhost:5432/svyatoslav'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .main import MainPage, RoomPage, SettlementPage, EvictionPage, ActivitiesPage
    api.add_resource(MainPage, '/')
    api.add_resource(RoomPage, '/room/<int:room_id>')
    api.add_resource(SettlementPage, '/settlement')
    api.add_resource(EvictionPage, '/eviction')
    api.add_resource(ActivitiesPage, '/activities')

    @app.cli.command('recreate-db')
    def create_db():
        db.drop_all()
        db.create_all()

    return app
