from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def should_be_no_goods(self):
        assert self.is_not_element_present(*MainPageLocators.BUTTON_CHECKOUT_ORDER), \
            "There is an item in the cart"

    def should_be_a_message(self):
        message = self.browser.find_element(*MainPageLocators.CART_MESSAGE)
        assert message.text.find('пуста'), 'There are items in the cart'