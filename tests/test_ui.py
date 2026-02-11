import pytest
import allure
from pages.main_page import MainPage


@allure.feature("UI Тесты")
@pytest.mark.ui
class TestUI:
    @allure.story("Поиск")
    def test_search_samsung(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.search_for("Samsung")
        assert "Samsung" in driver.title or "Samsung" in driver.current_url

    @allure.story("Заголовок")
    def test_main_page_title(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        assert "МТС" in page.get_page_title() or "MTS" in page.get_page_title()

    @allure.story("Негативный поиск")
    def test_search_gibberish(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.search_for("абракадабра123")
        assert driver.title

    @allure.story("Корзина")
    def test_open_cart(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.open("https://shop.mts.ru/cart")
        assert "cart" in driver.current_url

    @allure.story("Каталог")
    def test_catalog_url(self, driver):
        page = MainPage(driver)
        page.open("https://shop.mts.ru/catalog/smartfony")
        assert "smartfony" in driver.current_url
