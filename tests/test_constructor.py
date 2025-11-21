from web_locators.locators import *

class TestStellarBurgersConstructorForm:

    # Переход на 'Соусы'
    def test_constructor_go_to_sauces_scroll_to_sauces(self, valid_login):
        driver = valid_login
        driver.find_element(*MainPageLocators.MP_SAUSE_SECTION).click()

        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

        assert active_tab.text == "Соусы"

    #  Переход на 'Начинки'
    def test_constructor_go_to_filling_scroll_to_filling(self, valid_login):
        driver = valid_login
        driver.find_element(*MainPageLocators.MP_FILLING_SECTION).click()

        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

        assert active_tab.text == "Начинки"

    #  Переход на 'Булки'
    def test_constructor_go_to_bun_scroll_to_bun(self, valid_login):
        driver = valid_login
        driver.find_element(*MainPageLocators.MP_FILLING_SECTION).click()
        driver.find_element(*MainPageLocators.MP_BREAD_SECTION).click()

        active_tab = driver.find_element(By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")
        assert active_tab.text == "Булки"

