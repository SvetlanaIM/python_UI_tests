import time

import pytest
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage   # каждую папку/файл ставим точку
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


# pytest -v --tb=line --language=en test_main_page.py

def test_guest_can_go_to_login_page(browser):   # тест, заходящий на страницу
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)  # создаем объект - первая страница = main_page
    page.open()     # переходим на нее
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)    # создаем уже второй объект - вторую страницу. Это второй вариант перехода на страницу!
    # второй вариант - в main_page создаем объект, когда переходим со с главной страницы на логин пейдж в методе go_to_login_page
    login_page.should_be_login_page()   # проверяем, находимся ли мы на верной странице
    # относится к первому методу перехода на страницу:
    # login_page = page.go_to_login_page()  # получаем логин пейдж из метода перехода на страницу
    # login_page.should_be_login_page() # проверяем, находимся ли мы на этой странице


def test_guest_should_see_login_link(browser):  # тест, проверяющий, есть ли кнопка на странице
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_link()     # проверяем, есть ли на странице кнопка с корзиной
    main_page.go_to_basket_page()       # переходим на страницу с корзиной
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_not_be_any_products_in_busket()

# pytest -s -m "new" test_main_page.py


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()       # переходим на страницу с корзиной
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_not_be_any_products_in_busket()







