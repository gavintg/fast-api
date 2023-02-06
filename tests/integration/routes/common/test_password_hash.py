from api.routes.common.password_hash import PasswordHash

password_hash = PasswordHash()

class TestPasswordHash:

    def test_get_hashed_password(self):
        hashed_password = password_hash.get_hashed_password('password')
        same_hashed_password = password_hash.get_hashed_password('password')
        assert hashed_password == same_hashed_password

    def test_check_hashed_password(self):
        plain_text_password = 'password'
        hashed_password = password_hash.get_hashed_password(plain_text_password)
        assert password_hash.check_hashed_password(plain_text_password, hashed_password)
