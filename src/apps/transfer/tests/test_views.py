import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


def test_transfers_endpoint_with_unauthenticated_client(client):
    response = client.get('/api/v1/transfers/')
    assert response.status_code == 403


def test_transfers_endpoint_with_authenticated_client(client,
                                                      django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username,
                                          password=password)
    client.login(username=username, password=password)
    response = client.get('/api/v1/transfers/')
    assert response.status_code == 200


def test_transfer_post_endpoint_with_unauthenticated_user(client,
                                                          django_user_model):
    user2 = django_user_model.objects.create_user(username='user2',
                                                  password='bar')

    # for testing use only JSON FORMAT!
    data = {
        "amount": 10,
        "receiver": user2.id,
    }
    # unauthenticated user cannot sent transfers
    response = client.post('/api/v1/transfers/', data=data)
    assert response.status_code == 403


def test_transfer_post_endpoint_with_authenticated_client(client,
                                                          django_user_model):
    username = "user1"
    password = "bar"
    # current user
    django_user_model.objects.create_user(username=username,
                                          password=password)
    user2 = django_user_model.objects.create_user(username='user2',
                                                  password='bar')
    client.login(username=username, password=password)

    # for testing use only JSON FORMAT!
    data = {
        "amount": 10,
        "receiver": user2.id,
    }
    response = client.post('/api/v1/transfers/', data=data)
    assert response.status_code == 201
    assert response.data['amount'] == 10
    assert response.data['receiver'] == user2.id


# Current auth user tried to send 5663 coins when his balance was 5000
@pytest.mark.xfail(raises=ValidationError)
def test_transfer_post_endpoint_tried_to_send_to_much(client,
                                                      django_user_model):
    username = "user1"
    password = "bar"
    django_user_model.objects.create_user(username=username,
                                          password=password)
    user2 = django_user_model.objects.create_user(username='user2',
                                                  password='bar')
    client.login(username=username, password=password)
    data = {
        "amount": 5663,
        "receiver": user2.id,
    }
    client.post('/api/v1/transfers/', data=data)


@pytest.mark.xfail(raises=ValidationError)
def test_transfer_post_user_tried_to_send_coins_to_himself(client,
                                                           django_user_model):
    username = "user1"
    password = "bar"
    current_user = django_user_model.objects.create_user(username=username,
                                                         password=password)
    client.login(username=username, password=password)
    data = {
        "amount": 565,
        "receiver": current_user.id,
    }
    client.post('/api/v1/transfers/', data=data)


def test_transfer_post_endpoint_receiver_doesnt_exists(client,
                                                       django_user_model):
    username = "user1"
    password = "bar"
    # current user
    django_user_model.objects.create_user(username=username,
                                          password=password)
    client.login(username=username, password=password)
    data = {
        "amount": 145,
        "receiver": 2321,
    }
    response = client.post('/api/v1/transfers/', data=data)
    assert response.status_code == 400
