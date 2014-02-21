import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        chromedriver = os.path.join(os.getcwd(), "driver\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.get('http://www.gmail.com')
        self.addCleanup(self.browser.quit)
        self.email = "emailXXXXX@gmail.com"
        self.ps = "passwordXXX"

    def testInput(self):
        email = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "Email")))
        email.send_keys(self.email)
        pw = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "Passwd")))
        pw.send_keys(self.ps)
        self.assertIn('Gmail', self.browser.title)
        ele_submit = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "signIn")))
        ele_submit.submit()
        time.sleep(5)
        self.assertTrue(self.browser.current_url.startswith('https://mail.google.com/mail/'))
		
		
		
if __name__ == '__main__':
    unittest.main(verbosity=2)
