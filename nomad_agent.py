import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
load_dotenv(".env")

print("Has error module:", hasattr(selenium , 'error'))

if hasattr(selenium, 'error'):
    print("Has NoSuchElementExpection:", hasattr(openai.NoSuchElementException, 'NoSuchElementException'))
    

email = os.environ["ACCOUNT_EMAIL"]
pw = os.environ["ACCOUNT_PASSWORD"]
phone = os.environ["PHONE"]
url = os.environ["URL"]

print(email)

chrome_driver_path = os.environ["CHROMEDRIVER_PATH"]


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()
    
    
# Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

print("CHROMEDRIVER STARTED...")
print("OPENING URL ")
print(url)



driver.get(url)
