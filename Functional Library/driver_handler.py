from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

import time

####______________________________________________________________________________________________________####

'''

The following serves as a library for handling selenium.webdriver objects.

'''

####______________________________________________________________________________________________________####

def setup_driver(url: str, timeout: float):
    '''
    Function for initializing webdriver and WebdriverWait objects.

    Input:
        url: string with url adress of webpage of interest
        timeout: float object for maximal allowed time of loading

    Return:
        webdriver and webdriver wait objects
    '''
    # Set up the Chrome WebDriver
    driver_options = Options()
    driver_options.add_argument("--headless=new")
    driver = webdriver.Chrome(driver_options)

    driver.get(url) 
    wait = WebDriverWait(driver, timeout, ignored_exceptions=[TimeoutException, WebDriverException, ElementNotInteractableException])
    time.sleep(3)

    return driver, wait

