from selenium import webdriver
import time

driver =webdriver.Chrome()

url = "https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/"

driver.get(url)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("driver.png")

url = "https://github.com/***kullanıcı adını yaz"
driver.get(url)


print(driver.title)
if "**kulanıcı adını yaz**" in driver.title: #kullanıcı adını yaz
    driver.save_screenshot("github.png")

print(time.sleep(2))

driver.back()
#driver.forward()

time.sleep(2)
driver.close()