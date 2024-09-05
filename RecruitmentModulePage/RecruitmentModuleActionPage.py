import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from RecruitmentModuleLocator.RecruitmentModuleLocatorPage import RecruitmentModuleLocatorPage


class RecruitmentModuleActionPage:
    def __init__(self):
        self.driver = driver

    def click_recruitment_module(self):
        click_recruitment_module = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentModuleLocatorPage.Click_Recruitment_Module))
        click_recruitment_module.click()

    def click_candidates(self):
        click_candidates = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentModuleLocatorPage.Click_Candidates))
        click_candidates.click()

    def click_vacancies(self):
        click_vacancies = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RecruitmentModuleLocatorPage.Click_Vacancies))
        click_vacancies.click()
