import pytest
import allure
from selenium import webdriver

# @pytest.fixture
# def browser():
#     with allure.step("Открыть и настроить браузер"):
#         browser = webdriver.Chrome()
#         browser.implicitly_wait(4)
#         browser.maximize_window()
#         yield browser
#     with allure.step("Закрыть браузер"):
#         browser.quit()

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()