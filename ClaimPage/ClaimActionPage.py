import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ClaimLocator.ClaimLocatorPage import ClaimLocatorPage


class ClaimActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_claim(self):
        click_claim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_Claim))
        click_claim.click()

    def click_configure(self):
        click_configure = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_Configure))
        click_configure.click()

    def click_submit_claim(self):
        click_submit_claim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_Submit_Claim))
        click_submit_claim.click()

    def click_my_claim(self):
        click_my_claim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_My_Claim))
        click_my_claim.click()

    def click_employee_claim(self):
        click_employee_claim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_Employee_Claim))
        click_employee_claim.click()

    def click_assign_claim(self):
        click_assign_claim = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClaimLocatorPage.Click_Assign_Claim))
        click_assign_claim.click()



    Click_My_Claim = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a")
    Click_Employee_Claim = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a")
    Click_Assign_Claim = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a")
