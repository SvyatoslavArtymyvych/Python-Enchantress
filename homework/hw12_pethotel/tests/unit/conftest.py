import pytest

from hotel import create_app


@pytest.fixture
def pet_hotel():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client