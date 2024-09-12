import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LogoutLocator.LogoutLocatorPage import LogoutLocatorPage


class LogoutActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_drop_down(self):
        click_drop_down = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocatorPage.click_Drop_down))
        click_drop_down.click()

    def click_log_out(self):
        click_log_out = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogoutLocatorPage.click_Log_out))
        click_log_out.click()


        