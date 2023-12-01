class TestUserUnitTest:
    def test_user_string_representation(self, simple_user):
        assert str(simple_user) == simple_user.name
