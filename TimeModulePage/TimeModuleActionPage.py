import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TimeModuleLocator.TimeModuleLocatorPage import TimeModuleLocatorPage


class TimeModuleActionPage:

    def __init__(self):
        self.driver = driver

    def click_time_module(self):
        click_time_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeModuleLocatorPage.Click_Time_Module))
        click_time_module.click()

    def click_timesheet(self):
        click_timesheet = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeModuleLocatorPage.Click_Timesheet))
        click_timesheet.click()

    def click_attendance(self):
        click_attendance = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeModuleLocatorPage.Click_Attendance))
        click_attendance.click()

    def click_reports(self):
        click_reports = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeModuleLocatorPage.Click_Reports))
        click_reports.click()

    def click_project_info(self):
        click_project_info = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(TimeModuleLocatorPage.Click_Project_Info))
        click_project_info.click()

