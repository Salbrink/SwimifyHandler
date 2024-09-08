from selenium.webdriver.common.by import By

import driver_handler
import html_renderer

####______________________________________________________________________________________________________####

'''

The following serves as a library for initially scraping information of live.Swimify.com and from there 
select competition from either of the sections

- Competitions this week
- Upcoming competitions
- Finished competitions

'''

####______________________________________________________________________________________________________####

def run(url):
    '''
    Demo run of class. Takes the url of the Swimify competition
    and runs through all essential functions of class

    Input:
        url: url adress of competition
    '''
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(url, 20)
    
    section, index = select_section(wait)
    competition_url = select_competition(driver, section, index)

    ##________##
    driver.quit()
    return competition_url

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

def select_section(wait):
    '''
    Function to select one of the sections

    - Competitions this week
    - Upcoming competitions
    - Finished competitions

    from the main menu of live.swimify.com.

    Input:
        wait: active selenium.webdriver.WebdriverWait object
    
    Return:
        html clickable div element of section of choice
        index 1,2 or 3 of the section of choice
    '''
    ##____ Find sections "Competitions This Week", "Upcoming Competitions" and "Finished Competititons"  ____##

    # Define the CSS selector for section div elements
    competition_section_divs_selector = 'div[class^="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 "]'

    # Get all competition section div elements
    competition_section_divs = html_renderer.find_all_elements(wait, \
                                competition_section_divs_selector, By.CSS_SELECTOR)

    ##____ Find and print the titles of WebElements ____##

    # Define the CSS selector for title p elements
    title_element_selector = 'p[class^="MuiTypography-root MuiTypography-body1 css-"]'
    title_elements = []

    print("\nSelect section:")
    for i, comp_sec in enumerate(competition_section_divs):
        # Get and store the title string
        title_element = html_renderer.find_sub_element(comp_sec, title_element_selector, By.CSS_SELECTOR).text
        title_elements.append(title_element)
        print(f'\t{i + 1} ' + title_element)

    index = _choice_index(title_elements)
    selected_section = competition_section_divs[index]
    return selected_section, index + 1

def select_competition(driver, section, index):
    '''
    Function to find all competitions in a given section and
    allow input choice from the terminal to select a competition of interest.

    Input:
        driver: active selenium.webdriver object
        section: clickable div eelement of chosen section

    Return:
        url of competition
    '''
    ##____ Find all competitions in chosen section ____##

    # Define the CSS selector for competition clickable elements
    match index: 
        case 1:
            competition_divs_selector = 'div[class^="MuiBox-root css-"][role="article"][aria-labelledby^="competition-title-"]'
        case 2: 
            competition_divs_selector = "div.MuiGrid-root.MuiGrid-container.MuiGrid-wrap-xs-nowrap.css-3s91ag"
        case 3:
            competition_divs_selector = "div.MuiGrid-root.MuiGrid-container.MuiGrid-wrap-xs-nowrap.css-3s91ag"
        case _:
            print("Error: Not a Valid Choice of Section")

    # Get all competition div elements
    competitions = html_renderer.find_all_sub_elements(section, competition_divs_selector, By.CSS_SELECTOR)

    # Define the CSS selector for title p elements
    title_element_selector = 'p[class^="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-"]'

    # Get all competition titles and clickable elements
    competition_list, competition_div_map = html_renderer.get_all_strings(competitions, \
                                                title_element_selector, By.CSS_SELECTOR)

    print("\nSelect competition:")
    for i, comp_title in enumerate(competition_list):
        print(f'\t{i + 1} ' + comp_title)

    ##____ Choose competition seciton depending on input ____##
    choice = _choice_index(competition_list)

    # Get and click selected competition
    selected_competition = competition_list[choice]
    html_renderer.click_element(driver, competition_div_map[selected_competition])

    print("Found Competition URL: " + driver.current_url)

    return driver.current_url

## Test
# run("https://live.swimify.com")