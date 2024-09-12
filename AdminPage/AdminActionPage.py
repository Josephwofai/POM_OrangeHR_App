import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AdminLocator.AdminLocatorPage import AdminLocatorPage


class AdminActionPage:
    def __init__(self):
        self.driver = driver

    def click_admin_module(self):
        click_admin_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Admin_Module))
        click_admin_module.click()

    def click_user_managements(self):
        click_user_managements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_User_Managements))
        click_user_managements.click()

    def click_job(self):
        click_job = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Job))
        click_job.click()

    def click_organizations(self):
        click_organizations = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Organizations))
        click_organizations.click()

    def click_qualification(self):
        click_qualification = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Qualification))
        click_qualification.click()


    def click_nationalities(self):
        click_nationalities = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Nationalities))
        click_nationalities.click()

    def click_corporate_branding(self):
        click_corporate_branding = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Corporate_Branding))
        click_corporate_branding.click()

    def click_configuration(self):
        click_configuration = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AdminLocatorPage.Click_Configuration))
        click_configuration.click()