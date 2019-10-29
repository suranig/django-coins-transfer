import pytest
from django.core.exceptions import ValidationError
from apps.user.models import User
from apps.transfer.models import Transfer


pytestmark = pytest.mark.django_db


@pytest.fixture
def mike():
    return User.objects.create(username='Mike', balance=150)


@pytest.fixture
def harvey():
    return User.objects.create(username='Harvey',
                               balance=5000,
                               password='abcdefgh')


def test_user_instance_mike(mike):
    assert mike.username == 'Mike'
    assert mike.balance == 150


def test_user_isntance_harvey(harvey):
    assert harvey.username == 'Harvey'
    assert harvey.username != 'Mike'
    assert harvey.balance == 5000, 'Harvey current balance should be 5000.'
    assert harvey.password == 'abcdefgh'


def test_mike_profile(mike):
    assert mike.username == 'Mike'
    assert mike.balance == 150


def test_harvey_profile(harvey):
    assert harvey.username == 'Harvey'
    assert harvey.balance != 150
    assert harvey.balance == 5000


def test_mike_sent_20_coins_to_harvey(mike, harvey):
    t = Transfer.objects.create(sender=mike, receiver=harvey, amount=20)
    assert t.amount == 20
    assert t.sender.balance <= 150
    assert t.sender.balance == 130
    assert t.receiver.balance >= 5000
    assert t.receiver.balance == 5020


def test_harvey_sent_50_coins_to_mike(mike, harvey):
    t = Transfer.objects.create(sender=harvey, receiver=mike, amount=50)
    assert t.amount == 50
    assert t.sender.balance == 4950
    assert t.receiver.balance == 200


@pytest.mark.xfail(raises=ValidationError)
def test_mike_sent_coins_to_himself_by_miss_click_and_got_error(mike):
        Transfer.objects.create(sender=mike, receiver=mike, amount=50)


@pytest.mark.xfail(raises=ValidationError)
def test_mike_tried_to_send_200_coins_to_harvey_and_got_error(mike, harvey):
    # Mike got error because he owns only 150 coins
    Transfer.objects.create(sender=mike, receiver=harvey, amount=200)


@pytest.mark.xfail(raises=ValidationError)
def test_harvey_sent_0_coins_to_mike_by_miss_click(mike, harvey):
    Transfer.objects.create(sender=harvey, receiver=mike, amount=0)
