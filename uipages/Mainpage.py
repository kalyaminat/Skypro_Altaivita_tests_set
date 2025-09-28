from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import allure
from Altaivita.constants import main_url

class MainPage:

    def __init__(self, browser, url= main_url, timeout=10):
        self.browser = browser
        self.url = url

    @allure.step("UI. Открыть главную страницу")
    def open(self):
        self.browser.get(self.url)

    @allure.step("UI. Добавление товара")
    def add_product(self):
        self.browser.execute_script("window.scrollBy(0, 110);")
        category = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'group_tag-bg-category_1')))

        category.click()
        cart_icon = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header__basket.js-basket-wrapper')))
        button_add = WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-product-id="4131"]  div.product__add_2_0')))
        button_add.click()
    @allure.step("UI. Превью суммы в корзине на главной странице")
    def get_mini_cart_price(self):
        cart_icon = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header__basket.js-basket-wrapper')))
        mini_price = WebDriverWait(self.browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.basket-price.js-total'))).text
        return mini_price
    @allure.step("UI. Переход на страницу корзины")
    def go_to_cart(self):
        cart_icon = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header__basket.js-basket-wrapper'))).click()
        cart_link= WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[class="dropdown-go-over link-gray ga_link_to_cart"]')))
        cart_link.click()
