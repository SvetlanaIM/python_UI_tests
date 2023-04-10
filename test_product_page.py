import time
import pytest
from .pages.locators import BasketLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


#
# @pytest.mark.parametrize('links', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),    # помечаем ссылку как xfail
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.skip(reason="ignore for now to test other tests")
# def test_guest_can_add_product_to_basket(browser, links):  # тест, проверяющий, что можно добавить товар в корзину
#     link = links
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     time.sleep(1)
#     page.solve_quiz_and_get_code()
#     time.sleep(1)
#     page.should_be_the_right_product_after_adding_to_the_basket(link)
#     page.should_be_the_right_price_product_after_adding_to_the_basket(link)
#     # assert browser.find_element(*AddToBasketLocators.PRODUCT_NAME).text == browser.find_element(*AddToBasketLocators.PRODUCT_NAME_IN_BASKET).text, f'the name doesn\'t match on page {links}'
#     # assert browser.find_element(*AddToBasketLocators.PRODUCT_PRICE).text == browser.find_element(*AddToBasketLocators.PRODUCT_PRICE_IN_BASKET).text, f'the price doesn\'t match on page {links}'
@pytest.mark.skip(reason="ignore for now to test other tests")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="ignore for now to test other tests")
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="ignore for now to test other tests")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):  # проверяем, видно ли логин ссылку с любой страницы сайта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page() # переходим на другую страницу (логин пейдж), поэтому нужно создать новый page object
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


