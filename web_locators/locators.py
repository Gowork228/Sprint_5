from selenium.webdriver.common.by import By

class RegisterLocators:

    RL_NAME_FIELD = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")

    RL_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

    RL_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    RL_REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    RL_LOGIN_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")

    RL_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    RL_ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")

class LoginLocators:

    LL_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

    LL_PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")

    LL_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    LL_RESET_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Забыли пароль?']")

class ProfileLocators:

    PL_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

    PL_LOGO_STELLAR_BURGER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    PL_LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class MainPageLocators:

    MP_BREAD_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::*")

    MP_SAUSE_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::*")

    MP_FILLING_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::*")

    MP_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    MP_PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

class ResetPasswordLocators:

    RPL_EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")

    RPL_RESET_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    RPL_LOGIN_BUTTON = (By.XPATH, ".//a[text()='Войти']")