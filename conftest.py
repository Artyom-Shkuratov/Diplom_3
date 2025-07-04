import pytest
from selenium import webdriver
import pytest
from selenium import webdriver
from urls import Urls, ApiUrls
from helpers import GeneratorData as GD
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param.lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.browser_name = browser_name
    
    yield driver
    
    driver.quit()
    
@pytest.fixture(scope='function')
def register_user():
    
    payload = GD.generate_random_user_data()
    email = payload['email']
    password= payload['password']
    response = requests.post(ApiUrls.CREATE_USER, json=payload)
    if response.status_code != 200:
        pytest.skip("Пользователь не зарегистрирован")
    access_token = response.json().get("access_token")
    
    # Отдаём в тест
    yield {
        "email": email,
        "password": password,
        "access_token": access_token
    }
    requests.delete(ApiUrls.DELETE_USER, headers={"Authorization": access_token})
    