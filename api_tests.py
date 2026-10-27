import allure
from apipages.Apipage import Apipage

base_url = "https://altaivita.ru/engine/"
s_cid = "76a701dd27b7e7511db257c6510b8302"
customer_id = ""
product_id = 710

@allure.severity("Critical")
@allure.id("API")
@allure.title("Добавление товара в корзину")
def test_add_to_cart(api):
    response_add = api.add_product_to_cart(product_id, customer_id)
    with allure.step("Проверка ключевых слов при довавлении товара в корзину"):
        assert response_add.json()["status"] == "ok", "Тест выполнен с ошибкой"
        assert response_add.json()["btn_text"] == "Добавлено", "Товар не добавлен"
        assert response_add.json()["sum_quantity"] == "1"
    with allure.step("Проверка статус-кода ответа"):
        assert response_add.status_code == 200

@allure.severity("Critical")
@allure.id("API")
@allure.title("Удаление товара из корзины")
def test_delete_from_cart(api):
    with allure.step("Подготовка: добавить товар в гостевую корзину"):
        response_add = api.add_product_to_cart(product_id, customer_id)
        assert response_add.status_code == 200
        assert response_add.json()["status"] == "ok"

    with allure.step("Удалить товар из корзины"):
        response_delete = api.delete_product_from_cart(
            product_id, customer_id
        )

    with allure.step("Проверка ответа после удаления товара"):
        assert response_delete.status_code == 200

        data = response_delete.json()
        assert data["sum_quantity"] == "0", "В корзине есть товары"
        assert data["products_amount"] == 0, "В корзине есть товары"
        assert "quantity_to_delete" in data, "В ответе нет quantity_to_delete"

def test_get_cart_info(api):
    response_check = api.get_cart_info(product_id, customer_id)

    with allure.step("Проверка ключевого слова в ответе"):
        assert (
                response_check.json()["request"]["action"]
                == "ecom_link_products_cart"
        )











