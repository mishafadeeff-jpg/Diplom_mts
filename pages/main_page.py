import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")

    @allure.step("Отрыть главную страницу")
    def open_main_page(self) -> None:
        self.open(self.base_url)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        self._close_cookie_popup()

    @allure.step("Закрытие всплывающего окна")
    def _close_cookie_popup(self):
        """Закрывает куки или выбор города, если они перекрывают экран"""
        try:
            button = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "//button[contains(text(), 'Принять') or contains(text(), 'Хорошо')"
                                            " or contains(@class, 'cookie')]"))
            )
            button.click()
        except Exception:
            pass

    @allure.step("Поиск товара: {text}")
    def search_for(self, text: str) -> None:
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        search_box.click()
        search_box.clear()
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)

        try:
            WebDriverWait(self.driver, 5).until(
                lambda driver: "search" in driver.current_url
            )
        except Exception:
            with allure.step("Enter не сработал, переходим по прямой ссылке"):
                self.driver.get(f"{self.base_url}/search?q={text}")

    @allure.step("Получить заголовок")
    def get_page_title(self) -> str:
        return self.driver.title
