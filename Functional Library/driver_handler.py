from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotInteractableException
import time


def setup_driver(url, timeout):
    # Set up the Chrome WebDriver
    driver_options = Options()
    driver_options.add_argument("--headless=new")
    driver = webdriver.Chrome(driver_options)

    driver.get(url) 
    wait = WebDriverWait(driver, timeout, ignored_exceptions=[TimeoutException, WebDriverException, ElementNotInteractableException])
    time.sleep(3)

    return driver, wait

