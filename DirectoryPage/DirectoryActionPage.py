import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DirectoryLocator.DirectoryLocatorPage import DirectoryLocatorPage


class DirectoryActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_directory_module(self):
        click_directory_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DirectoryLocatorPage.Click_Directory_Module))
        click_directory_module.click()

    def enter_employee_name(self, name):
        enter_employee_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DirectoryLocatorPage.Enter_Employee_Name))
        enter_employee_name.send_keys(name)

    def click_reset_button(self):
        click_reset_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DirectoryLocatorPage.Click_Reset_Button))
        click_reset_button.click()