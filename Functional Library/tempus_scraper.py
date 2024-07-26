from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException


import time
import swimmer
import driver_handler
import html_renderer


def run(url, swimmer_object, event_list):
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(url, 10)
    
    sc_map, lc_map = get_PB_of_swimmer_object(driver, wait, swimmer_object, event_list)

    print_PB(event_list, sc_map, lc_map)

    #________##
    driver.quit()

def get_PB_of_swimmer_object(driver, wait, swimmer_object, event_list):

    # Find search bars and enter information from swimmer object
    first_name = html_renderer.find_element(wait, "Swimmer_first_name", By.ID)
    first_name.send_keys(swimmer_object.first_name)

    last_name  = html_renderer.find_element(wait, "Swimmer_last_name", By.ID)
    last_name.send_keys(swimmer_object.last_name)
    
    club_name  = html_renderer.find_element(wait, "Swimmer_swimmer_club", By.ID)
    club_name.send_keys(swimmer_object.club)

    # Press search button
    search_button = html_renderer.find_element(wait, 'input[type="submit"][name="yt0"][value="Sök"]', By.CSS_SELECTOR)
    search_button.click()

    # Press first swimmer
    top_search = html_renderer.find_element(wait, '//tr[@class="odd"]//a[@class="view"]', By.XPATH)
    if top_search is None:
        print("Swimmer Tempus not found")
        return {}, {}
    top_search.click()

    ##____ In swimmer menu ____##
    # Get map for short course PB's of events of interest
    sc_map = search_section(wait, "//h3[text()='Kortbana (25m)']", By.XPATH, event_list)

    # Get map for long course PB's of events of interest
    lc_map = search_section(wait, "//h3[text()='Långbana (50m)']", By.XPATH, event_list)

    return sc_map, lc_map


def search_section(wait, section_selector, section_selector_type, event_list):
    map = {}
    
    try:
        # Locate the header
        header = html_renderer.find_element(wait, section_selector, section_selector_type)
        
        # Find the table following the header
        table = html_renderer.find_sub_element(header, "following-sibling::div[@class='grid-view']/table", By.XPATH)

        # Locate all table rows of the specified type (both odd and even) within the Kortbana table
        rows = html_renderer.find_all_sub_elements(table, 'tbody tr.odd, tbody tr.even', By.CSS_SELECTOR)
        
        for row in rows:
            # Find the event name cell and extract the event name
            event_name = html_renderer.find_sub_element(row, 'td.name-column', By.CSS_SELECTOR).text.split('\n')[0].strip().lower()
            
            # Check if the event name is in the predefined list
            if event_name in event_list:
                # Extract the date and time from the respective cells
                date = html_renderer.find_all_sub_elements(row, 'td', By.TAG_NAME)[2].text.strip()
                time = html_renderer.find_all_sub_elements(row, 'td', By.TAG_NAME)[3].text.strip()
                # Add the date and time as a tuple to the list
                map[event_name] = (date, time)
        return map

    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
    
def print_PB(event_list, sc_map, lc_map):
    for event_name in event_list:
        try:
            print("\t" + event_name + " PB Short course: " + sc_map[event_name][1] + " date " + sc_map[event_name][0])    
        except KeyError:
            print("\tNo personal best for " + event_name + " SC")

        try:
            print("\t" + event_name + " PB Long course: " + lc_map[event_name][1] + " date " + lc_map[event_name][0])    
        except KeyError:
            print("\tNo personal best for " + event_name + " LC")

## Test
# run("https://www.tempusopen.se/index.php?r=Swimmer", swimmer.Swimmer("Ian", "Hangård", "Simklubben Sydsim"), ["25m fjärilsim", "1500m frisim", "100m ryggsim", "200m medley"])