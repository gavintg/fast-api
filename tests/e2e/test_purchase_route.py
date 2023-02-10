import json
import requests

class TestPurchase:

    def get_valid_user(self):
        requests.post('http://localhost:8000/user', json={'username': 'tokentest', 'password': 'mytokenpassword'})

    def get_access_token(self):
        result = requests.post('http://localhost:8000/token', json={
            'grant_type': 'password', 
            'scope': 'read_write', 
            'client_id': 'tokentest', 
            'client_secret': 'mytokenpassword'})
        assert result.status_code == 200
        data = json.loads(result.content)
        print("Firsttttt",data)
        return data['access_token']

    def test_get_purchases(self):
        self.get_valid_user()
        data = self.get_access_token()
        print("Thissss", data)
        
        response = requests.get('http://localhost:8000/purchase', 
                headers={"token" : data})
        assert response.status_code == 200
        assert response.content != None