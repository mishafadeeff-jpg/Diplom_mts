import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from data.config import Config

@pytest.fixture(scope="function")
def driver():
    print("\nЗапуск браузера...")
    options = Options()
    if Config.IS_HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    yield driver

    print("\nЗакрытие браузера...")
    driver.quit()
