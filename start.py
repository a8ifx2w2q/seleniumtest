import time
import os
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
weburl = os.getenv('WEB_URL')

check=1
while(check>0):
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options, executable_path=ChromeDriverManager().install())
    driver.get(weburl)
    time.sleep(1200)
    print("Times Run = ", check)
    check=check+1
