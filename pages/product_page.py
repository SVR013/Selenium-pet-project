from selenium.common import TimeoutException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def checking_if_the_book_has_been_added_to_the_cart(self):
        get_cart_cost = self.browser.find_element(*ProductPageLocators.COST_BASKET)
        find_out_the_cost_of_the_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK)
        basket_value = get_cart_cost.text.split(' ')[2]
        book_value = find_out_the_cost_of_the_book.text
        assert book_value.find(basket_value), 'Book not added to cart'

    def checking_the_product_name_in_the_purchase_message(self):
        get_book_name = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        get_book_name_in_message = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_MESSAGE)
        assert get_book_name.text == get_book_name_in_message.text, 'The titles of the books in the basket and in fact do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element has not disappeared"


    def should_be_no_goods(self):
        assert self.is_not_element_present(*MainPageLocators.BUTTON_CHECKOUT_ORDER), \
            "There is an item in the cart"

    def should_be_a_message(self):
        message = self.browser.find_element(*MainPageLocators.CART_MESSAGE)
        assert message.text.find('пуста'), 'There are items in the cart'