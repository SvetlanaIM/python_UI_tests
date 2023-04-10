# создаем page object для главной страницы сайта
from selenium.webdriver.common.by import By
from .locators import MainPageLocators      # импортируем локаторы в мейн пейдж

from .base_page import BasePage # чтобы импортировать, нужно ставить точку


class MainPage(BasePage):  # наследуемся, чтобы получить конструктор + методы базовой страницы
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    # делаем заглушку - будет просто вызывать конструктор предка и передавать ему те же значения
    # наверняка просто с pass также бы работало






  # следующие тесты закомментированы, тк больше не нужны - мы их перенесли в бейз пейдж)
  #   def go_to_login_page(self):
  #       link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
  #       link.click()
  #       # return LoginPage(browser=self.browser, url=self.browser.current_url) относится к первому методу перехода на страницу
  #       # то есть возвращаем новый объект - текущую страницу, на которую перешли
  #
  #   def should_be_login_link(self):     # сделали так, чтобы в случае, если не найдет кнопку, выдавал понятную ошибку
  #       assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # is_element_present - прописан у нас в бейз пейдж, там проверяет, если ли кнопка и вызывает исключение, если нет, возвращает тру/фолс
        # *MainPageLocators.LOGIN_LINK - обращаемся к локатору через класс, * - тк будет кортеж, его надо распаковать (how, what в итоге)