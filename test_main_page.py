import time

import pytest
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.main_page import MainPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_no_goods()
    page.should_be_a_message()

