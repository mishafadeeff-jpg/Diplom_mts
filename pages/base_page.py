from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://shop.mts.ru"

    def open(self, url: str = None) -> None:
        self.driver.get(url if url else self.base_url)

    def find(self, locator: tuple, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple, timeout: int = 10) -> None:
        self.find(locator, timeout).click()
