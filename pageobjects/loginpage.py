from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class login:
    # logout_btn="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,"Email").clear()
        self.driver.find_element(By.ID,"Email").send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys(password)
    def clklogin(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(1)

    def clklogout(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
        time.sleep(1)
