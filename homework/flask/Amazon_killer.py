from flask import Flask, request, jsonify
from datetime import datetime

amazon_killer = Flask(__name__)

USERS_DATABASE = {}
CARTS_DATABASE = {}
CARTS_DETAILS_DATABASE = {}
user_counter = 1
card_counter = 1


class NoSuchUser(Exception):
    def __init__(self, user_id):
        self.user_id = user_id


class NoSuchCart(Exception):
    def __init__(self, cart_id):
        self.cart_id = cart_id


@amazon_killer.route('/users', methods=["POST"])
def create_user():
    global user_counter
    user = request.json

    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response['registration_timestamp']
    USERS_DATABASE[user_counter] = user

    user_counter += 1

    return response, 201


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_handler(e):
    return {'error': f'No such user {e}'}, 404


@amazon_killer.route('/users/<int:user_id>')
def get_user_info(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)

    return user


@amazon_killer.route('/users/<int:user_id>', methods=["PUT"])
def update_user(user_id):
    user = request.json

    data = request.get_json()
    user["name"] = data['name']
    user["email"] = data['email']

    try:
        USERS_DATABASE[user_id]['name'] = user['name']
        USERS_DATABASE[user_id]['email'] = user['email']
    except KeyError:
        raise NoSuchUser(user_id)

    return {"status": "success"}, 200


@amazon_killer.route('/users/<int:user_id>', methods=["DELETE"])
def delete_user(user_id):
    try:
        del USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)

    return {"status": "success"}, 200


@amazon_killer.route('/carts', methods=["POST"])
def create_cart():
    global card_counter
    cart = request.json

    user_id = request.get_json()['user_id']

    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "products": [
            {
                "product": 'Book: how to stop be boring',
                "price": 500,
            },
            {
                "product": 'fireworks',
                "price": 1500,
            }
        ]
    }

    cart["registration_timestamp"] = response['registration_timestamp']
    cart["user_id"] = response['user_id']
    cart["products"] = response['products']

    if user_id in USERS_DATABASE:
        CARTS_DATABASE[card_counter] = cart

        card_counter += 1
    else:
        raise NoSuchUser(user_id)

    return {
               "cart_id": card_counter - 1,
               "creation_time": response['registration_timestamp']
           }, 201


@amazon_killer.errorhandler(NoSuchCart)
def no_such_user_handler(e):
    return {'error': f'No such cart with id {e}'}, 404


@amazon_killer.route('/carts/<int:cart_id>')
def get_cart_info(cart_id):
    try:
        cart = CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)

    return cart


@amazon_killer.route('/carts/<int:cart_id>', methods=["PUT"])
def update_cart(cart_id):

    data = request.get_json()
    try:
        CARTS_DATABASE[cart_id]['user_id'] = data['user_id']
        CARTS_DATABASE[cart_id]['product'] = data['product']
    except KeyError:
        raise NoSuchCart(cart_id)

    return {"status": "success"}, 200


@amazon_killer.route('/carts/<int:cart_id>', methods=["DELETE"])
def delete_cart(cart_id):
    try:
        del CARTS_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)

    return {"status": "success"}, 200


if __name__ == '__main__':
    amazon_killer.run(debug=True)
