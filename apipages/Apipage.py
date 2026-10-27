import requests
import allure


class Apipage:
    def __init__(
        self,
        base_url: str,
        s_cid: str,
        session: requests.Session,
    ):
        self.base_url = base_url
        self.s_cid = s_cid
        self.session = session

    @allure.step("API. Добавление товара в корзину")
    def add_product_to_cart(self, product_id: int, customer_id: int) -> requests.Response:
        data = {
            "product_id": product_id,
            "LANG_key": "ru",
            "S_wh": 1,
            "S_CID": self.s_cid,
            "S_cur_code": "rub",
            "S_koef": 1,
            "quantity": 1,
            "S_customerID": customer_id,
        }


        response = self.session.post(
            self.base_url + "cart/add_products_to_cart_from_preview.php",
            data=data,
            timeout=(10, 20),
        )
        return response

    @allure.step("API. Удаление товара из корзины")
    def delete_product_from_cart(self, product_id: int, customer_id: int) -> requests.Response:

        data = {
            "quantity_to_delete": "1",
            "product_id": product_id,
            "LANG_key": "ru",
            "S_wh": 1,
            "S_CID": self.s_cid,
            "S_cur_code": "rub",
            "S_koef": 1,
            "S_customerID": customer_id,
        }


        response = self.session.post(
            self.base_url + "cart/delete_products_from_cart_preview.php",
            data=data,
            timeout=(10, 20),
        )
        return response

    @allure.step("API. Проверка корзины после удаления")
    def get_cart_info(self, product_id: int, customer_id: int) -> requests.Response:
        data = {
            "action": "ecom_link_products_cart",
            "productID": product_id,
            "LANG_key": "ru",
            "S_wh": 1,
            "S_CID": self.s_cid,
            "S_cur_code": "rub",
            "S_koef": 1,
            "S_customerID": customer_id,
        }


        response = self.session.post(
            self.base_url + "ajax/ajax_ecommerce/ajax_ecommerce.php",
            data=data,
            timeout=(10, 20),
        )
        return response


