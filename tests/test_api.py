import requests
def test_get_user():
    response= requests.get("https://reqres.in/api/users/2")
    assert response.status_code==200
assert response.json()["data"]["id"]==2

def test_create_user():
    payload={"name":"Luciana","job":"QA"}
    response= requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code==201
    assert response.json()["name"]=="Luciana"

def test_delete_user():
    response= requests.delete("https://reqres.in/api/users/2")
    assert response.status_code==204