from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

def test_create_account():
    response = client.post('/accounts/', json={'account_number': '1234567890', 'balance': 100.0, 'owner': 'John Doe'})
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 100.0
    assert response.json()['owner'] == 'John Doe'

def test_read_account():
    response = client.get('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 100.0
    assert response.json()['owner'] == 'John Doe'

def test_update_account():
    response = client.put('/accounts/1', json={'balance': 200.0})
    assert response.status_code == 200
    assert response.json()['balance'] == 200.0

def test_delete_account():
    response = client.delete('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '1234567890'
    assert response.json()['balance'] == 200.0
    assert response.json()['owner'] == 'John Doe'