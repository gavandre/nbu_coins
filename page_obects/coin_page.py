from selenium.webdriver.common.by import By


class CoinPage:
    buy_button = (By.CSS_SELECTOR, "button[class='btn-primary buy']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_buy_button(self):
        self.driver.find_element(*self.buy_button).click()
