from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    # Переход на 'Соусы'
    def test_constructor_go_to_sauces_scroll_to_sauces(self, valid_login):
        driver = valid_login

        driver.find_element(*MainPageLocators.MP_SAUSE_SECTION).click()
        sauces_section = driver.find_element(*MainPageLocators.MP_SAUSE_SECTION)

        assert sauces_section.text == 'Соусы'

    #  Переход на 'Начинки'
    def test_constructor_go_to_filling_scroll_to_filling(self, valid_login):
        driver = valid_login

        driver.find_element(*MainPageLocators.MP_FILLING_SECTION).click()
        filling_section = driver.find_element(*MainPageLocators.MP_FILLING_SECTION)

        assert filling_section.text == 'Начинки'

    #  Переход на 'Булки'
    def test_constructor_go_to_bun_scroll_to_bun(self, valid_login):
        driver = valid_login

        driver.find_element(*MainPageLocators.MP_FILLING_SECTION).click()
        driver.find_element(*MainPageLocators.MP_BREAD_SECTION).click()
        bun_section = driver.find_element(*MainPageLocators.MP_BREAD_SECTION)

        assert bun_section.text == 'Булки'

