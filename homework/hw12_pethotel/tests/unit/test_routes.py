from freezegun import freeze_time
from hotel import create_app
import pytest


@pytest.fixture
def pet_hotel():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


def test_main_page(pet_hotel):
    response = pet_hotel.get('/', headers={'api_token': 'token'})

    assert response.status_code == 200
    assert response.json == {"message": "Welcome on main page"}


def test_settlement(pet_hotel):
    room_id = 1

    response = pet_hotel.post(
        '/settlement',
        json={
            "name": "Bob",
            "phone_number": "1122",
            "pets": {
                "Vee": {"feed": "13:00"},
                "Eva": {"feed": "13:00"}
            },
            "room_id": room_id
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 200
    assert response.json == {"status": "success"}

    response = pet_hotel.post(
        '/settlement',
        json={
            "name": "Bob",
            "phone_number": "1122",
            "pets": {
                "Vee": {"feed": "13:00"},
                "Eva": {"feed": "13:00"}
            },
            "room_id": 1
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 404
    assert response.json == {"error": "phone number already exists"}

    response = pet_hotel.post(
        '/eviction',
        json={
            "pet_name": ['Vee', 'Eva'],
            "room_id": 1
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 200
    assert response.json == {
        "Vee": {
            "lived_days_in_hotel": 0
        },
        "Eva": {
            "lived_days_in_hotel": 0
        }
    }


def test_eviction(pet_hotel):
    response = pet_hotel.post(
        '/settlement',
        json={
            "name": "Petro",
            "phone_number": "2255",
            "pets": {
                "Jessica": {"feed": "13:00"},
                "Bonny": {"feed": "13:00"}
            },
            "room_id": 1
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 200
    assert response.json == {"status": "success"}

    response = pet_hotel.post(
        '/eviction',
        json={
            "pet_name": ['Jessica', 'Bonny'],
            "room_id": 1
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 200
    assert response.json == {
        "Jessica": {
            "lived_days_in_hotel": 0
        },
        "Bonny": {
            "lived_days_in_hotel": 0
        }
    }


def test_activities(pet_hotel):
    response = pet_hotel.post(
        '/settlement',
        json={
            "name": "Ivan",
            "phone_number": "1133",
            "pets": {
                "Boy": {"feed": "11:00"},
                "Anny": {"feed": "13:00"}
            },
            "room_id": 1
        },
        headers={'api_token': 'token'}
    )

    assert response.status_code == 200
    assert response.json == {"status": "success"}

    response = pet_hotel.get('/activities', headers={'api_token': 'token'})

    assert response.status_code == 200
    assert response.json == {
        "11:00": [
            {
                "pet_id": 2,
                "activity_type": "feed"
            }
        ],
        "13:00": [
            {
                "pet_id": 1,
                "activity_type": "feed"
            }
        ],

    }
