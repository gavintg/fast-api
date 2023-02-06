from api.routes.token_repository import TokenRepository

repository = TokenRepository()

class TestTokenRepository:

    token = repository.insert_token()

    def test_insert_token(self):
        assert self.token != None

    def test_validate_token(self):
        is_valid = repository.validate_token(self.token)
        assert is_valid == True
