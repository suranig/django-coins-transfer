

def test_users_endpoint_with_unauthenticated_client(client):
    response = client.get('/api/v1/users/')
    assert response.status_code == 403


def test_users_detail_endpoint_with_unauthenticated_client(client):
    response = client.get('/api/v1/users/2/')
    assert response.status_code == 403


def test_users_endpoint_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username,
                                          password=password)
    client.login(username=username, password=password)
    response = client.get('/api/v1/users/')
    assert response.status_code == 200


def test_users_detail_endpoint_with_authenticated_client(client,
                                                         django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username,
                                                 password=password)
    user2 = django_user_model.objects.create_user(username='user2')
    client.login(username=username, password=password)
    response = client.get(f'/api/v1/users/{user.id}/')
    assert response.status_code == 200
    response2 = client.get(f'/api/v1/users/{user2.id}/')
    assert response2.status_code == 200
