import json
import requests
from api.routes.user_model import UserModel
from api.routes.user_repository import UserRepository

class TestUser:

    def test_post_token_success(self):
        user_repository = UserRepository()
        user_repository.insert(UserModel(username='ValidTokenUser', password='ValidTokenPassword'))
        result = requests.post('http://localhost:8000/token', json={
            'grant_type': 'password', 
            'scope': 'read_write', 
            'client_id': 'ValidTokenUser', 
            'client_secret': 'ValidTokenPassword'})
            
        assert result.status_code == 200
        data = json.loads(result.content)
        assert data['access_token'] != None
        assert data['token_type'] == 'Bearer'


    def test_post_token_failed(self):
        result = requests.post('http://localhost:8000/token', json={
            'grant_type': 'password', 
            'scope': 'read_write', 
            'client_id': 'InvalidTokenUser', 
            'client_secret': 'InvalidTokenPassword'})
        assert result.status_code == 401
