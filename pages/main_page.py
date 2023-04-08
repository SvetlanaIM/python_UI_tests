# создаем page object для главной страницы сайта
from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):  # наследуемся, чтобы получить конструктор + методы базовой страницы
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
