from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LoginLocator.LoginLocatorPage import LoginLocatorPage


class LoginActionPage:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, name):
        enter_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorPage.ENTER_USERNAME))
        enter_username.send_keys(name)

    def enter_password(self, word):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorPage.ENTER_PASSWORD))
        enter_password.send_keys(word)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocatorPage.CLICK_LOGIN_BUTTON))
        click_login_button.click()
