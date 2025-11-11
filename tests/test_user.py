import requests

def test_get_user(base_url, headers):
    res = requests.get(f"{base_url}/users/2", headers=headers)
    print('api: ',base_url)
    assert res.status_code == 200
    data = res.json()
    user = data["data"]

    assert user["id"] == 2
    assert user["email"] == "janet.weaver@reqres.in"
    assert "first_name" in user
    assert "last_name" in user

    