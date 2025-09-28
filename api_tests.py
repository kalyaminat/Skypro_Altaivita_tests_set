from .constants import *
import allure
import json
import pytest
from .apipages.Apipage import Apipage
base_url = "https://altaivita.ru/engine/"
s_cid = "76a701dd27b7e7511db257c6510b8302"
customer_id = 372502
product_id = 710

@allure.severity("Critical")
@allure.id("API")
@allure.title("Добавление товара в корзину")
def test_add_to_cart():
    api = Apipage(base_url, s_cid)
    response_add = api.add_product_to_cart(product_id, customer_id)
    with allure.step("Проверка ключевых слов при довавлении товара в корзину"):
        assert response_add.json()["status"] == "ok", "Тест выполнен с ошибкой"
        assert response_add.json()["btn_text"] == "Добавлено", "Товар не добавлен"
        assert response_add.json()["sum_quantity"] == "1"
    with allure.step("Проверка статус-кода ответа"):
        assert response_add.status_code == 200
# def test_check_cart():
#     api = Apipage(base_url, s_cid)
#     response_check = api.get_cart_info(product_id, customer_id)
#     with allure.step("Проверка корзины после добавления"):
#         assert response_check.json()["position"] == '1'
@allure.severity("Critical")
@allure.id("API")
@allure.title("Удаление товара из корзины")
def test_delete_from_cart():
    api = Apipage(base_url, s_cid)
    response_delete = api.delete_product_from_cart(product_id, customer_id)

    with allure.step("Проверка ключевых слов после удаления товара"):
        assert response_delete.json()["sum_quantity"] == '0', "В корзине есть товары"
        assert response_delete.json()["products_amount"] == 0, "В корзине есть товары"
        assert "quantity_to_delete" in response_delete.json(), "Данного текста в ответе нет"

@allure.severity("Critical")
@allure.id("API")
@allure.title("Проверка корзины после удаления")
def test_check_cart_after_delete():
    api = Apipage(base_url, s_cid)
    response_check = api.get_cart_info(product_id, customer_id)

    with allure.step("Проверка ключеввого слова в ответе"):
        assert response_check.json()["request"]["action"] == "ecom_link_products_cart"









