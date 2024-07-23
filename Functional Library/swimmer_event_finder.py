from selenium.webdriver.common.by import By

import event
import driver_handler
import html_renderer
import swimmer
import time


def run(url, club_name):
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(url, 5)
    
    swimmers = load_swimmers_and_events(driver, wait, club_name)

    ##________##
    driver.quit()
    return swimmers


def load_swimmers_and_events(driver, wait, selected_club):

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

            swimmer_div_map[swimmer_name].click()
            time.sleep(1)
    
            try:
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
                
                swimmer_object.print_events()

            except Exception as e:
                print(f"\tNo entries found. Error {e}")

    return swimmer_objects_map
        
## Test
# run("https://live.swimify.com/competitions/smpara-smjsm-50m-2024-2024-07-03/swimmers/clubs/206")