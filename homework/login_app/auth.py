from flask_login import login_user, logout_user, login_required
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_restful import Resource

from . import db


class Login(Resource):
    def get(self):
        return {"message": "Please enter your email and password"}, 200

    def post(self):
        response = request.get_json()
        email = response['email']
        password = response['password']
        remember = True if bool(response['remember']) else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return {"error": "User doesn't exist or password is wrong"}, 404

        login_user(user, remember=remember)
        return {"status": "success"}, 200


class SignUp(Resource):
    def get(self):
        return {"message": "Please enter your email, name and password"}, 200

    def post(self):
        data = request.get_json()
        email = data['email']
        name = data['name']
        password = data['password']

        user = User.query.filter_by(email=email).first()

        if user:
            return {"error": "email address already exists"}, 404

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return {"status": "success"}, 200


class LogOut(Resource):
    @login_required
    def get(self):
        logout_user()
        return {"status": "success"}, 200
