import json
import requests

class TestPurchase:

    def test_get_purchases(self):
        result = requests.post('http://localhost:8000/token', json={
            'grant_type': 'password', 
            'scope': 'read_write', 
            'client_id': 'ValidTokenUser', 
            'client_secret': 'ValidTokenPassword'})
        data = json.loads(result.content)
        
        response = requests.get('http://localhost:8000/purchase', 
                headers={"token" : data['access_token']})
        assert response.status_code == 200
        assert response.content != None