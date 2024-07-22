from selenium.webdriver.common.by import By

import time
import driver_handler
import html_renderer


def run(url):
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(\
        url, 20)
    
    # Run selection method
    select_session(driver, wait)

    # Wait for closure
    input("Press Enter to cancel...")
    driver.quit()


def select_session(driver, wait):
    ##____ Find and map sessions ____##

    # Define the CSS selector for session div elements
    session_div_selector = 'div[class="MuiBox-root css-qlbhet"]'

    # Get all competition session div elements
    session_divs = html_renderer.find_all_elements(wait, \
                                session_div_selector, By.CSS_SELECTOR)
    
    session_map = {}

    for session_div in session_divs:
        # Find the name strings
        session_name = html_renderer.find_sub_element(session_div, \
                                    'p.MuiTypography-root.MuiTypography-body1.css-xu169k', \
                                        By.CSS_SELECTOR).text
        
        # Find the day and time and join strings
        session_time  = ' '.join([string.text for string in html_renderer.find_all_sub_elements(session_div, \
                                    'p.MuiTypography-root.MuiTypography-body1.css-bxnpil', \
                                        By.CSS_SELECTOR)])
        
        # Create a new name of type "Session X | Day Time"
        session_name = session_name + " | " + session_time

        # Map title string to div element
        session_map[session_name] = session_div

    ##____ Click through all sessions and load event schedule ____#

    # Key-value map for session and event schedule
    session_event_map = {}

    for key in session_map:

        # Print session name as title
        print("\n" + key)

        # Click session div element and wait for webdriver to load session information
        driver.execute_script("arguments[0].click();", session_map[key])
        time.sleep(2)

        # Load event schedule of session
        try:
            events = html_renderer.find_all_elements(wait, "//a[@display='flex']", By.XPATH)

            for event in events:
                # Extract the time
                start_time = html_renderer.find_sub_element(event, \
                                'div.MuiBox-root.css-z9ki6v > p', By.CSS_SELECTOR).text.strip()
  
                # Extract the event
                session_event = html_renderer.find_sub_element(event, \
                                    'div.MuiBox-root.css-6771j6 > p', By.CSS_SELECTOR).text
                
                # Add the extracted time and event to the map
                session_event_map[key] = ' | '.join([start_time, session_event])

                # Output the list of times and events
                print("\t" + session_event_map[key])

        except Exception as e:
            print(f"An error occurred: {e}")
        
    
run("https://live.swimify.com/competitions/smpara-smjsm-50m-2024-2024-07-03/events/summary/1/146")