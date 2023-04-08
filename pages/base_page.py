class BasePage(): # базовая страница, от которой будут унаследованы все остальные классы

    def __init__(self, browser, url): # будем создавать объекты с браузером и ссылкой
        self.browser = browser
        self.url = url

    def open(self):     # метод, с помощью которого будем открывать страницу
        self.browser.get(self.url)

