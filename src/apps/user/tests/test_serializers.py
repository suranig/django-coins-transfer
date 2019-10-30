import pytest

from apps.user.models import User
from apps.user.serializers import UserSerializer

pytestmark = pytest.mark.django_db


class TestUserSerializer:

    @pytest.fixture(autouse=True)
    def setup_method(self, db):
        self.user_attributes = {
            'id': 1,
            'username': 'Testuser',
            'email': 'tuser@g.com',
            'first_name': 'Test',
            'last_name': 'User'}

        self.serializer_data = {
            'id': 2,
            'username': 'Testuser2',
            'email': 'tuser2@g.com',
            'first_name': 'Test2',
            'last_name': 'User2'}

        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        assert set(data.keys()) == \
               set(['id', 'username', 'email', 'first_name', 'last_name'])

    @pytest.mark.parametrize(
        "data_field,user_attributes_field",
        [('id', 'id'),
         ('username', 'username'),
         ('email', 'email'),
         ('first_name', 'first_name'),
         ('last_name', 'last_name'),
         pytest.param('id', 'username', marks=pytest.mark.xfail)],
    )
    def test_field_content(self, data_field, user_attributes_field):
        data = self.serializer.data
        assert data[data_field] == self.user_attributes[user_attributes_field]
