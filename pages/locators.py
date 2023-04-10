from selenium.webdriver.common.by import By


# сюда будем добавлять все локаторы!

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    SUBMIT_REGISTER = (By.NAME, "registration_submit")


class BasketLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    GO_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini .btn:first-child")
    EMPTY_BASKET = (By.XPATH, "//div[@id='content_inner']/p")
    SOME_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".row h2")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# теперь каждый селектор — это пара: как искать и что искать.
