import requests
import pytest
from utils.logger import logger
def test_get_user():
    logger.info("Inicio del test de API - GET")
    response= requests.get("https://jsonplaceholder.typicode.com/posts/1")
    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code==200
    assert response.json()["id"]==1

def test_create_user():
    logger.info("Inicio del test de API - POST")
    payload={"title":"Test","body":"QA","userId":1}
    response= requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code==201

def test_delete_user():
    logger.info("Inicio del test de API - DELETE")
    response= requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    logger.info(f"Status Code: {response.status_code}")
    assert response.status_code==200
    
    