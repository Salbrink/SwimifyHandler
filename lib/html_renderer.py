from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from logging import debug, log
import time

####______________________________________________________________________________________________________####

'''

The following serves as a library for parsing html content and isolate objects of interest. 
To do this, the Pyhton Selenium library is used and adapted for the purpose.  

'''

####______________________________________________________________________________________________________####


def click_element(driver, element) -> None:
    '''
    Public method to interact with clickable WebElement

    Inputs:
        driver: active selenium.webdriver object
        element: interactable WebElement
        
    '''
    try:
        element.click()
    except ElementNotInteractableException:
        # Try scrolling into view and clicking again
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Small delay to allow scroll action to complete
        element.click()

def find_element(wait: WebDriverWait, selector: str, selector_type=None, wait_time=10) -> WebElement:
    ''' 
    Public method to find a specific html element in the webdrivers current state.

    Inputs:
        driver: active selenium.webdriver object
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        WebElement with specified selector
    '''
    try:
        element = wait.until(EC.presence_of_element_located((selector_type, selector)))
        wait.until(EC.visibility_of(element))
        return element
    except TimeoutException as e:
        debug(f"TimeoutException: Element not found within {wait_time} seconds.")
        debug(f"Selector: {selector}")
        debug(f"Selector Type: {selector_type}")
        

def find_all_elements(wait: WebDriverWait, selector: str, selector_type=None) -> list[WebElement]:
    ''' 
    Public method to find all specific html elements in the webdrivers current state.

    Inputs:
        driver: active selenium.webdriver object
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html elements
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        List of WebElements with specified selector
    '''
    try:
        elements = wait.until(EC.presence_of_all_elements_located((selector_type, selector)))
        return elements
    except TimeoutException as e:
        debug(f"TimeoutException: Element not found within {10} seconds.")
        debug(e.stacktrace)
        return None

def find_sub_element(parent, selector: str, selector_type=None) -> WebElement:
    ''' 
    Public method to find a specific html element in a parent html element in 
    the webdrivers current state.

    Inputs:
        parent: parent WebElement
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        WebElement with specified selector
    '''
    return parent.find_element(selector_type, selector)

def find_all_sub_elements(parent, selector: str, selector_type=None) -> list[WebElement]:
    ''' 
    Public method to find all specific html elements in a parent html element in 
    the webdrivers current state.

    Inputs:
        parent: parent WebElement
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        List of WebElements with specified selector
    '''
    return parent.find_elements(selector_type, selector)

def get_all_strings(web_elements, selector: str, selector_type) -> map:
    '''
    Finds all strings of interest in a list of web elements.

    Inputs:
        web_elements: list of web elements to search
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Returns:
        - Dictionary where all strings are keys
          for respective web element

    '''

    ## Create list for all strings and key-value map for strings and web-elements
    result_dic  = {}

    ## Go through all web elements
    for web_element in web_elements:

        ## Find specific element where string of interest is located
        specififc_element = web_element.find_element(selector_type, selector)

        ## If found, get title
        if specififc_element:

            ## Retrieve wanted string from 
            string = specififc_element.text

            ## Set value web element as value to string key
            result_dic[string] = web_element
            
    return result_dic
