from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

####______________________________________________________________________________________________________####

'''

The following serves as a library for parsing html content and isolate objects of interest. 
To do this, the Pyhton Selenium library is used and adapted for the purpose.  

'''

####______________________________________________________________________________________________________####
## Private methods

####_____________________________________________________________________________________________________####
## Public methods



def find_element(driver: webdriver, wait: WebDriverWait, selector: str, selector_type=None):
    ''' 
    Private method to find a specific html element in the webdrivers current state.

    Inputs:
        driver: active selenium.webdriver object
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        WebElement with specified selector
    '''
    return wait.until(EC.presence_of_element_located((selector_type, selector)))

def find_all_elements(driver: webdriver, wait: WebDriverWait, selector: str, selector_type=None):
    ''' 
    Private method to find all specific html elements in the webdrivers current state.

    Inputs:
        driver: active selenium.webdriver object
        wait: selenium.webdriver.support.ui.WebDriverWait object
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Return:
        List of WebElements with specified selector
    '''
    return wait.until(EC.presence_of_element_located((selector_type, selector)))

def get_all_strings(web_elements, selector: str, selector_type):
    '''
    Finds all strings of interest in a list of web elements.

    Inputs:
        web_elements: list of web elements to search
        selector: String object to locate html element
        selector_type: selenium.webdriver.common.by.Literal object

    Returns:
        - List of all strings of interest
        - Dictionary where all strings are keys
          for respective web element

    '''

    ## Create list for all strings and key-value map for strings and web-elements
    result_list = []
    result_dic  = {}

    ## Go through all web elements
    for web_element in web_elements:
        
        ## Find specific element where string of interest is located
        specififc_element = web_element.find_element(selector_type, selector)

        ## If found, get title
        if specififc_element:

            ## Retrieve wanted string from 
            string = specififc_element.text

            ## Store wanted string in result_list
            result_list.append(string)

            ## Set value web element as value to string key
            result_dic[string] = web_element
            
    return result_list, result_dic
