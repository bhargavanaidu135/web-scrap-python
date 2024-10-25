from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\\Users\\PathTochromedriver.exe')
# something added for demo
def get_driver_args():

    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("disable-infobars")
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("disable-dev-shm-usage")
    chromeoptions.add_argument("no-sandbox")
    chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeoptions.add_argument("disable-blink-features=AutomationControlled")

    chrome_driver = webdriver.Chrome(service=service, options=chromeoptions)
    chrome_driver.get("https://account.amazon.jobs/en-US/login?relay=%2Fen-US")
    return chrome_driver

def main():
    driver = get_driver_args()
#something added  
    # entering username in the login field by using inspect keyId(NAME) and values(email)
    driver.find_element(By.NAME, "email").send_keys("<UserName>")
    time.sleep(2)
  
    # once the username(email) is given and then clicks on sign-in-button
    driver.find_element(By.ID, "sign-in-button").click()
    time.sleep(5)
  
    # Entering password and keys.RETURN(means Enter)
    driver.find_element(By.NAME, "password").send_keys("<Password>" + Keys.RETURN)
  
    # get the current url path
    print(driver.current_url)

print(main())


