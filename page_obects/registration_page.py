from pypom import Page
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from service_utils.utilities import ServiceUtils


class RegistrationPage(Page):
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
        self.log = ServiceUtils.get_logger()
        #super().__init__()

    def input_lastname(self, value: str) -> None:
        """
        Method inputs the user's lastname
        :param value: The last name
        :return: None
        """
        try:
            self.driver.find_element(*self.lastname_field).send_keys(value)
            self.log.info("RegistrationPage: The lastname was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The lastname field doesn't exist")

    def input_name(self, value: str) -> None:
        """
        Method inputs the users name
        :param value: The first name
        :return: None
        """
        try:
            self.driver.find_element(*self.name_field).send_keys(value)
            self.log.info("RegistrationPage: The first was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The first name field doesn't exist")

    def input_fathers_name(self, value: str) -> None:
        """
        Method inputs the fathers name
        :param value: The fathers name
        :return: None
        """
        try:
            self.driver.find_element(*self.fathers_name_field).send_keys(value)
            self.log.info("RegistrationPage: The fathers name was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The fathers name field doesn't exist")

    def input_email(self, value: str) -> None:
        """
        Method inputs the email address
        :param value: The Email address
        :return: None
        """
        try:
            self.driver.find_element(*self.email_field).send_keys(value)
            self.log.info("RegistrationPage: The email was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The email field doesn't exist")

    def press_receive_code_button(self) -> None:
        """
        This method clicks on the "Receive code button"
        :return: None
        """
        try:
            self.driver.find_element(*self.receive_code_button).click()
            self.log.info("RegistrationPage: The 'Receive button' was pressed successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The 'Receive button' doesn't exist")

    def input_phone_number(self, value: str) -> None:
        """
        This method inputs the phone number
        :param value: The phone number
        :return: None
        """
        try:
            self.driver.find_element(*self.phone_number_field).send_keys(value)
            self.log.info("RegistrationPage: The phone number was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The phone number field doesn't exist")

    def input_password_filed(self, value: str) -> None:
        """
        This method inputs the users password
        :param value: The password
        :return: None
        """
        try:
            self.driver.find_element(*self.password_field).send_keys(value)
            self.log.info("RegistrationPage: The password was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The password field doesn't exist")

    def input_confirmed_password(self, value: str) -> None:
        """
        This method inputs the password once more for confirmation
        :param value: The password
        :return:
        """
        try:
            self.driver.find_element(*self.confirm_password_field).send_keys(value)
            self.log.info("RegistrationPage: The password confirmation was inputted successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The password confirmation field ")

    def click_on_confirmation_toggle(self) -> None:
        """
        THis method clicks on the confirmation toggle
        :return: None
        """
        try:
            self.driver.find_element(*self.toggle).click()
            self.log.info("RegistrationPage: The confirmation toggle was turned on successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The confirmation toggle doesn't exist")

    def click_on_recaptcha(self) -> None:
        """
        This method clicks on the recaptcha button
        :return: None
        """
        try:
            self.driver.find_element(*self.re_captcha).click()
            self.log.info("RegistrationPage: The recaptcha was clicked successfully")
        except NoSuchElementException:
            self.log.info("RegistrationPage: The recaptcha doesn't exist")
