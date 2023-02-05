import json 
import requests

class TestMain:
    def test_main(self):
        result = requests.get("http://localhost:8000/")
        assert result.status_code == 200
        data = json.loads(result.content)
        assert data["message"] == "Hello World"
