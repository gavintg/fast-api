from api.routes.user_model import UserModel
from api.routes.user_repository import UserRepository
from api.routes.common.password_hash import PasswordHash

repository = UserRepository()

class TestUserRepository:

    def test_insert_user(self):
        user = UserModel(username='testUser', password='testPassword')
        user_id = repository.insert(user)
        assert user_id != 0

    def test_select_by_username(self):
        repository.insert(UserModel(username='anotherUsername', password='anotherPassword'))
        user = repository.select_by_username('anotherUsername')
        assert user.username == 'anotherUsername'
        assert PasswordHash().check_hashed_password('anotherPassword', user.hashed_password)

