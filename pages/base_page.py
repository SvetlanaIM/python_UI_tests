from selenium.common.exceptions import NoSuchElementException   # импортируем ошибку, которую будем отлавливать
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


