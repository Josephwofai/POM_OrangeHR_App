from selenium.webdriver.common.by import By


class PimLocatorPage:
    Click_Pim_Module = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
    Click_Configuration = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span")
    Click_Employee_list = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
    Click_Add_Employee = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a")
    Click_Reports = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a")
