import pytest
from selenium import webdriver
from pageobjects.loginpage import login
# from testcases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_1:
    baseurl=ReadConfig.getApplicationURl()
    username= ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homepagetitle(self):
        self.logger.debug("****** test_1 login *******")
        self.logger.info("****** verifying home page title *******")
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseurl)
        actual_title=self.driver.title
        if actual_title=="Your store. Login":
            assert True
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\test_homepage.png')          # < running >
            self.logger.info("****** home page title is passed *******")
            self.driver.close()
        else:
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\test_homepage.png')
            self.driver.close()
            assert False
            self.logger.error("****** home page title is failed *******")


    @pytest.mark.regression
    def test_login(self):
        self.logger.debug("****** test_2 login click *******")
        self.driver=webdriver.Chrome()
        # self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clklogin()
        act_title = self.driver.title
        self.logger.info("****** verifying login page title *******")
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\test_loginpage.png')
            self.logger.info("****** login page title is passed *******")
            self.driver.close()
        else:
            self.driver.save_screenshot(r'C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots\test_loginpage.png')
            assert False
            self.logger.info("****** login page title is failed *******")
            self.driver.close()


# C:\Users\ACHOPRA\PycharmProjects\FrameWork\screenshots
