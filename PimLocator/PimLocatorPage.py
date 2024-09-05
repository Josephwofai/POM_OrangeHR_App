from selenium.webdriver.common.by import By


class PimLocatorPage:
    Pim_Module = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6")
    Click_Configuration = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span")
    Click_Employee_list = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
    Click_Add_Employee = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a")
    Click_Reports = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a")
