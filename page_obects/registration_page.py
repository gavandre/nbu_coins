from selenium.webdriver.common.by import By


class RegistrationPage:
    lastname_field = (By.CSS_SELECTOR, "input[placeholder='Прізвище*']")

    def __init__(self, driver):
        self.driver = driver

    def input_lastname(self, value):
        self.driver.find_element(*self.lastname_field).send_keys(value)
