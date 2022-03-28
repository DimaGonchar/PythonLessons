import webbrowser
from selenium import webdriver
import os
import time
import selenium
from heshtags import heshtagsList
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from instagramLogIn import instagramLogInData
from facebookLogIn import facebookLogInData

options=Options()
options.add_argument("--disable-infobars")
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
pathToChromeDriver=os.getcwd()+"\\Drivers\\Chrome\\chromedriver.exe"

driver=webdriver.Chrome(chrome_options=options, executable_path= pathToChromeDriver)
driver.get("https://instagram.com")

try:
    driver.implicitly_wait(20)
    intagramIdentificator=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    intagramIdentificator.clear()
    intagramIdentificator.send_keys(instagramLogInData.get("login"))

    
    instagramPassword=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    instagramPassword.clear()
    instagramPassword.send_keys(instagramLogInData.get("password"))

    logInButton=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
    logInButton.click()
   
except exceptions.ImeNotAvailableException as exeption:
    print(exeption)
    logInWithFacebookButton=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]")
    logInWithFacebookButton.click()

    facebookLoginForm=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input")
    facebookLoginForm.send_keys(facebookLogInData.get("login"))
    
    facebookPasswordForm=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input")
    facebookPasswordForm.send_keys(facebookLogInData.get("password"))

    facebookLogInButton=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button")
    facebookLogInButton.click()

try:
    notNowButton=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
    notNowButton.click()

except exceptions.NoSuchElementException as exption:
    driver.implicitly_wait(10)
    turnOffNotificationButton=driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
    turnOffNotificationButton.click()

searchByTag=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")

searchByTag.send_keys(random.choice(heshtagsList))
searchByTag.click()

enterButton=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a")
enterButton.click()

searchByTag.send_keys(Keys.ENTER)
searchByTag.send_keys(Keys.ENTER)

time.sleep(1000)