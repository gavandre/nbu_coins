import pytest
from page_obects.home_page import HomePage


def test_0001(setup_teardown):
    driver = HomePage(driver="chrome")
    driver.click_logo_btn()
