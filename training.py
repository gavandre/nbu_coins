# from selenium import webdriver
# import chromedriver_autoinstaller
#
# chromedriver_autoinstaller.install()
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://coins.bank.gov.ua/")
from page_obects.home_page import HomePage
from page_obects.login_page import LoginPage
from page_obects.registration_page import RegistrationPage
from service_utils.utilities import WebDriverManager
from test_data.test_data import CabinetLogin

driver = WebDriverManager().get_driver()
driver.get(CabinetLogin.url)
home_page = HomePage(driver)
home_page.click_cabinet_btn()
login_page = LoginPage(driver)
login_page.press_register_button()
login_page.registration_page.input_lastname("Петренко")
login_page.registration_page.input_name("Петро")
login_page.registration_page.input_fathers_name("Петрович")
login_page.registration_page.input_email("gavandre@gmail.com")
login_page.registration_page.press_receive_code_button()
#home_page.cabinet.input_email("adfadfdfd")
#home_page.click_cabinet_btn()
driver.quit()
