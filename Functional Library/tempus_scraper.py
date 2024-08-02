from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import driver_handler
import html_renderer


####______________________________________________________________________________________________________####

'''

The following serves as a library for scraping information of Tempus Open. The methods are only applicable
when the club/swimmer in question is registered in Tempus.

'''

####______________________________________________________________________________________________________####

def run(url, swimmer_object, event_list):
    '''
    Demo run of class. Takes the url of the Swimify competition
    and runs through all essential functions of class
    '''
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(url, 10)
    
    sc_map, lc_map = get_PB_of_swimmer_object(driver, wait, swimmer_object, event_list)

    print_PB(event_list, sc_map, lc_map)

    #________##
    driver.quit()

def get_PB_of_swimmer_object(driver, wait, swimmer_object, event_list):
    '''
    Function for finding personal bests in long course and short course 
    for a given swimmer.py object.
    
    Input:
        driver: active selenium.webdriver object
        wait: active selenium.webdriver.WebdriverWait object

    Return:
        Key-value maps with event name as Key and time:date of PB as value for
        both short course and long course.
    '''

    # Find search bars and enter information from swimmer object
    first_name = html_renderer.find_element(wait, "Swimmer_first_name", By.ID)
    first_name.send_keys(swimmer_object.first_name)

    last_name  = html_renderer.find_element(wait, "Swimmer_last_name", By.ID)
    last_name.send_keys(swimmer_object.last_name)
    
    club_name  = html_renderer.find_element(wait, "Swimmer_swimmer_club", By.ID)
    club_name.send_keys(swimmer_object.club)

    # Press search button
    search_button = html_renderer.find_element(wait, 'input[type="submit"][name="yt0"][value="Sök"]', By.CSS_SELECTOR)
    html_renderer.click_element(driver, search_button)

    # Press first swimmer
    top_search = html_renderer.find_element(wait, '//tr[@class="odd"]//a[@class="view"]', By.XPATH)
    if top_search is None:
        print("Swimmer Tempus not found")
        return {}, {}
    html_renderer.click_element(driver, top_search)

    ##____ In swimmer menu ____##
    # Get map for short course PB's of events of interest
    sc_map = _search_section(wait, "//h3[text()='Kortbana (25m)']", By.XPATH, event_list)

    # Get map for long course PB's of events of interest
    lc_map = _search_section(wait, "//h3[text()='Långbana (50m)']", By.XPATH, event_list)

    return sc_map, lc_map


def _search_section(wait, section_selector, section_selector_type, event_list):
    '''
    Private method for creating a map given a section in tempus page of a swimmer.

    Input:
        wait: active selenium.webdriver.WebdriverWait object
        section_selector: selector for finding html object of section
        section_selection_type: selenium.webdriver.common.by selector
        event_list: list of event_string names

    Return:
        Kay-Value map with event name as key and time and date of personal best as value.
    '''
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
    '''
    Method for printing events and personal best times in terminal.
    
    Input:
        event_list: list of event names as strings
        sc_map: Key-Value map of event and personal bests short course
        lc_map: Key-Value map of event and personal bests long course
        '''
    for event_name in event_list:
        try:
            print("\t" + event_name + " PB Short course: " + sc_map[event_name][1] + " date " + sc_map[event_name][0])    
        except KeyError:
            print("\tNo personal best for " + event_name + " SC")

        try:
            print("\t" + event_name + " PB Long course: " + lc_map[event_name][1] + " date " + lc_map[event_name][0])    
        except KeyError:
            print("\tNo personal best for " + event_name + " LC")

def add_times_to_events(driver, wait, swimmer_object):
    # Find search bars and enter information from swimmer object
    first_name = html_renderer.find_element(wait, "Swimmer_first_name", By.ID)
    first_name.send_keys(swimmer_object.first_name)

    last_name  = html_renderer.find_element(wait, "Swimmer_last_name", By.ID)
    last_name.send_keys(swimmer_object.last_name)
    
    club_name  = html_renderer.find_element(wait, "Swimmer_swimmer_club", By.ID)
    club_name.send_keys(swimmer_object.club)

    # Press search button
    search_button = html_renderer.find_element(wait, 'input[type="submit"][name="yt0"][value="Sök"]', By.CSS_SELECTOR)
    html_renderer.click_element(driver, search_button)

    # Press first swimmer
    top_search = html_renderer.find_element(wait, '//tr[@class="odd"]//a[@class="view"]', By.XPATH)
    if top_search is None:
        print("Swimmer Tempus not found")
        return {}, {}
    html_renderer.click_element(driver, top_search)

    for event in swimmer_object.events:
        event_string = event.distance
## Test
# run("https://www.tempusopen.se/index.php?r=Swimmer", swimmer.Swimmer("Ian", "Hangård", "Simklubben Sydsim"), ["25m fjärilsim", "1500m frisim", "100m ryggsim", "200m medley"])