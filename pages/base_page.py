from selenium.common.exceptions import NoSuchElementException, \
    TimeoutException  # импортируем ошибку, которую будем отлавливать
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators

from .locators import AddToBasketLocators
import math
class BasePage(): # базовая страница, от которой будут унаследованы все остальные классы

    def __init__(self, browser, url, timeout=10):   # будем создавать объекты с браузером и ссылкой
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)    # Добавляем, чтобы для каждой page ждал по несколько секунд

    def open(self):     # метод, с помощью которого будем открывать страницу
        self.browser.get(self.url)


    def is_element_present(self, how, what):    # метод, проверяющий, есть ли элемент на странице
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):  # метод, проверяющий, что элемент не появляется на странице
        try:
            WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):     # проверяем, что на странице какой-либо элемент исчезает
        try:    # 1 - частота запроса (каждую секунду в течение 4 секунд проверяет) TimeoutExceptions - ignored_exceptions, здесь просто для наглядности*
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(expected_conditions.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self): # идем на страницу с логином (сначала для проверки делаем отрицательный тест)
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):     # если что-то пойдет не так, будет выдавать понятную ошибку
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
