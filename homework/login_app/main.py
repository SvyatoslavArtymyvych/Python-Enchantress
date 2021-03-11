from flask_login import login_required, current_user
from flask import request
from flask_restful import Resource
from .models import Order

from . import db


class MainPage(Resource):
    def get(self):
        return {"message": "Welcome on main page"}, 200


class Profile(Resource):
    @login_required
    def get(self):
        return {"name": current_user.name}, 200


class OrderPage(Resource):
    @login_required
    def get(self):
        orders = Order.query.filter_by(user_id=current_user.id).all()

        if orders:
            response = {}
            for i in orders:
                response['order_%s' % i.id] = {
                    'creation_time': i.creation_time,
                    'product_id': i.product_id
                }
            return {"orders": response}, 200
        else:
            return {'error': 'order is empty'}, 404

    def post(self):
        from datetime import datetime
        response = request.get_json()
        product_id = response['product_id']
        creation_time = '%s' % datetime.now()

        order = Order(user_id=current_user.id,
                      creation_time=creation_time,
                      product_id=product_id)

        db.session.add(order)
        db.session.commit()

        return {"status": "success"}, 200
