from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\PathTochromedriver.exe')   # required path if you use windows

def get_driver_args():
# different arguments used for accessing the web content through web driver in a smootherway.
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("disable-infobars")
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("disable-dev-shm-usage")
    chromeoptions.add_argument("no-sandbox")
    chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    chromeoptions.add_argument("disable-blink-features=AutomationControlled")

    chrome_driver = webdriver.Chrome(service=service, options=chromeoptions)
    chrome_driver.get("https://mausam.imd.gov.in/")  # rquired web URL to scrap content
    return chrome_driver

def filter_text(text1, text2):
    """Extracting and handling two text inputs simultaneously"""

    text_output1 = text1.split("Southwesterly")[1].strip()
    text_output2 = text2.split(": ")[1].strip()

    return f"The captured wind speed is {text_output1} at the time of {text_output2}"

def get_content():
    chrome_driver = get_driver_args()
    # Get the xpath by using inspect mode of a web browser   
    ele_xpath1 = chrome_driver.find_element(by="xpath", value="/html/body/section[3]/div[2]/div[1]/div/div/div[1]/div/div/div/section/div/div[2]/div[2]/div[4]") 
    ele_xpath2 = chrome_driver.find_element(by="xpath", value="/html/body/section[3]/div[2]/div[1]/div/div/div[1]/div/div/div/section/div/div[2]/div[2]/div[5]")
    
    return filter_text(ele_xpath1.text,ele_xpath2.text)

print(get_content())

