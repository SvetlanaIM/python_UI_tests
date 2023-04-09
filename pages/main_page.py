# создаем page object для главной страницы сайта
from selenium.webdriver.common.by import By

from .base_page import BasePage # чтобы импортировать, нужно ставить точку


class MainPage(BasePage):  # наследуемся, чтобы получить конструктор + методы базовой страницы
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):     # сделали так, чтобы в случае, если не найдет кнопку, выдавал понятную ошибку
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        # is_element_present - прописан у нас в бейз пейдж, там проверяет, если ли кнопка и вызывает исключение, если нет, возвращает тру/фолс
