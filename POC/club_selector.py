from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import driver_handler
import html_renderer

####______________________________________________________________________________________________________####

'''

The following serves as a library for allowing choice of club/clubs in a given Swimify competition

'''

####______________________________________________________________________________________________________####
def run(url):
    '''
    Demo run of class. Takes the url of the Swimify competition
    and runs through all essential functions of class
    '''
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(\
        url, 20)
    
    club_url = select_club(driver, wait)

    # Wait for closure
    driver.quit()
    return club_url

##____ Choose competition section depending on input ____##
def _choice_index(list_of_choices):
    '''
    Private method to allow interactive choice in list from 
    terminal.

    Input:
        list_of_choices: list with found objects to choose from

    Return:
        index of choice.
    '''
    choice_index = -1
    last_index   = len(list_of_choices) - 1
    while ((choice_index < 0) or (last_index < choice_index)):
        try:
            if last_index < choice_index: 
                print("Not a valid input\n\n") 
                choice_index = -1
            else: 
                choice_index = int(input("\nEnter index to click: ")) - 1
        except ValueError:
            print("\nPlease enter a valid integer index.\n")
    

    print(f'\nSelected {choice_index + 1}: {list_of_choices[choice_index]}\n')
    return choice_index

def select_club(driver, wait):
    '''
    Interactive function that finds all clubs entered in a Swimify competition
    and allows user to select one club of interest.

    Input:
        driver: active selenium.webdriver object
        wait: active selenium.webdriver.WebdriverWait object
    '''
    ##____ Enter the "Swimmers" menu to locate the clubs ____#
    try:
        # Wait for the button to be clickable
        button = html_renderer.find_element(wait, '//button[.//p[contains(text(), "Swimmers")]]', By.XPATH)
        
        # Click the button using JavaScript
        html_renderer.click_element(driver, button)

        # Locate all the parent div elements containing the club information
        club_divs = html_renderer.find_all_elements(wait, 'div.MuiBox-root.css-1eukt2p', By.CSS_SELECTOR)
        club_divs.append(html_renderer.find_element(wait, 'div.MuiBox-root.css-1fis6zz', By.CSS_SELECTOR))

        # Get list of club names and key-value map with club names and clickable div elements
        club_names, club_div_map = html_renderer.get_all_strings(club_divs, \
                                        'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-1bpwwm7', \
                                            By.CSS_SELECTOR)
        print("\nSelect Club:")

        for i, club_name in enumerate(club_names):
            print(f'\t{i + 1} ' + club_name)

        
        # Get the user input choice of club
        choice = _choice_index(club_names)
        html_renderer.click_element(driver, club_div_map[club_names[choice]])

        print("Found Club URL: " + driver.current_url)

        return club_names[choice], driver.current_url

    except Exception as e:
        print(f'Error: {e}')


def check_if_swedish_club(club_name):
    '''
    Boolean returning true if the club name entered is featured in Tempus Open database.
    
    Inputs:
        club_name: str object with club name.
        
    Return: 
        True if club_name in Tempus, False otherwise or if WebdriverWait object times out.
    '''
    # Initialize the WebDriver
    try:
        # Navigate to the specified URL
        driver, wait = driver_handler.setup_driver("https://svensksimidrott.se/vara-simidrotter/simning/om/hitta-din-forening", 10)

        # Find the search input element using its ID
        search_input = html_renderer.find_element(wait, "search1", By.ID)

        # Clear any pre-filled text in the search input (optional, usually good practice)
        search_input.clear()

        # Enter the club name into the search input
        search_input.send_keys(club_name)

        # Submit the form (this might be automatic based on the site's behavior)
        search_input.send_keys(Keys.RETURN)

        # Wait until elements of the specified type are present on the page
        try:
            elements_present = wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'div.vti4syij6mFN3aMkVRop > div.KtHlRBLdoxSVj3WTjGuU > b.normal')))
            return True if elements_present else False
        except TimeoutException:
            return False
    finally:
        # Close the WebDriver (clean up)
        driver.quit()
