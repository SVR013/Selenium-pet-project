from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_CHECKOUT_ORDER = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-block")
    CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators:
    EMAIL_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTRATION2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_MESSAGE = (By.CSS_SELECTOR, '.alertinner.wicon')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    COST_BASKET = (By.CSS_SELECTOR, '.basket-mini')
    PRICE_BOOK = (By.CSS_SELECTOR, '.price_color')
    NAME_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")