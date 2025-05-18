#Project to Remove spamm mail from yahoo mail
import time as t
import pyautogui as gui
from selenium import webdriver as webdriver

t.sleep(7)

chrome_driver = webdriver.Chrome("./chromedriver")
chrome_driver.maximize_window()
chrome_driver.get('https://login.yahoo.com')

username_textbox=chrome_driver.find_element_by_id("login-username")

username_textbox.send_keys("xxxxxxxxxxxxxxxxx@yahoo.com")#username
t.sleep(3)
next_btn=chrome_driver.find_element_by_id("login-signin")
next_btn.click()

if "Prove you're not a robot" in chrome_driver.page_source:
    t.sleep(10)#Completing Captcha

t.sleep(60)#Entering OTP

for i in range(76):
    gui.click(x=356,y=460)#Clicking on delete

    if "primary-btn" in chrome_driver.page_source:
        primary=chrome_driver.find_element_by_id("primary-btn")
        primary.click()
    else:
        print("we need help")
        t.sleep(5)

    t.sleep(3)
    


