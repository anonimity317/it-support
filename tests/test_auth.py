import pytest
from website import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.app_context():
        with app.test_client() as client:
            yield client

def test_register(client):
    response = client.post('/sign-up', data={
        'username': 'admin',
        'first_name': 'admin',
        'password1': 'admin',
        'password2': 'admin',
    })
    assert response.status_code == 200

@pytest.mark.parametrize("username, password, expected_status", [
    ("admin", "admin", 200), # Successful login
    ("user1", "user", 200),  # Successful login for another user
    ("invalid_user", "wrong_pass", 401), # Invalid credentials
    ("", "admin", 400), # Empty username
    ("admin", "", 400) # Empty password
])
def test_login(client, username, password, expected_status):
    response = client.post('/login', data={
        'username': username,
        'password': password
    })
    assert response.status_code == expected_status

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302