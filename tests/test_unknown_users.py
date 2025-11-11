import requests

def test_unknown_users(base_url, headers):
    res = requests.get(f"{base_url}/unknown", headers=headers)
    assert res.status_code == 200
    
    data = res.json()
    users = data["data"]
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "year" in user
        assert "color" in user
