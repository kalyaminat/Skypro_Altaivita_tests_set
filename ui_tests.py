from decimal import Decimal

import allure

from uipages.Mainpage import MainPage
from uipages.Cartpage import CartPage


@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Добавление товара в корзину")
def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()

    with allure.step("Проверить, что сумма мини-корзины больше нуля"):
        price = CartPage.parse_price(main_page.get_mini_cart_price())
        assert price > Decimal("0"), "Сумма мини-корзины не больше нуля"


@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Сумма корзины совпадает с суммой мини-корзины")
def test_sum_cart_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()

    mini_cart_sum = CartPage.parse_price(
        main_page.get_mini_cart_price()
    )

    main_page.go_to_cart()
    cart_page = CartPage(browser)

    with allure.step("Проверить сумму товаров в корзине"):
        total_sum = CartPage.parse_price(
            cart_page.get_total_sum_from_cart()
        )

        assert total_sum > Decimal("0"), "Сумма корзины не больше нуля"
        assert total_sum == mini_cart_sum, (
            f"Сумма корзины {total_sum} "
            f"не совпадает с мини-корзиной {mini_cart_sum}"
        )


@allure.severity("Critical")
@allure.epic("UI")
@allure.title("Удаление единственного товара из корзины")
def test_cart_is_empty(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.add_product()
    main_page.go_to_cart()

    cart_page = CartPage(browser)

    with allure.step("Убедиться, что перед удалением корзина не пустая"):
        initial_sum = CartPage.parse_price(
            cart_page.get_total_sum_from_cart()
        )
        assert initial_sum > Decimal("0"), "Корзина уже пустая"

    cart_page.delete_goods_from_cart()

    with allure.step("Проверить нулевую сумму после удаления"):
        total_sum = CartPage.parse_price(
            cart_page.get_total_sum_from_cart()
        )
        assert total_sum == Decimal("0"), "Сумма корзины не равна нулю"