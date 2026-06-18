import requests
import pytest
def test_get_user():
    response= requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code==200
    assert response.json()["id"]==1

def test_create_user():
    payload={"title":"Test","body":"QA","userId":1}
    response= requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code==201

def test_delete_user():
    response= requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code==200
    
    