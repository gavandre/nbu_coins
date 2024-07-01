import inspect
import logging

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ServiceUtils:
    @staticmethod
    def get_logger():
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


class WebDriverManager:
    def __init__(self):
        chromedriver_autoinstaller.install()
        self.log = ServiceUtils.get_logger()

    def open_url(self, url):
        self.driver.get("https://coins.bank.gov.ua/")
        self.log.log(f"The page {url} was opened")

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        return self.driver

    def close_driver(self):
        self.driver.quit()
