from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/productpage/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url )
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sathuvish@gmail.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("vishnu")
        driver.find_element_by_id("login_submit").click()
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("login_submit").click()
        cc = driver.find_element_by_class_name("login_alert")
        print type(cc.text)
        try:
            err = self.assertEqual(str(cc.text), "Username or Password are Incorrect.")
            print "valuse:",err
        except AssertionError as e: 
            print e
            raise
        #driver.find_element_by_css_selector("#signIn > div.modal-dialog > div.modal-content > div.modal-footer > button.btn.btn-default").click()
        
    def test_login1(self):
        driver = self.driver
        driver.get(self.base_url )
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("")
        driver.find_element_by_id("login_submit").click()
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("login_submit").click()
        cc = driver.find_element_by_class_name("login_alert")
        print type(cc.text)
        try:
            err = self.assertEqual(str(cc.text), "Fill All Form Details.")
            print "valuse:",err
        except AssertionError as e: 
            print e
            raise
    
    def tearDown(self):
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
