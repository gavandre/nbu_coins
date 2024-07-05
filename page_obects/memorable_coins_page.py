from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from service_utils.utilities import ServiceUtils


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
        try:
            items = self.driver.find_elements(*self.product_item)
            self.log.info("The list of elements was detected successfully")
            locator_index = 1
            for item in items:
                try:
                    item_element = item.find_element(By.XPATH, self.child_text_item).text
                    if coin_name in item_element:
                        product_item = self.driver.find_element(By.XPATH, self.picked_item + f"[{locator_index}]")
                        hover = ActionChains(self.driver).move_to_element(product_item)
                        hover.perform()
                        icon_button = item.find_element(By.XPATH, self.child_bucket_icon_item)
                        while True:
                            if icon_button.is_enabled():
                                icon_button.click()
                            else:
                                continue
                        break
                    elif coin_name not in item_element:
                        locator_index += 1
                        continue
                    else:
                        break
                except NoSuchElementException as error:
                    self.log.info(f"Could not detect the {coin_name} in child web object due to {error} exception")
        except NoSuchElementException as error:
            self.log.info(f"Could not detect the list of elements due to {error}")
