import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


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
        
def user_sign_in(driver,email,pw,phone):
    wait = WebDriverWait(driver, 10)  
    try:
        
        sign_in_button_xpath = "html/body/div[3]/a[1]" 
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, sign_in_button_xpath)))        
        print("FOUND SIGN IN BUTTON POP UP")
        # Scroll to the element and then click
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)
        sign_in_button.click()
    except TimeoutException:
        print("Sign in button pop up not found, trying navigation bar")

        try:
            nav_bar_button_xpath = "/html/body/div[1]/header/nav/div/a[2]"
            sign_in_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, nav_bar_button_xpath)))
            print("FOUND SIGN IN ON NAV BAR")
            # Scroll to the element and then click
            driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_page_button)
            sign_in_page_button.click()
        except TimeoutException:
            print("Sign in button on navigation bar not found")
            
    # INPUT USER LOGIN INFO
    try:
        emailphone_xpath = '//*[@id="username"]' 
        username_input = wait.until(EC.element_to_be_clickable((By.XPATH, emailphone_xpath)))        
        print("FOUND EMAIL OR PHONE INPUT")
        username_input.send_keys(email)
        time.sleep(2)
        password_xpath = '//*[@id="password"]' 
        password_input= wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath))) 
        print("FOUND PASSWORD INPUT")
        password_input.send_keys(pw, Keys.ENTER)
        time.sleep(2)
    except TimeoutException:
        print("COULD NOT INPUT USER DETAILS INTO SIGN IN FORM")


def apply_to_jobs(driver,all_listings):
    wait = WebDriverWait(driver, 10)  
    # APPLY FOR JOBS
    for listing in all_listings:
        print("Listing Opening...")
        print(listing)
        driver.execute_script("arguments[0].scrollIntoView(true);", listing)
        try:
            wait.until(EC.element_to_be_clickable(listing))
            listing.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", listing)
        time.sleep(2)
        try:
            # Click Apply Button
            apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            apply_button.click()
            # Insert Phone Number
            # Find an <input> element where the id contains phoneNumber
            time.sleep(5)
            phone_input = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
            if phone_input.text == "":
                phone_input.clear()
                time.sleep(1)
                phone_input.send_keys(phone)
            else:
                print("COULD NOT GET PHONE INPUT FIELD")
            
            # Check the Submit Button
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="artdeco-button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                abort_application()
                print("Complex application, This listing has been skipped.")
                continue
            else:
                # Click Submit Button
                print("Submitting job application")
                submit_button.click()
            
            time.sleep(2)
            # Click Close Button
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()


        except NoSuchElementException:
            print("DRIVER COULD NOT APPLY TO JOB")
            abort_application()
            continue

    
    print("ALL JOB LISTINGS HAVE BEEN PROCCESSED")
    time.sleep(5)
    driver.quit()


    
    
# Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)  
print("CHROMEDRIVER STARTED...")
print("OPENING URL ")
print(url)


driver.get(url)


# SIGN IN USER
user_sign_in(driver,email,pw,phone)
time.sleep(5)

# GET LISTINGS
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

if all_listings:
    print("Starting the job application process...")
    apply_to_jobs(driver,all_listings)
else:
    print("COULD NOT FIND JOB LISTINGS ELEMENT")



