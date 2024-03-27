import pytest
import time
import datetime
from selenium import webdriver
from pageobjects.loginpage import login
from pageobjects.addCustomer import xpaths
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_3:
    baseurl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("****** verifying home page login *******")
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clklogin()
        time.sleep(1)
        self.logger.info("****** login successfull *******")
        self.ac=xpaths(self.driver)
        self.logger.info("****** adding new customer data *******")
        self.ac.clkcustomer_menu()
        time.sleep(1)
        self.ac.clkcustomer_menu_item()
        time.sleep(1)
        self.ac.clkadd_new_btn()
        time.sleep(1)
        self.timestamp=timestamp_email()
        self.ac.setemail(self.timestamp)
        self.ac.setpassword("ansh@123")
        self.ac.setfirstname("ansh")
        self.ac.setlastname("chopra")
        self.ac.setgender("Male")
        time.sleep(1)
        self.ac.setdob("8 / 7 / 2002")                   # format  mm/dd/yyyy
        self.ac.setcompanyname("capgemini")
        # self.ac.clkcustomer_role("Guests")
        # time.sleep(2)
        self.ac.setvendor("1")
        time.sleep(1)
        self.ac.clksavebtn()
        time.sleep(2)
        self.logger.info("****** new customer details added *******")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully."in self.msg:
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\customerAdd.png')
            self.logger.info("****** add customer test passed with screenshot *******")
            assert True
        else:
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\customerNOTAdd.png')
            self.logger.info("****** add customer test failed  *******")
            assert False



def timestamp_email():
    current_time = datetime.datetime.now()

    timestamp = current_time.strftime("%Y_%m_%d_%H_%M_%S")

    return "ansh"+timestamp+"@gmail.com"

# https://admin-demo.nopcommerce.com/Admin/Customer/List
