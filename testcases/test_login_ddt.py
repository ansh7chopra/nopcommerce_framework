import pytest
from selenium import webdriver
from pageobjects.loginpage import login
# from testcases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time
from utilities import XLutilities
class Test_2_ddt:
    baseurl=ReadConfig.getApplicationURl()
    path=r"C:\Users\ACHOPRA\PycharmProjects\FrameWork\TestData\data_driven_test_file.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self):
        self.logger.info("****** test_2_ddt login *******")
        self.logger.info("****** verifying login_ddt  *******")
        self.driver=webdriver.Chrome()

        self.driver.get(self.baseurl)
        self.lp=login(self.driver)

        rows=XLutilities.getRowCount(self.path,'Sheet1')
        print("number of rows in excel:",rows)

        status_list=[]

        for r in range(2,rows+1):
            user=XLutilities.readData(self.path,'Sheet1',r,1)
            password=XLutilities.readData(self.path,'Sheet1',r,2)
            status = XLutilities.readData(self.path,'Sheet1', r, 3)
            self.lp.setusername(user)
            self.lp.setpassword(password)
            self.lp.clklogin()
            time.sleep(3)

            act_title = self.driver.title
            expected_title="Dashboard / nopCommerce administration"

            if act_title==expected_title:
                if status=="pass":
                    self.logger.info("TITLE IS MATCHED")
                    status_list.append("test case pass")
                    self.lp.clklogout()
                elif status=="fail":
                    self.logger.info("title is matched but status is fail")
                    status_list.append("test case fail")

            elif act_title!=expected_title:
                if status=="pass":
                    self.logger.info("TITLE Is not matched but status is passed")
                    status_list.append("test case fail")
                elif status=="fail":
                    self.logger.info("title not matched and status is fail")
                    status_list.append("test case pass")

        if "test case fail " not in status_list:
            self.logger.info("data driven testing is passed")
            self.driver.close()
            assert  True
        else:
            self.logger.info("data driven testing is failed")
            self.driver.close()
            assert False

        print(status_list)


#   ddt= DATA DRIVEN TESTING 




