from selenium.webdriver.common.by import By


class RegistrationPage:
    lastname_field = (By.CSS_SELECTOR, "input[placeholder='Прізвище*']")
    name_field = (By.XPATH, "(//input)[12]")
    fathers_name_field = (By.CSS_SELECTOR, "input[placeholder='По батькові*']")
    email_field = (By.CSS_SELECTOR, "#email_address")
    receive_code_button = (By.XPATH, "(//div[@id='email-verification-link'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def input_lastname(self, value):
        self.driver.find_element(*self.lastname_field).send_keys(value)

    def input_name(self, value):
        self.driver.find_element(*self.name_field).send_keys(value)

    def input_fathers_name(self, value):
        self.driver.find_element(*self.fathers_name_field).send_keys(value)

    def input_email(self, value):
        self.driver.find_element(*self.email_field).send_keys(value)

    def press_receive_code_button(self):
        self.driver.find_element(*self.receive_code_button).click()
