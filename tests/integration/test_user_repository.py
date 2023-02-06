import argon2
from api.routes.user_model import UserModel
from api.routes.user_repository import UserRepository

repository = UserRepository()

class TestUser:

    def test_insert_user(self):
        user = UserModel(username='testUser', password='testPassword')
        user_id = repository.insert(user)
        assert user_id != 0

    def test_select_by_username(self):
        repository.insert(UserModel(username='anotherUsername', password='anotherPassword'))
        user = repository.select_by_username('anotherUsername')
        assert user.username == 'anotherUsername'
        assert user.password == argon2.hash_password('anotherPassword'.encode('UTF-8'))

