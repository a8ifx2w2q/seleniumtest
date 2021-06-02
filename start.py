
import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

weburl = os.getenv('WEB_URL')


gChromeOptions = webdriver.ChromeOptions()
gChromeOptions.add_argument("window-size=1920x1480")
gChromeOptions.add_argument("disable-dev-shm-usage")
gChromeOptions.add_argument("disable-blink-features=AutomationControlled")
gChromeOptions.add_argument("no-sandbox")
gChromeOptions.add_argument("'useAutomationExtension', False")
gChromeOptions.add_argument('"excludeSwitches", ["enable-logging", "enable-automation"]')
gChromeOptions.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"')
gDriver = webdriver.Chrome(
    chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
)
check=1
while(check>0):   
    gDriver.get(weburl)
    time.sleep(20)
    gDriver.close()
    print("Times Run = ", check)
    check=check+1
