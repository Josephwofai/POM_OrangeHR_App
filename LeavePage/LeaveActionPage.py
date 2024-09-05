import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LeaveLocator.LeaveLocatorPage import LeaveLocatorPage


class LeaveActionPage:
    def __init__(self):
        self.driver = driver

    def leave_module(self):
        leave_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Leave_Module))
        leave_module.click()

    def click_apply(self):
        click_apply = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Apply))
        click_apply.click()

    def click_my_leave(self):
        click_my_leave = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_My_Leave))
        click_my_leave.click()

    def click_entitlement(self):
        click_entitlement = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Entitlement))
        click_entitlement.click()

    def click_reports(self):
        click_reports = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Reports))
        click_reports.click()

    def click_configure(self):
        click_configure = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Configure))
        click_configure.click()

    def click_leave_list(self):
        click_leave_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Leave_List))
        click_leave_list.click()

    def click_assign_leave(self):
        click_assign_leave = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LeaveLocatorPage.Click_Assign_Leave))
        click_assign_leave.click()
