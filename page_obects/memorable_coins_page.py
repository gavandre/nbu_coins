import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_obects.login_page import LoginPage
from service_utils.utilities import ServiceUtils
from test_data.test_data import TextMessages, CabinetLogin


class MemorableCoinsPage:
    product_item = (By.XPATH, "//div[@class='col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-6 col_product "
                              "col_product_bank']")
    child_text_item = ".//div/div/div/a"  # child element (the name of coin) of product item_element
    child_bucket_icon_item = ".//div/div/div[3]/span"  # child element (the bucket icon) of product item_element
    picked_item = "//div[@class='col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-6 col_product col_product_bank']"
    bucket_popup_window = "//div[@class='modal-body']"

    def __init__(self, driver):
        self.driver = driver
        self.log = ServiceUtils.get_logger()

    def coin_picker(self, coin_name: str):
        global icon_button
        login_page = LoginPage(self.driver)
        try:
            brake_1_loop = False
            while True:
                items = self.driver.find_elements(*self.product_item)
                self.log.info("The list of elements was detected successfully")
                locator_index = 1
                brake_2_loop = False
                while True:
                    for item in items:
                        try:
                            item_element = item.find_element(By.XPATH, self.child_text_item).text
                            if coin_name in item_element:
                                product_item = self.driver.find_element(By.XPATH,
                                                                        self.picked_item + f"[{locator_index}]")
                                hover = ActionChains(self.driver).move_to_element(product_item)
                                hover.perform()
                                self.log.info("The desired element was hovered successfully")
                                try:
                                    icon_button = item.find_element(By.XPATH, self.child_bucket_icon_item)
                                except (NoSuchElementException, StaleElementReferenceException) as error:
                                    self.log.info(f"The basket button could not be detected due to {error}")
                                    pass
                                if icon_button.get_attribute('title'):
                                    self.driver.refresh()
                                    self.log.info("Page was refreshed")
                                    brake_2_loop = True
                                    break
                                else:
                                    self.click(self.child_bucket_icon_item)
                                    self.log.info("The basket button was pressed successfully")
                                    try:
                                        wait = WebDriverWait(self.driver, 600)
                                        wait.until(EC.visibility_of_element_located((By.XPATH, self.bucket_popup_window)))
                                        time.sleep(30)
                                    except NoSuchElementException as error:
                                        self.log.info(f"Could not find element du to {error}")
                                    # проробити сценарій коли юзера викидає при спробі клікнути на кнопку купити
                                    try:
                                        if login_page.presence_of_login_page():
                                            self.log.info("The login page detected")
                                            login_page.full_login_to_account(CabinetLogin.email_o, CabinetLogin.password_o)
                                            self.log.info("The user logged successfully")
                                            brake_2_loop = False
                                            break
                                    except NoSuchElementException:
                                        brake_2_loop = True
                                        self.log.info("User remains on the Memorable coins page")
                                        break
                            elif coin_name not in item_element:
                                locator_index += 1
                                continue
                        except (NoSuchElementException, StaleElementReferenceException) as error:
                            self.log.info(
                                f"Could not detect the {coin_name} in child web object due to {error} exception")
                            brake_2_loop = True
                            pass
                    if brake_2_loop:
                        brake_1_loop = True
                        break
                if brake_1_loop:
                    break
        except NoSuchElementException as error:
            self.log.info(f"Could not detect the list of elements due to {error}")
            pass

    def click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)
