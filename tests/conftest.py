from selenium import webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest


@pytest.fixture()
def setup_teardown(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        geckodriver_autoinstaller.install()
        driver = webdriver.Firefox()
    driver.implicitly_wait(8)
    driver.maximize_window()
    driver.get("https://coins.bank.gov.ua/")
    request.cls.driver = driver
    yield driver
    driver.quit()
