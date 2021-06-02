
import time
import os

import undetected_chromedriver.v2 as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')

check=1
while(check>0):
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    gDriver = uc.Chrome(
        options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
    
    gDriver.get(weburl)
    print("Waiting...")
    time.sleep(20)
    gDriver.close()
    print("Times Run = ", check)
    check=check+1
