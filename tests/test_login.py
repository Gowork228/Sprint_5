import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.urls import UrlsForTests
from test_data.test_data import *

from web_locators.locators import *


class TestLogin:

    #  Вход по кнопке 'Войти в аккаунт' на главной
    def test_login_valid_data_from_main_page_successes(self, driver):
        driver.get(UrlsForTests.BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_LOGIN_BUTTON)).click()

        driver.find_element(*LoginLocators.LL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*LoginLocators.LL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
        driver.find_element(*LoginLocators.LL_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL

    #  Вход через кнопку 'Личный кабинет'
    def test_login_valid_data_use_profile_button_successes(self, driver):
        driver.get(UrlsForTests.BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_PROFILE_BUTTON)).click()
        driver.find_element(*MainPageLocators.MP_PROFILE_BUTTON).click()

        driver.find_element(*LoginLocators.LL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*LoginLocators.LL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
        driver.find_element(*LoginLocators.LL_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL

    #  Вход через кнопку в форме регистрации
    def test_login_valid_data_from_register_page_successes(self, driver):
        driver.get(UrlsForTests.REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegisterLocators.RL_LOGIN_BUTTON)).click()

        driver.find_element(*LoginLocators.LL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*LoginLocators.LL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
        driver.find_element(*LoginLocators.LL_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL

     # Вход через кнопку в форме восстановления пароля
    def test_login_valid_data_from_forgot_password_page_successes(self, driver):
        driver.get(UrlsForTests.FORGOT_PASSWORD_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ResetPasswordLocators.RPL_LOGIN_BUTTON)).click()

        driver.find_element(*LoginLocators.LL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*LoginLocators.LL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
        driver.find_element(*LoginLocators.LL_LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL






