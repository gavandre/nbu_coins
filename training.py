# from selenium import webdriver
# import chromedriver_autoinstaller
#
# chromedriver_autoinstaller.install()
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# driver.get("https://coins.bank.gov.ua/")
from page_obects.coin_page import CoinPage
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
#register_page = login_page.press_register_button()
#register_page = RegistrationPage(driver)
#register_page.click_on_recaptcha()
login_page = LoginPage(driver)
login_page.input_email(CabinetLogin.email_o)
login_page.input_password(CabinetLogin.password_o)
login_page.press_login_button()
home_page.click_memorable_coins_tub()
home_page.memorable_coins_page.coin_picker('"Черепаха"')   #Крапля життя , '"Черепаха"', 'Орьнек'
# coin_page = CoinPage(driver)
#coin_page.click_on_buy_button()
# login_page.press_register_button()
# login_page.registration_page.input_lastname("Петренко")
# login_page.registration_page.input_name("Петро")
# login_page.registration_page.input_fathers_name("Петрович")
# login_page.registration_page.input_email("gavandre@gmail.com")
#login_page.registration_page.press_receive_code_button()
#home_page.cabinet.input_email("adfadfdfd")
#home_page.click_cabinet_btn()
driver.quit()
