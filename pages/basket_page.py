from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):

# здесь должны быть методы со всеми проверками

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET),  "the basket is not empty"

    def should_not_be_any_products_in_busket(self):
        assert self.is_not_element_present(*BasketLocators.SOME_PRODUCTS_IN_BASKET)



