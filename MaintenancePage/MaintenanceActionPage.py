import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MaintenanceLocator.MaintenanceLocatorPage import MaintenanceLocatorPage


class MaintenanceActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_maintenance(self):
        click_maintenance = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocatorPage.Click_Maintenance))
        click_maintenance.click()

    def click_password(self, password):
        click_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocatorPage.Click_Password))
        click_password.send_keys(password)

    def click_confirm(self):
        click_confirm = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocatorPage.Click_Confirm))
        click_confirm.click()

    def click_cancel(self):
        click_cancel = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MaintenanceLocatorPage.Click_Confirm))
        click_cancel.click()