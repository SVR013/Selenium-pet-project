from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url.find('login') != -1, f'The string \'login\' is not in the given url {self.url.find}'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        login_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION2)
        password2_field.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()
        assert self.browser.find_element(*LoginPageLocators.LOGIN_MESSAGE), 'Failed to register'