from pypom import Page
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from page_obects.login_page import LoginPage
from service_utils.utilities import ServiceUtils


class HomePage(Page):
    logo_button = (By.XPATH, "//a[@aria-label='Логотип']")
    cabinet_button = (By.XPATH, "//a[@aria-label='Кабінет']//*[name()='svg']")
    basket_button = (By.XPATH, "//a[@aria-label='Кошик']//*[name()='svg']")
    wish_list_button = (By.XPATH, "//a[@aria-label='Cписок бажань']//*[name()='svg']")
    search_button = (By.XPATH, "//li[@class='small-menu-search show']")
    statistic_button = (By.XPATH, "(//*[name()='svg'][@class='styled_svg'])[5]")

    def __init__(self, driver):
        super().__init__(driver)
        self.cabinet = LoginPage(self.driver)
        self.log = ServiceUtils.get_logger()

    def click_logo_btn(self):
        try:
            result = self.driver.find_element(*self.logo_button)
            result.click()
            self.log.info("The logo button was clicked successfully")
        except NoSuchElementException as error:
            self.log.info(f"The log button wasn't clicked do to {error} exception")

    def click_cabinet_btn(self):
        try:
            result = self.driver.find_element(*self.cabinet_button)
            result.click()
            self.log.info("The cabinet icon was clicked successfully")
        except NoSuchElementException as error:
            self.log.info(f"Could not click on cabinet icon due to {error} exception")