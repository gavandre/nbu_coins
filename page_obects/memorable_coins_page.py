from selenium.webdriver.common.by import By


class MemorableCoinsPage:
    product_item = (By.CSS_SELECTOR, ".product")

    def __init__(self, driver):
        self.driver = driver

    def coin_picker(self, coin_name: str):
        items = self.driver.find_elements(*self.product_item)
        #items.text()
        for item in items:
            item_element = item.text
            if coin_name in item_element:
                item.click()
                break
            elif coin_name not in item_element:
                continue
            else:
                break
