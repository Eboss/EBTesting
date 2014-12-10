from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # 
import requests

class Loginnew(unittest.TestCase):

    ''' Setup Webdriver and base url '''

    # def setUp(self):
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    base_url_local = "http://beta.equityboss.com"
    base_url_server = "http://175.41.131.199"
    base_url = base_url_local
    verificationErrors = []
    accept_next_alert = True

    ''' Function For testing different Login usernames '''

    def login(self,driver,uname,paswd,error):

        driver.find_element_by_id("alpha_login_username").clear()
        driver.find_element_by_id("alpha_login_username").send_keys(uname)
        driver.find_element_by_id("alpha_login_password").clear()
        driver.find_element_by_id("alpha_login_password").send_keys(paswd)
        driver.find_element_by_id("alpha_login_login").click()
        data_error = driver.find_element_by_class_name("error_msg")
        print data_error.text
        
        print "******************************************"
        print "Checking error messages",data_error.text, "=",error
        print "*******************************************"
        try:
            err = self.assertEqual(str(data_error.text), error)
        except AssertionError as e: 
            print "error:",e
            raise

    ''' Test case for checking error message in login Page '''

    def test_errormessage(self):
        print "##################Testing Error Messages For Login Page##############"
        driver = self.driver
        driver.get(self.base_url+'/login/')
        #driver.find_element_by_link_text("Sign In").click()
        error1 = "Incorrect Email/Username Format"
        error2 = "Username / Password is Required"
        error3 = "Username or Password are Incorrect."
        self.login(driver,"vishnu","vishnu",error1)
        self.login(driver,"vishnu@gmail.com","vishnu",error3)
        self.login(driver,"","",error2)
        
    def test_loginsucces(self):
        print "##################Testing For login Success##############"
        driver = self.driver
        driver.get(self.base_url+'/login/')
        #driver.find_element_by_link_text("Sign In").click()
        self.login(driver,"admin@equityboss.com","admin2697",'')
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "watchlist_homepage")))
        print driver.current_url
        try:
            err = self.assertEqual(str(driver.current_url),self.base_url+"/watchlist/" )
        except AssertionError as e: 
            print e
            raise

    def test_watchlist(self):
        print "##################Testing Count Of Watchlist##############"
        driver = self.driver
        driver.get(self.base_url+'/watchlist/')
        datas_watchlist = driver.find_elements_by_class_name("single_wl")
        #for data in datas_watchlist:
            #print type(data.text)
        #    v = data.text.split()
            #print v
        #print len(datas_watchlist)

        d = driver.find_elements_by_class_name("b-dropdown-link")
        #print len(d)
        try:
            err = self.assertEqual(len(datas_watchlist),len(d)-1)
        except AssertionError as e: 
            print e
            raise
        #print cc

    def test_watchlisteditable(self):
        watchlist = []
        list1 = []
        stocks_datas = {"name":"","data" : {}}
        stocks_data_list = []
        driver = self.driver
        wl_data = driver.find_elements_by_class_name("top_wl")
        for i in wl_data:
            
            watchlist.append(i.text.split('\n'))
        
        #print watchlist
        for lis in watchlist:
            for ds in lis:
                list1.append(ds.split(':'))
        print list1
        print len(list1)
        for item in list1:
            if len(item) == 1:
                stocks_datas["name"] = item[0]
                #print stocks_datas
            else:
                stocks_datas["data"][item[0]] = item[1]
            #stocks_datas
            stocks_data_list.append(stocks_datas)
        print tuple(stocks_data_list)

        #print stocks_data_list

        # driver.get(self.base_url+'/api/eboss/wl/')
        # data = driver.find_elements_by_tag_name("html") 
        # r = requests.get(self.base_url+'/api/eboss/wl/',auth=('admin@equityboss.com', 'admin2697'))
        # print r
        #tex = data[0].text
        #pos = data[0].text.find('"watchlist"')
        #print tex[213616:]
        # r = requests.get(self.base_url+'/api/eboss/wl/')
        # print r.json()
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



