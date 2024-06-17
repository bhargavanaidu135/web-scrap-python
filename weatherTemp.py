from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\bhargava\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

def get_driver_args():

    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("disable-infobars")
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("disable-dev-shm-usage")
    chromeoptions.add_argument("no-sandbox")
    chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeoptions.add_argument("disable-blink-features=AutomationControlled")

    chrome_driver = webdriver.Chrome(service=service, options=chromeoptions)
    chrome_driver.get("https://mausam.imd.gov.in/")
    return chrome_driver

def filter_text(text):
    """Extract only the dynamic text or number"""
    text_output = str(text.split("Southwesterly"))
    return text_output
def filter_text2(text2):
    text_output2 = str(text2.split(": ")[1])
    return text_output2


def get_content():
    chrome_driver = get_driver_args()
    ele_xpath = chrome_driver.find_element(by="xpath", value="/html/body/section[3]/div[2]/div[1]/div/div/div[1]/div/div/div/section/div/div[2]/div[2]/div[4]") 
    ele_xpath2 = chrome_driver.find_element(by="xpath", value="/html/body/section[3]/div[2]/div[1]/div/div/div[1]/div/div/div/section/div/div[2]/div[2]/div[5]")
    print(filter_text2(ele_xpath2.text))
    return filter_text(ele_xpath.text)

print(get_content())

