from .base_page import BasePage
from .locators import BasketLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_button()
        button = self.browser.find_element(*BasketLocators.BASKET_BUTTON)
        button.click()

    def should_be_button(self):
        assert self.is_element_present(
            *BasketLocators.BASKET_BUTTON), "There is no AddToBusket button on the page or it's not found"

    def should_be_the_right_product_after_adding_to_the_basket(self, link):
        assert self.browser.find_element(*BasketLocators.PRODUCT_NAME).text == self.browser.find_element(
            *BasketLocators.PRODUCT_NAME_IN_BASKET).text, f'the name doesn\'t match on page {link}'

    def should_be_the_right_price_product_after_adding_to_the_basket(self, link):
        assert self.browser.find_element(*BasketLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *BasketLocators.PRODUCT_PRICE_IN_BASKET).text, f'the price doesn\'t match on page {link}'

    def should_not_be_success_message(
            self):
        assert self.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *BasketLocators.SUCCESS_MESSAGE), "The success message didn't disappear, but it should have"
