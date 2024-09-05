import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PerformanceLocator.PerformanceLocatorPage import PerformanceLocatorPage


class PerformanceActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_performance_module(self):
        click_performance_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocatorPage.Click_Performance_Module))
        click_performance_module.click()

    def click_configure(self):
        click_configure = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocatorPage.Click_Configure))
        click_configure.click()

    def click_my_tracker(self):
        click_my_tracker = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocatorPage.Click_My_Tracker))
        click_my_tracker.click()

    def click_employee_tracker(self):
        click_employee_tracker = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PerformanceLocatorPage.Click_Employee_Tracker))
        click_employee_tracker.click()
