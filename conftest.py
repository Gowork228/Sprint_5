import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_locators.locators import LoginLocators
from web_locators.locators import MainPageLocators

from test_data.test_data import MyTestData
from test_data.urls import UrlsForTests

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(UrlsForTests.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def valid_login(driver):
    driver.get(UrlsForTests.LOGIN_URL)
    driver.find_element(*LoginLocators.LL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
    driver.find_element(*LoginLocators.LL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
    driver.find_element(*LoginLocators.LL_LOGIN_BUTTON).click()

    WebDriverWait(driver,5).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))
    return driver