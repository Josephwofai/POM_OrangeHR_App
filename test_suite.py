import pytest
from selenium import webdriver
from LoginPage.LoginActionPage import LoginActionPage
from AdminLocator.AdminLocatorPage import AdminLocatorPage
from PimLocator.PimLocatorPage import PimLocatorPage
from LeaveLocator.LeaveLocatorPage import LeaveLocatorPage
from TimeModuleLocator.TimeModuleLocatorPage import TimeModuleLocatorPage
from RecruitmentModuleLocator.RecruitmentModuleLocatorPage import RecruitmentModuleLocatorPage
from MyInforModuleLocator.MyInforModuleLocatorPage import MyInforModuleLocatorPage
from PerformanceLocator.PerformanceLocatorPage import PerformanceLocatorPage
from DashBoardLocator.DashBoardLocatorPage import DashBoardLocatorPage
from DirectoryLocator.DirectoryLocatorPage import DirectoryLocatorPage
from MaintenanceLocator.MaintenanceLocatorPage import MaintenanceLocatorPage
from ClaimLocator.ClaimLocatorPage import ClaimLocatorPage
from BuzzLocator.BuzzLocatorPage import BuzzLocatorPage
from LogoutLocator.LogoutLocatorPage import LogoutLocatorPage


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


# Verify URl launch
@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginActionPage(driver)
    login_page.login_url("https://opensource-demo.orangehrmlive.com/")
    return login_page


# Verify login_page
def test_login_page_orange_hrm_website(login):
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login_button()

def test_admin_page_orange_hrm_website(login):
    test_admin_page = AdminPage(login.driver)
    test_admin_page.click_admin_module()
    test_admin_page.click_user_management()
    test_admin_page.click_job()
    test_admin_page.click_organizations()
    test_admin_page.click_qualification()
    test_admin_page.click_nationalities()
    test_admin_page.click_corporate_branding()

def test_pim_page_orange_hrm_website(login):
    test_pim_page = PimPage(login.driver)
    test_pim_page.pim_module()
    test_pim_page.click_configuration()
    test_pim_page.click_employee_list()
    test_pim_page.click_reports()

def test_leave_page_orange_hrm_website(login):
    test_leave_page = LeavePage(login.driver)
    test_leave_page.click_leave_module()
    test_leave_page.click_pply()
    test_leave_page.click_my_leave()
    test_leave_page.click_entitlement()
    test_leave_page.click_reports()
    test_leave_page.click_configure()
    test_leave_page.click_leave_list()
    test_leave_page.click_assign_leave()

def test_time_page_orange_hrm_website(login):
    test_time_page = TimeModulePage(login.driver)
    test_time_page.sh

