import time

from .base_page import BasePage
from .locators import AddToBasketLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):    # добавляем товар в корзину
        self.should_be_button()
        button = self.browser.find_element(*AddToBasketLocators.BASKET_BUTTON)
        button.click()

    def should_be_button(self):     # проверяем, есть ли кнопка добавления товара в корзину
        assert self.is_element_present(*AddToBasketLocators.BASKET_BUTTON), "There is no AddToBusket button on the page or it's not found"

    def should_be_the_right_product_after_adding_to_the_basket(self, link):
        assert self.browser.find_element(*AddToBasketLocators.PRODUCT_NAME).text == self.browser.find_element(
            *AddToBasketLocators.PRODUCT_NAME_IN_BASKET).text, f'the name doesn\'t match on page {link}'

    def should_be_the_right_price_product_after_adding_to_the_basket(self, link):
        assert self.browser.find_element(*AddToBasketLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *AddToBasketLocators.PRODUCT_PRICE_IN_BASKET).text, f'the price doesn\'t match on page {link}'

    def should_not_be_success_message(self):    # проверяем, что на странице нет сообщения о том, что товар добавлен в корзину
        assert self.is_not_element_present(*AddToBasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def success_message_should_disappear(self): # проверяем, ушло ли сообщение на странице
        assert self.is_disappeared(*AddToBasketLocators.SUCCESS_MESSAGE), "The success message didn't disappear, but it should have"
