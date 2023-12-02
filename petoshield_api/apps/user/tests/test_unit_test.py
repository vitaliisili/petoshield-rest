import pytest
from apps.user.models import UserManager


@pytest.fixture
def user_manager():
    return UserManager()


class TestUserUnitTest:
    def test_user_manager_create_user_without_email(self, user_manager):
        with pytest.raises(ValueError):
            user_manager.create_user(email=None)

    def test_user_string_representation(self, simple_user):
        assert str(simple_user) == simple_user.name
