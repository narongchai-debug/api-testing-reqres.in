import requests

def test_login_success(base_url, headers):
    payload = {
        'email': 'george.bluth@reqres.in', 
        'password': '12345'
    }

    res = requests.post(f"{base_url}/login", json=payload, headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert "token" in data

def test_login_missing_password(base_url, headers):
    payload = {
        'email' : 'george.bluth@reqres.in'
    }
    
    res = requests.post(f"{base_url}/login", json=payload,headers=headers)
    assert res.status_code == 400
    data = res.json()
    assert data["error"] == "Missing password"

def test_login_user_not_found(base_url, headers):
    #Email not found
    payload = {
        "email": "george.bluth@reqres.ins", 
        "password": "123456"
    }

    res = requests.post(f"{base_url}/login", json=payload,headers=headers)
    assert res.status_code == 400
    data = res.json()
    assert data["error"] == "user not found"


    
