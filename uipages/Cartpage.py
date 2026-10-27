from decimal import Decimal

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import cart_url


class CartPage:
    TOTAL_SUM = (
        By.CSS_SELECTOR,
        "span.js-total_products_amount",
    )
    DELETE_BUTTON = (
        By.CSS_SELECTOR,
        "div.basket__delete.js-item-delete",
    )

    def __init__(self, browser, url=cart_url, timeout=15):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, timeout)

    @allure.step("UI. Открыть страницу корзины")
    def open(self):
        self.browser.get(self.url)

    @allure.step("UI. Получить сумму в корзине")
    def get_total_sum_from_cart(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_SUM)
        )
        return element.text.strip()

    @staticmethod
    def parse_price(text):
        normalized = (
            text.replace("₽", "")
            .replace(" ", "")
            .replace("\u00a0", "")
            .replace("\u202f", "")
            .replace(",", ".")
            .strip()
        )
        return Decimal(normalized)

    @allure.step("UI. Удалить товар из корзины")
    def delete_goods_from_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.DELETE_BUTTON)
        ).click()

        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_SUM, "0"),
            message="После удаления не появилось значение суммы с нулём",
        )

        self.wait.until(
            lambda browser: self.parse_price(
                browser.find_element(*self.TOTAL_SUM).text
            ) == Decimal("0"),
            message="Сумма корзины не стала равна нулю после удаления",
        )