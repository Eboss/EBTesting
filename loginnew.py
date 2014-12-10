from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # 

class Loginnew(unittest.TestCase):

    ''' Setup Webdriver and base url '''

    # def setUp(self):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    base_url = "http://127.0.0.1:8000"
    verificationErrors = []
    accept_next_alert = True

    ''' Function For testing different Login usernames '''

    def login(self,driver,uname,paswd,error):

        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(uname)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(paswd)
        driver.find_element_by_id("login_submit").click()
        data_error = driver.find_element_by_class_name("login_alert")
        print data_error.text
        
        print "******************************************"
        print "Checking error messages",data_error.text, "=",error
        print "*******************************************"
        try:
            err = self.assertEqual(str(data_error.text), error)
        except AssertionError as e: 
            print e
            raise

    ''' Test case for checking error message in login Page '''

    def test_errormessage(self):
        print "##################Testing Error Messages For Login Page##############"
        driver = self.driver
        driver.get(self.base_url+'/login/')
        driver.find_element_by_link_text("Sign In").click()
        error1 = "Username or Password are Incorrect."
        error2 = "Fill All Form Details."
        self.login(driver,"vishnu","vishnu",error1)
        self.login(driver,"vishnu@gmail.com","vishnu",error1)
        self.login(driver,"","",error2)
        
    def test_loginsucces(self):
        print "##################Testing Error Messages For Login Page##############"
        driver = self.driver
        driver.get(self.base_url+'/login/')
        driver.find_element_by_link_text("Sign In").click()
        self.login(driver,"admin@equityboss.com","admin2697",'')
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "watchlist_homepage")))
        print driver.current_url
        try:
            err = self.assertEqual(str(driver.current_url),"http://127.0.0.1:8000/watchlist/" )
        except AssertionError as e: 
            print e
            raise

    def test_watchlist(self):
        driver = self.driver
        driver.get(self.base_url+'/watchlist/')
        datas_watchlist = driver.find_elements_by_class_name("single_wl")
        for data in datas_watchlist:
            print type(data.text)
            v = data.text.split()
            print v
        len(datas_watchlist)
        d = driver.find_elements_by_class_name("b-dropdown-link")
        len(d)
        #print cc
        self.driver.quit()
 
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    # def tearDown(self):
    #     #self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
