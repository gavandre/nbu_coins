from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

from page_obects.registration_page import RegistrationPage
from sdk.constants import OperationResult
from service_utils.utilities import ServiceUtils


class LoginPage:
    email_field = (By.CSS_SELECTOR, "input[placeholder='E-Mail:']")
    password_field = (By.CSS_SELECTOR, "#password")
    register_button = (By.CSS_SELECTOR, ".btn.btn-success.bank-registration")
    login_button = (By.CSS_SELECTOR, "button[class='btn btn-default']")
    login_button_click = "button[class='btn btn-default']"
    return_button = (By.XPATH, "//div[@class='return_main_page']//*[name()='svg']")

    def __init__(self, driver):
        self.driver = driver
        self.log = ServiceUtils.get_logger()
        self.registration_page = RegistrationPage(driver)

    def input_email(self, value):
        try:
            result = self.driver.find_element(*self.email_field)
            result.send_keys(value)
            self.log.info("Email field was detected end proper data set")
            return OperationResult.SUCCESS
        except NoSuchElementException as error:
            self.log.info(f"Could not detect email field due to {error} exception")

    def input_password(self, value):
        try:
            result = self.driver.find_element(*self.password_field)
            result.send_keys(value)
            self.log.info("Password field was detected end proper data set")
        except NoSuchElementException as error:
            self.log.info(f"Could not detect password field due to {error} exception")

    def press_login_button(self):
        try:
            result = self.driver.find_element(*self.login_button)
            result.click()
            self.log.info("Login button was pressed successfully")
        except (NoSuchElementException, ElementClickInterceptedException) as error:
            self.log.info(f"Could not press login button due to {error} exception")

    def press_register_button(self):
        """
        Pressing the Register button on the login page
        :Example:

        The following example will press the register button on login page
        . code-block:: python
            login_page = LoginPage(driver)
            login_page.press_register_button()

        """
        try:
            self.click(self.login_button_click)
            self.log.info("Register button was pressed successfully")
            return OperationResult.SUCCESS
        except NoSuchElementException as error:
            self.log.info("Could not press Register button")
            return OperationResult.FAILURE

    def full_login_to_account(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.press_login_button()

    def presence_of_login_page(self):
        email = self.driver.find_element(*self.email_field)
        password = self.driver.find_element(*self.password_field)
        login_button = self.driver.find_element(*self.login_button)
        if email and password and login_button:
            return True

    def click(self, locator):
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        self.driver.execute_script("arguments[0].click();", element)