import time

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_obects.login_page import LoginPage
from service_utils.utilities import ServiceUtils
from test_data.test_data import TextMessages, CabinetLogin


class MemorableCoinsPage:
    product_item = (By.XPATH, "//div[@class='col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-6 col_product "
                              "col_product_bank']")
    child_text_item = ".//div/div/div/a"  # child element (the name of coin) of product item_element
    child_bucket_icon_item = ".//div/div/div[3]/span"  # child element (the bucket icon) of product item_element
    picked_item = "//div[@class='col-xl-4 col-lg-4 col-md-4 col-sm-6 col-xs-6 col_product col_product_bank']"

    def __init__(self, driver):
        self.driver = driver
        self.log = ServiceUtils.get_logger()

    def coin_picker(self, coin_name: str):
        global icon_button
        login_page = LoginPage(self.driver)
        try:
            #brake_1_loop = False
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
                                try:
                                    icon_button = item.find_element(By.XPATH, self.child_bucket_icon_item)
                                except (NoSuchElementException, StaleElementReferenceException):
                                    pass
                                if icon_button.get_attribute('title'):
                                    self.driver.refresh()
                                    brake_2_loop = True
                                    break
                                else:
                                    self.click(self.child_bucket_icon_item)
                                    # проробити сценарій коли юзера викидає при спробі клікнути на кнопку купити
                                    try:
                                        if login_page.presence_of_login_page():
                                            login_page.full_login_to_account(CabinetLogin.email, CabinetLogin.password)
                                        else:
                                            brake_2_loop = True
                                            break
                                    except NoSuchElementException:
                                        pass
                            elif coin_name not in item_element:
                                locator_index += 1
                                continue
                        except (NoSuchElementException, StaleElementReferenceException) as error:
                            self.log.info(
                                f"Could not detect the {coin_name} in child web object due to {error} exception")
                            brake_2_loop = True
                            pass
                    if brake_2_loop:
                        #brake_1_loop = True
                        break
                #if brake_1_loop:
                #break
        except NoSuchElementException as error:
            self.log.info(f"Could not detect the list of elements due to {error}")
            pass

    def click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)
