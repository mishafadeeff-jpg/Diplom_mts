import requests
from data.config import Config
from requests import Response


class ApiClient:
    def __init__(self):
        self.base_url = Config.API_URL
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0", "Accept": "application/json"})

    def get_cart(self) -> Response:
        return self.session.get(f"{self.base_url}/cart")

    def add_to_cart(self, product_id: str) -> Response:
        return self.session.post(f"{self.base_url}/cart/add", json={"id": product_id})

    def search_product(self, text: str) -> Response:
        return self.session.get(f"{Config.BASE_URL}/search/results", params={"q": text})
