import math
from selenium.common import NoAlertPresentException
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


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