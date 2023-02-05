from api.routes.user_model import UserModel
from api.routes.user_repository import UserRepository

repository = UserRepository()

class TestUser:

    def test_insert_user(self):
        user = UserModel(username='testUser', password='testPassword')
        user_id = repository.insert(user)
        assert user_id != 0

    def test_select_by_id(self):
        user_id = repository.insert(UserModel(username='anotherUsername', password='anotherPassword'))
        user = repository.select_by_id(user_id)
        assert user.username == 'anotherUsername'
        assert user.password != 'anotherPassword' # should be md5 hash
        assert user.id == user_id

