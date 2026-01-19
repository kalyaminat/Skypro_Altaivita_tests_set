from Altaivita.uipages.Mainpage import MainPage
from Altaivita.uipages.Cartpage import CartPage
from .conftest import browser
from time import sleep
import allure
from .constants import main_url, cart_url


@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Добавление товара в корзину")
@allure.description("Добавление товара и превью цены товара в корзине на главной странице")
def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()
    main_page.get_mini_cart_price()
    assert main_page.get_mini_cart_price() != '0 ₽', "Сумма в корзине нулевая"

@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Проверка суммы")
@allure.description("Переход на страницу корзины, проверка суммы")
def test_sum_cart_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()
    main_page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.open()
    cart_page.get_total_sum_from_cart()
    total_sum = cart_page.get_total_sum_from_cart()
    assert total_sum.replace('₽','').strip().isdigit() and len(total_sum.replace('₽','').strip()) > 1, \
        "Сумма в корзмне состоит из одного знака 0"

@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Удаление товаров их корзины")
@allure.description("Удаление товаров и проверка, что сумма равна 0")
def test_cart_is_empty(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()
    main_page.go_to_cart()
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.delete_goods_from_cart()
    sleep(10)
    total_sum = cart_page.get_total_sum_from_cart()
    
    assert total_sum.replace('₽', '').strip() == '0', "Сумма в корзине не равна 0"



