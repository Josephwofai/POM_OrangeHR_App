import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MyInforModuleLocator.MyInforModuleLocatorPage import MyInforModuleLocatorPage


class MyInforModuleActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_my_info_module(self):
        click_my_info_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_My_Info_Module))
        click_my_info_module.click()

    def click_personal_details(self):
        click_personal_details = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Personal_Details))
        click_personal_details.click()

    def click_contact_details(self):
        click_contact_details = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Contact_Details))
        click_contact_details.click()

    def click_emergency_contact(self):
        click_emergency_contact = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Emergency_Contact))
        click_emergency_contact.click()

    def click_dependents(self):
        click_dependents = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Dependents))
        click_dependents.click()

    def click_immigration(self):
        click_immigration = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Immigration))
        click_immigration.click()

    def click_job(self):
        click_job = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Job))
        click_job.click()

    def click_salary(self):
        click_salary = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Salary))
        click_salary.click()

    def click_report_to(self):
        click_report_to = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Report_To))
        click_report_to.click()

    def click_qualification(self):
        click_qualification = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Qualification))
        click_qualification.click()

    def click_membership(self):
        click_membership = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MyInforModuleLocatorPage.Click_Membership))
        click_membership.click()
