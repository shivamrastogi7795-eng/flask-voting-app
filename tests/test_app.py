import json

from app import app


def test_root_and_health_endpoints():
    client = app.test_client()

    home_response = client.get('/')
    health_response = client.get('/health')

    assert home_response.status_code == 200
    assert home_response.data.decode() == 'Welcome to the App'
    assert health_response.status_code == 200
    assert health_response.data.decode() == 'App is running'
