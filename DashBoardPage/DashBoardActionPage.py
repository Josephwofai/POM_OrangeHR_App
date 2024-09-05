import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DashBoardLocator.DashBoardLocatorPage import DashBoardLocatorPage


class DashBoardActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_dash_board(self):
        click_dash_board = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Dash_Board))
        click_dash_board.click()

    def click_john_doe(self):
        click_john_doe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_John_Doe))
        click_john_doe.click()

    def click_about(self):
        click_about = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Close_About))
        click_about.click()

    def click_john(self):
        click_john = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_John))
        click_john.click()

    def click_support(self):
        click_support = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Support))
        click_support.click()

    def click_doe(self):
        click_doe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Doe))
        click_doe.click()

    def click_change_password(self):
        click_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Password))
        click_password.click()

    def click_cancel(self):
        click_cancel = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(DashBoardLocatorPage.Click_Cancel))
        click_cancel.click()
