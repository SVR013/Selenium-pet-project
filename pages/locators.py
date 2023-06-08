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