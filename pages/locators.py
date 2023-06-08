from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    # PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    # EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    # PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    COST_BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRICE_BOOK = (By.CSS_SELECTOR, '.price_color')
    NAME_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')