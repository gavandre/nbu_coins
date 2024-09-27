from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class RegistrationPage:
    lastname_field = (By.CSS_SELECTOR, "input[placeholder='Прізвище*']")
    name_field = (By.XPATH, "(//input)[12]")
    fathers_name_field = (By.CSS_SELECTOR, "input[placeholder='По батькові*']")
    email_field = (By.CSS_SELECTOR, "#email_address")
    receive_code_button = (By.XPATH, "(//div[@id='email-verification-link'])[1]")
    phone_number_field = (By.XPATH, "(//input[@id='telephone'])[1]")
    password_field = (By.XPATH, "(//input[@id='password'])[1]")
    confirm_password_field = (By.XPATH, "(//input[@id='confirmation'])[1]")
    toggle = (By.CSS_SELECTOR, "label[for='shoprules']")
    re_captcha = (By.XPATH, "//div[@class='g-recaptcha']")

    def __init__(self, driver):
        self.driver = driver

    def input_lastname(self, value: str):
        self.driver.find_element(*self.lastname_field).send_keys(value)

    def input_name(self, value: str):
        self.driver.find_element(*self.name_field).send_keys(value)

    def input_fathers_name(self, value: str):
        self.driver.find_element(*self.fathers_name_field).send_keys(value)

    def input_email(self, value: str):
        self.driver.find_element(*self.email_field).send_keys(value)

    def press_receive_code_button(self):
        self.driver.find_element(*self.receive_code_button).click()

    def input_phone_number(self, value: str):
        self.driver.find_element(*self.phone_number_field).send_keys(value)

    def input_password_filed(self, value: str):
        self.driver.find_element(*self.password_field).send_keys(value)

    def input_confirmed_password(self, value: str):
        self.driver.find_element(*self.confirm_password_field).send_keys(value)

    def click_on_confirmation_toggle(self):
        self.driver.find_element(*self.toggle).click()

    def click_on_recaptcha(self):
        self.driver.find_element(*self.re_captcha).click()
