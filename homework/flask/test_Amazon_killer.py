from freezegun import freeze_time
from Amazon_killer import amazon_killer as app
import pytest


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time('2021-02-08 14:16:41')
def test_create_user(store_app):
    response = store_app.post(
        '/users',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com",
        })
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": '2021-02-08T14:16:41'
    }


def test_get_user_no_such_user(store_app):
    user_id = 0

    response = store_app.get(f'users/{user_id}')

    assert response.status_code == 404
    assert response.json == {'error': f'No such user {user_id}'}


def test_put_user_no_such_user(store_app):
    user_id = 0

    response = store_app.put(
        f'/users/{user_id}',
        json={
            "name": "Illia",
            "email": "illia.sukonnik@gmail.com",
        }
    )

    assert response.status_code == 404
    assert response.json == {'error': f'No such user {user_id}'}


def test_delete_user_no_such_user(store_app):
    user_id = 0

    response = store_app.get(f'users/{user_id}')
    print(response)

    assert response.status_code == 404
    assert response.json == {'error': f'No such user {user_id}'}


@freeze_time('2021-02-08 14:16:41')
def test_create_cart(store_app):
    user_id = 0

    response = store_app.post(
        '/carts',
        json={
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
        })

    assert response.status_code == 404
    assert response.json == {
        "error": f"No such user {user_id}"
    }


def test_get_cart_no_such_user(store_app):
    cart_id = 0

    response = store_app.get(f'carts/{cart_id}')

    assert response.status_code == 404
    assert response.json == {'error': f'No such cart with id {cart_id}'}


def test_put_cart_no_such_user(store_app):
    cart_id = 0

    response = store_app.put(
        f'/carts/{cart_id}',
        json={
            "user_id": 1,
            "products": [
                {
                    "product": 'fireworks',
                    "price": 1500,
                }
            ]
        })

    assert response.status_code == 404
    assert response.json == {'error': f'No such cart with id {cart_id}'}


def test_delete_cart_no_such_cart(store_app):
    cart_id = 0

    response = store_app.get(f'users/{cart_id}')
    print(response)

    assert response.status_code == 404
    assert response.json == {'error': f'No such user {cart_id}'}
