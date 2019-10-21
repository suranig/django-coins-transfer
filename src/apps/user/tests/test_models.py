import pytest

from apps.user.models import User


pytestmark = pytest.mark.django_db


@pytest.fixture
def mike():
    return User.objects.create(username='Mike23',
                               first_name='Mike',
                               last_name='Ross',
                               email='mike@gmail.com',
                               balance=15000)


def test_user_instance_mike(mike):
    assert mike.username == 'Mike23'
    assert mike.first_name == 'Mike'
    assert mike.last_name == 'Ross'
    assert mike.email == 'mike@gmail.com'
    assert mike.balance == 15000
    assert mike.is_superuser == False
    assert mike.is_staff == False
    assert mike.is_active == True
