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
login_page.input_email(CabinetLogin.email)
login_page.input_password(CabinetLogin.password)
login_page.press_login_button()

#home_page.cabinet.input_email("adfadfdfd")
#home_page.click_cabinet_btn()
driver.quit()
