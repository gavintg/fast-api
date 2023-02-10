import json
import requests
from api.routes.token_repository import TokenRepository

class TestPurchase:

    token_repository = TokenRepository()

    def test_get_purchases(self):
        token = self.token_repository.insert_token()
        
        response = requests.get('http://localhost:8000/purchase', headers={"token" : token})
        assert response.status_code == 200
        assert response.content != None