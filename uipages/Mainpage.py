import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import main_url


class MainPage:
    CATEGORY = (By.ID, "group_tag-bg-category_1")
    ADD_BUTTON = (
        By.CSS_SELECTOR,
        '[data-product-id="4131"] div.product__add_2_0',
    )
    CART_ICON = (
        By.CSS_SELECTOR,
        "div.header__basket.js-basket-wrapper",
    )
    MINI_CART_PRICE = (
        By.CSS_SELECTOR,
        "span.basket-price.js-total",
    )
    CART_LINK = (
        By.CSS_SELECTOR,
        'a[class="dropdown-go-over link-gray ga_link_to_cart"]',
    )

    def __init__(self, browser, url=main_url, timeout=15):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, timeout)

    @allure.step("UI. Открыть главную страницу")
    def open(self):
        self.browser.get(self.url)

    @allure.step("UI. Добавить товар и дождаться изменения суммы")
    def add_product(self):
        self.browser.execute_script("window.scrollBy(0, 110);")

        self.wait.until(
            EC.element_to_be_clickable(self.CATEGORY)
        ).click()

        previous_price = self.get_mini_cart_price()

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        ).click()

        self.wait.until(
            lambda browser: (
                browser.find_element(*self.MINI_CART_PRICE).text.strip()
                != previous_price
            ),
            message="Сумма в мини-корзине не изменилась после добавления",
        )

    @allure.step("UI. Получить сумму в мини-корзине")
    def get_mini_cart_price(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.MINI_CART_PRICE)
        )
        return element.text.strip()

    @allure.step("UI. Перейти в корзину")
    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()