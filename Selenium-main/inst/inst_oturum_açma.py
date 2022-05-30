from instUserInfo import email,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:

    def __init__(self,email,password):
        self.browser= webdriver.Chrome()
        self.email=email
        self.password=password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        emailInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

a=Instagram(email,password)
a.signIn()




