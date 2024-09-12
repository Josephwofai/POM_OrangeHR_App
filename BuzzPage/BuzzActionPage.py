import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BuzzLocator.BuzzLocatorPage import BuzzLocatorPage


class BuzzActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_buzz(self):
        click_buzz = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(BuzzLocatorPage.click_Buzz))
        click_buzz.click()
