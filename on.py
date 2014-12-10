import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(self.base_url+"/productpage/")
        driver.find_element_by_link_text("Sign In").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("admin@equityboss.com")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin2697")
        driver.find_element_by_id("login_submit").click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "watchlist_homepage")))
        #self.driver.implicitly_wait(3000)
        print element.text
        print self.driver.current_url
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("selenium")
        # elem.send_keys(Keys.RETURN)
        #self.assertIn("Google", driver.title)
        

    def tearDown(self):
        
    	#print self.driver.current_window_handle
        self.driver.close()

if __name__ == "__main__":
    unittest.main()