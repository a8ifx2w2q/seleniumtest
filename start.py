import time
import os
import undetected_chromedriver as uc
from selenium import webdriver

weburl = os.getenv('WEB_URL')

check=1
while(check>0):


    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options, executable_path=/app/.apt/usr/bin/google-chrome)
    driver.get('https://bet365.com')
    print("Times Run = ", check)
    check=check+1
