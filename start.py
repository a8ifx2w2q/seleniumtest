import time
import os
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
weburl = os.getenv('WEB_URL')
options = webdriver.ChromeOptions() 
options.add_argument("window-size=1920x1480")
options.add_argument("disable-blink-features=AutomationControlled")
options.add_argument("disable-dev-shm-usage")
options.add_argument("no-sandbox")
options.add_argument("'useAutomationExtension', False")
options.add_argument('"excludeSwitches", ["enable-logging", "enable-automation"]')
options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17"')
driver = uc.Chrome(options=options, executable_path=ChromeDriverManager().install())
check=1
while(check>0):
    driver.get(weburl)
    print("Website Loaded... Waiting")
    time.sleep(20)
    driver.quit()
    print("Times Run = ", check)
    check=check+1
