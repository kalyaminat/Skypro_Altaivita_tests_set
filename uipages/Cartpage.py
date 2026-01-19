from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Altaivita.constants import cart_url
import allure

class CartPage:
    def __init__(self, browser, url = cart_url):
        self.browser = browser
        self.url = url

    @allure.step("UI. Открыть страницу корзины")
    def open(self):
        self.browser.get(self.url)
    @allure.step("UI. Проверить сумму в корзине")
    def get_total_sum_from_cart(self):
        total_sum = self.browser.find_element(By.CSS_SELECTOR, 'span.js-total_products_amount').text
        return total_sum

    # def cart_is_not_empty(self):
    #     item = WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located((By.CSS_SELECTOR, '.basket__item')))
    #     return item
    @allure.step("UI. Удаление товара из корзины")
    def delete_goods_from_cart(self):
        delete_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.basket__delete.js-item-delete")))
        delete_button.click()
        self.browser.implicitly_wait(5)

    # def check_cart(self):
    #     try:
    #         WebDriverWait(self.browser, 4).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, '.basket__item')))
    #     except TimeoutException:
    #         return False
    #     return True



