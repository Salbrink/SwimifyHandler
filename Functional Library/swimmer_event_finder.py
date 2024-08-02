from selenium.webdriver.common.by import By

import event
import driver_handler
import html_renderer
import swimmer
import tempus_scraper

####______________________________________________________________________________________________________####

'''

The following serves as a library for localizing entered swimmers in a given Swimfy competition.
There are also possibilities to find events for respective swimmer and---given that the swimmers are
registered in Sweden---locate the personal best times of the events from Tempus Open

'''

####______________________________________________________________________________________________________####

def run(url: str, club_name: str):
    '''
    Demo run of class. Takes the url of the Swimify competition
    and runs through all essential functions of class
    '''
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(url, 5)
    
    swimmers = load_swimmers_and_events(driver, wait, club_name)

    ##________##
    driver.quit()
    return swimmers


def load_swimmers_and_events(driver, wait, selected_club: str):
    '''
    Function for loading all swimmers from a given club and also all entered
    events for each swimmer

    Input:
        driver: active selenium.webdriver object
        wait: active selenium.webdriver.WebdriverWait object

    Return:
        Key-value map with keys of swimmer string name and value of swimmer.py objects
    '''

    # Find swimmer div elements
    swimmer_divs = html_renderer.find_all_elements(wait, \
                        'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-1hbn5fk', By.CSS_SELECTOR)
    
    # Get list of swimmer names and key-value map of swimmer name and clickable div element
    swimmer_names, swimmer_div_map = html_renderer.get_all_strings(swimmer_divs, \
                                        'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-lc08jz', \
                                            By.CSS_SELECTOR)

    # Key-value map of swimmer names and swimmer.py objects
    swimmer_objects_map = {}

    for swimmer_name in swimmer_names:
        if selected_club in swimmer_name: 
            print("\n\tRelays not yet handled")

        else:
            print("\n" + swimmer_name)
            # Create new swimmer instance
            try:
                first_name, last_name = swimmer_name.split(' ', 1)
                swimmer_object = swimmer.Swimmer(first_name, last_name, selected_club)
                swimmer_objects_map[swimmer_name] = swimmer_object
            except ValueError:
                print("Not a swimmer")

            html_renderer.click_element(driver, swimmer_div_map[swimmer_name])
    
            try:
                _find_events(wait, swimmer_object)

                tempus_driver, tempus_wait = driver_handler.setup_driver("https://www.tempusopen.se/index.php?r=Swimmer", 10)

                _find_best_times(tempus_driver, tempus_wait, swimmer_object)
                
                swimmer_object.print_events()

            except Exception as e:
                print(f"\tNo entries found. Error {e}")

    return swimmer_objects_map

def _find_events(wait, swimmer_object):
    '''
    Private method for  finding entered events of a swimmer.py object in a Swimify competition

    Input:
        wait: active selenium.webdriver.WebdriverWait object
        swimmer_object: swimmer.py object
    '''
    # Locate the parent div elements with the specified class
    event_elements = html_renderer.find_all_elements(wait, \
                            'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-h9dk79', \
                                By.CSS_SELECTOR)
    
    for event_element in event_elements:
        # Locate the p element with the specific class within the parent element
        p_element = html_renderer.find_sub_element(event_element, \
                        'div.MuiBox-root.css-2ijh4t > p.MuiTypography-root.MuiTypography-body1.css-151uy7p', \
                            By.CSS_SELECTOR)
        
        # Extract the text content and add it to the swimmer object
        event_string = ''.join(p_element.text)
        swimmer_object.add_event(event.Event(event_string))

def _find_best_times(driver, wait, swimmer_object):
    driver.get("https://www.tempusopen.se/index.php?r=Swimmer")

    events = swimmer_object.events

    event_string_list = [e.distance for e in events]

    

    print(events)