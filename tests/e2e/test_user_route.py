import json
import requests

class TestUser:

    def test_post_user(self):
        result = requests.post('http://localhost:8000/user', json={'username': 'anyuser', 'password': 'anypassword'})
        assert result.status_code == 200
        data = json.loads(result.content)
        self.user_id = data['user_id']
        assert self.user_id != 0

    def test_get_user(self):
        result = requests.get(f'http://localhost:8000/user/anyuser')
        assert result.status_code == 200
        data = json.loads(result.content)
        assert data['username'] == 'anyuser'