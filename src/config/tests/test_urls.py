

def test_with_client_swagger_docs(client):
    response = client.get('/')
    assert response.status_code == 200


def test_with_client_auth_login(client):
    response = client.get('/auth/login/')
    assert response.status_code == 200
