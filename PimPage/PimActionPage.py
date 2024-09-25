import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PimLocator.PimLocatorPage import PimLocatorPage


class PimActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_pim_module(self):
        click_pim_module = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(PimLocatorPage.Click_Pim_Module))
        click_pim_module.click()
        time.sleep(3)

    def click_configuration(self):
        click_configuration = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocatorPage.Click_Configuration))
        click_configuration.click()
        time.sleep(3)

    def click_employee_list(self):
        click_employee_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocatorPage.Click_Employee_list))
        click_employee_list.click()
        time.sleep(3)

    def click_add_employee(self):
        click_add_employee = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocatorPage.Click_Add_Employee))
        click_add_employee.click()
        time.sleep(3)

    def click_reports(self):
        click_reports = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PimLocatorPage.Click_Reports))
        click_reports.click()
        time.sleep(3)