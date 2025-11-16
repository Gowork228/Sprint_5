import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.urls import UrlsForTests
from test_data.test_data import *

from web_locators.locators import *


class TestRegistration:

    def test_registration_valid_data_successful_registration(self, driver):
        driver.get(UrlsForTests.REGISTER_URL)

        driver.find_element(*RegisterLocators.RL_NAME_FIELD).send_keys(RandomTestData.USER_NAME)
        driver.find_element(*RegisterLocators.RL_EMAIL_FIELD).send_keys(RandomTestData.LOGIN)
        driver.find_element(*RegisterLocators.RL_PASSWORD_FIELD).send_keys(RandomTestData.PASSWORD)
        driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginLocators.LL_LOGIN_BUTTON))

        assert driver.current_url == UrlsForTests.LOGIN_URL


    def test_registration_empty_name_zero_result(self, driver):
        driver.get(UrlsForTests.REGISTER_URL)

        driver.find_element(*RegisterLocators.RL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*RegisterLocators.RL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)
        driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegisterLocators.RL_REGISTER_BUTTON))

        assert driver.current_url == UrlsForTests.REGISTER_URL and driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).is_displayed()


    @pytest.mark.parametrize('invalid_email_list', ['lll@y', 'lllyan.ru', 'lll @yan.ru', 'lll@ya n.ru',
        '@yan.ru', 'lll@.ru', 'lll@yan.'])
    def test_registration_invalid_email_not_registered(self, driver, invalid_email_list):
        driver.get(UrlsForTests.REGISTER_URL)

        driver.find_element(*RegisterLocators.RL_NAME_FIELD).send_keys(MyTestData.USER_NAME)
        driver.find_element(*RegisterLocators.RL_EMAIL_FIELD).send_keys(invalid_email_list)
        driver.find_element(*RegisterLocators.RL_PASSWORD_FIELD).send_keys(MyTestData.PASSWORD)

        driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegisterLocators.RL_REGISTER_BUTTON))

        assert driver.current_url == UrlsForTests.REGISTER_URL and driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).is_displayed()


    @pytest.mark.parametrize('invalid_password_list', ['1', '11111'])
    def test_registration_short_password_failed_registration(self, driver, invalid_password_list):
        driver.get(UrlsForTests.REGISTER_URL)

        driver.find_element(*RegisterLocators.RL_NAME_FIELD).send_keys(MyTestData.USER_NAME)
        driver.find_element(*RegisterLocators.RL_EMAIL_FIELD).send_keys(MyTestData.LOGIN)
        driver.find_element(*RegisterLocators.RL_PASSWORD_FIELD).send_keys(invalid_password_list)
        driver.find_element(*RegisterLocators.RL_REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(RegisterLocators.RL_ERROR_MESSAGE))
        error_message = driver.find_element(*RegisterLocators.RL_ERROR_MESSAGE)

        assert error_message.text in 'Некорректный пароль'