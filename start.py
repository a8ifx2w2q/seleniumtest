
import time
import os

import undetected_chromedriver.v2 as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')

check=1
while(check>0):
    options = uc.ChromeOptions()
    options.user_data_dir=/app/
    options.add_argument("window-size=1920x1480")
    options.add_argument("disable-dev-shm-usage")
    driver = uc.Chrome(
        options=options, executable_path=ChromeDriverManager().install()
    )
    
    driver.get(weburl)
    print("Waiting...")
    time.sleep(20)
    driver.close()
    print("Times Run = ", check)
    check=check+1
