from selenium.webdriver.common.by import By


class LoginPage:

    email_field = (By.CSS_SELECTOR, "input[placeholder='E-Mail:']")
    password_field = (By.CSS_SELECTOR, "#password")
    register_button = (By.CSS_SELECTOR, ".btn.btn-success.bank-registration")
    login_button = (By.CSS_SELECTOR, "button[class='btn btn-default']")
    return_button = (By.XPATH, "//div[@class='return_main_page']//*[name()='svg']")

    def __init__(self, driver):
        self.driver = driver

    def input_email(self, value):
        self.driver.find_element(*self.email_field).send_keys(value)

    def input_password(self, value):
        self.driver.find_element(*self.password_field).send_keys(value)

    def press_login(self):
        self.driver.find_element(*self.login_button).click()
