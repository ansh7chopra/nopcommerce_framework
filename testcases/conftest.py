# from selenium import webdriver
# import pytest
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture(scope='class')
# def setup(request):
#     driver=webdriver.chrome()
#     request.cls.driver=driver
#     yield
#     driver.close()


def metadata_report(config):
    config.metadata['project name']='nop commerce'
    config.metadata['module name']='customers'
    config.metadata['tester name']='ansh'

 #  this is the flag to run to generate html report

 # pytest --html=reports\report.html testcases/test_login.py
