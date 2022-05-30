from selenium.webdriver.common import keys
from instUserInfo import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:

    def __init__(self,username,password):
        self.browser= webdriver.Chrome()
        self.username=username
        self.password=password
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)


    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").click()
        #followersLink.click()

        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        time.sleep(2)
        followersCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followersCount}")
        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followersCount != newCount:
                followersCount=newCount
                print(f"second count : {newCount}")
                time.sleep(2)
            else: 
                break

        followers = dialog.find_elements_by_css_selector("li")

        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)



a=Instagram(username,password)
a.signIn()
a.getFollowers()


