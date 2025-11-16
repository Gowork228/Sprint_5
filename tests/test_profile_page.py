import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_data.urls import UrlsForTests
from test_data.test_data import *

from web_locators.locators import *

class TestProfilePage:

    #  Переход по клику на 'Личный кабинет'
    def test_click_profile_button_open_profile_page(self, valid_login):
        driver = valid_login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        logout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(ProfileLocators.PL_LOGOUT_BUTTON))

        assert driver.current_url == UrlsForTests.PROFILE_URL and logout_button.text == 'Выход'

    #  Переход из личного кабинета в конструктор по клику на «Конструктор»
    def test_click_constructor_button_open_constructor(self, valid_login):
        driver = valid_login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfileLocators.PL_CONSTRUCTOR_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL

    #  Переход из личного кабинета в конструктор по клику на логотип Stellar Burgers
    def test_click_logo_open_constructor(self, valid_login):
        driver = valid_login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfileLocators.PL_LOGO_STELLAR_BURGER)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.MP_BREAD_SECTION))

        assert driver.current_url == UrlsForTests.BASE_URL

    #  Выход по кнопке «Выйти» в личном кабинете
    def test_click_logout_button_open_login_page(self, valid_login):
        driver = valid_login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MP_PROFILE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ProfileLocators.PL_LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(LoginLocators.LL_LOGIN_BUTTON))

        assert driver.current_url == UrlsForTests.LOGIN_URL