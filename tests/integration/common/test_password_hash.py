from api.routes.common.password_hash import PasswordHash

password_hash = PasswordHash()

class TestPasswordHash:

    def test_get_hashed_password(self):
        new_password = password_hash.get_hashed_password('password')
        next_password = password_hash.get_hashed_password('password')
        assert new_password == next_password

    def test_check_hashed_password(self):
        new_password = password_hash.get_hashed_password('password')
        assert password_hash.check_hashed_password('password', new_password)
