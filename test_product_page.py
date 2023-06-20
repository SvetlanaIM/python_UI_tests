import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

promo_book = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = promo_book + "0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = promo_book + "0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_not_be_any_products_in_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "1928374650")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_the_right_product_after_adding_to_the_basket(link)
        page.should_be_the_right_price_product_after_adding_to_the_basket(link)


@pytest.mark.parametrize('links', [promo_book + "0",
                                   promo_book + "1",
                                   promo_book + "2",
                                   promo_book + "3",
                                   promo_book + "4",
                                   promo_book + "5",
                                   promo_book + "6",
                                   pytest.param(promo_book + "7", marks=pytest.mark.xfail),
                                   promo_book + "8",
                                   promo_book + "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_the_right_product_after_adding_to_the_basket(link)
    page.should_be_the_right_price_product_after_adding_to_the_basket(link)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()
