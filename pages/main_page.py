from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure
import time


class MainPage(BasePage):
    SEARCH_INPUT = (By.NAME, "q")

    @allure.step("Открыть главную страницу")
    def open_main_page(self) -> None:
        self.open(self.base_url)
        time.sleep(3)

    @allure.step("Поиск товара: {text}")
    def search_for(self, text: str) -> None:
        try:
            box = self.find(self.SEARCH_INPUT)
            box.click()
            box.clear()
            box.send_keys(text)
            time.sleep(1)
            box.send_keys(Keys.ENTER)
            time.sleep(3)
        except Exception:
            pass

        if "search" not in self.driver.current_url:
            with allure.step("План Б: Прямой переход"):
                self.driver.get(f"{self.base_url}/search/results?q={text}")
                time.sleep(4)

    @allure.step("Получить заголовок")
    def get_page_title(self) -> str:
        return self.driver.title
