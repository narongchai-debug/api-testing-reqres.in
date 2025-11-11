import requests

def test_get_users(base_url, headers):
    res = requests.get(f"{base_url}/users?page=1", headers=headers) 
    assert res.status_code == 200

    data = res.json()
    users = data["data"] #get users in data
    for user in users:
        assert "id" in user
        assert "email" in user
