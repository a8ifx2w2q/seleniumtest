
import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')


gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
gChromeOptions.add_argument("disable-blink-features=AutomationControlled")
gDriver = webdriver.Chrome(
    chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)
check=1
while(check>0):   
    gDriver.get(weburl)
    time.sleep(20)
    gDriver.quit()
    print("Times Run = ", check)
    check=check+1
