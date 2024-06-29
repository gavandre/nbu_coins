from selenium.webdriver.common.by import By
from page_obects.login_page import LoginPage
from service_utils.utilities import ServiceUtils
from pypom import Page


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

    def click_logo_btn(self):
        return self.driver.find_element(*self.logo_button).click()

    def click_cabinet_btn(self):
        self.driver.find_element(*self.cabinet_button).click()
        #return LoginPage(self.driver)
