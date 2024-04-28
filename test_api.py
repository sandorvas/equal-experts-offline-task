import requests

def test_get_gists():
    response = requests.get('http://localhost:8080/gists')
    assert response.status_code == 200
    gists = response.json()
    assert isinstance(gists, list)

