import requests

class TestUser:

    def test_post_user(self):
        result = requests.post('http://localhost:8000/user', json={'username': 'gavin', 'password': 'password'})
        assert result.status_code == 200
        #data = json.loads(result.content)
        #assert data['message'] == 'Hello World'

    def test_get_user(self):
        result = requests.get('http://localhost:8000/user/1')
        assert result.status_code == 200
        #data = json.loads(result.content)
        #assert data['message'] == 'Hello World'