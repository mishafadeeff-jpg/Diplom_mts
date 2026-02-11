import pytest
import allure
from api.client import ApiClient
from data.config import Config


@allure.feature("API Тесты")
@pytest.mark.api
class TestApiCart:
    def setup_method(self):
        self.api = ApiClient()

    @allure.story("Добавление товара")
    def test_add_item_to_cart(self):
        resp = self.api.add_to_cart(Config.PRODUCT_ID)
        assert resp.status_code == 200

    @allure.story("Просмотр корзины")
    def test_get_cart(self):
        self.api.add_to_cart(Config.PRODUCT_ID)
        assert self.api.get_cart().status_code == 200

    @allure.story("Невалидный товар")
    def test_add_invalid_item(self):
        assert self.api.add_to_cart(Config.INVALID_ID).status_code == 400

    @allure.story("Неверный метод")
    def test_method_not_allowed(self):
        resp = self.api.session.delete(f"{Config.API_URL}/cart/add")
        assert resp.status_code in [404, 405]

    @allure.story("Поиск")
    def test_search_product(self):
        assert self.api.search_product("Samsung").status_code == 200
