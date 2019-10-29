

def test_users_endpoint_with_unauthenticated_client(client):
    response = client.get('/api/v1/users/')
    assert response.status_code == 403


def test_users_endpoint_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username,
                                          password=password)
    client.login(username=username, password=password)
    response = client.get('/api/v1/users/')
    assert response.status_code == 200
