import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class xpaths:
    customer_menu="//a[@href='#']//p[contains(text(),'Customers')]"
    customer_menu_item="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_btn="//a[@class='btn btn-primary']"

    Email="//input[@id='Email']"
    Password="//input[@id='Password']"
    First_name="//input[@id='FirstName']"
    Last_name="//input[@id='LastName']"
    Gender_male="//input[@id='Gender_Male']"
    Gender_female="//input[@id='Gender_Female']"
    dob_xpath="//input[@id='DateOfBirth']"
    company_name="//input[@id='Company']"

    customer_role="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    customer_role_item1="// span[normalize - space() = 'Administrators']"
    customer_role_item2="// span[normalize - space() = 'Forum Moderators']"
    customer_role_item3="// span[normalize - space() = 'Guests']"
    customer_role_item4="// span[normalize - space() = 'Registered']"
    customer_role_item5="// span[normalize - space() = 'Vendors']"

    vendorbox="//select[@id='VendorId']"
    textarea="//textarea[@id='AdminComment']"
    savebtn="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clkcustomer_menu(self):
        self.driver.find_element(By.XPATH,self.customer_menu).click()

    def clkcustomer_menu_item(self):
        self.driver.find_element(By.XPATH,self.customer_menu_item).click()

    def clkadd_new_btn(self):
        self.driver.find_element(By.XPATH,self.add_new_btn).click()

    def setemail(self,mail):
        self.driver.find_element(By.XPATH,self.Email).send_keys(mail)

    def setpassword(self,pas):
        self.driver.find_element(By.XPATH,self.Password).send_keys(pas)

    def setfirstname(self,fname):
        self.driver.find_element(By.XPATH,self.First_name).send_keys(fname)

    def setlastname(self,lname):
        self.driver.find_element(By.XPATH,self.Last_name).send_keys(lname)

    def clkcustomer_role(self,role):
        c_role=self.driver.find_element(By.XPATH,self.customer_role).click()
        self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item4).click()
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item1).click()
        elif role=='Guests':
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item3).click()
        elif role=='vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item5).click()
        elif role=='Forum moderators':
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item2).click()
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.customer_role_item4).click()

    def setvendor(self,value):
        find=self.driver.find_element(By.XPATH,self.vendorbox)
        drop=Select(find)
        drop.select_by_index(value)

    def setgender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.Gender_male).click()
        if gender=='Female':
            self.driver.find_element(By.XPATH,self.Gender_female).click()

    def setdob(self,dob):
        self.driver.find_element(By.XPATH,self.dob_xpath).send_keys(dob)

    def setcompanyname(self,company):
        self.driver.find_element(By.XPATH,self.company_name).send_keys(company)

    def clksavebtn(self):
        self.driver.find_element(By.XPATH,self.savebtn).click()


# //div[@class='k-widget k-multiselect k-multiselect-clearable k-state-focused k-state-border-down']//div[@role='listbox']
