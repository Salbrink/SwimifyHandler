from selenium.webdriver.common.by import By

import driver_handler
import html_renderer

##____ Set up the Chrome WebDriver ____##
driver, wait = driver_handler.setup_driver("https://live.swimify.com", 20)

##____ Choose competition seciton depending on input ____##
def choice_index(list_of_choices):
    choice_index = -1
    last_index   = len(list_of_choices) - 1
    while ((choice_index < 0) or (last_index < choice_index)):
        try:
            if last_index < choice_index: 
                print("Not a valid input\n\n") 
                choice_index = -1
            else: 
                choice_index = int(input("Enter index to click: ")) - 1
        except ValueError:
            print("Please enter a valid integer index.\n\n")
    

    print(f'Selected {choice_index + 1}: {list_of_choices[choice_index]}')
    return choice_index

def select_section():
    ##____ Find sections Competitions This Week, Upcoming Competitions and Finished Competititons  ____##

    # Define the CSS selector for section div elements
    competition_section_divs_selector = 'div[class^="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 "]'

    # Get all competition section div elements
    competition_section_divs = html_renderer.find_all_elements(wait, \
                                competition_section_divs_selector, By.CSS_SELECTOR)

    ##____ Find and print the titles of WebElements ____##

    # Define the CSS selector for title p elements
    title_element_selector = 'p[class^="MuiTypography-root MuiTypography-body1 css-"]'
    title_elements = []

    for i, comp_sec in enumerate(competition_section_divs):

        # Get and store the title string
        title_element = html_renderer.find_sub_element(comp_sec, title_element_selector, By.CSS_SELECTOR).text
        title_elements.append(title_element)
        print(f'{i + 1} ' + title_element)

    index = choice_index(title_elements)
    selected_section = competition_section_divs[index]
    return selected_section, index + 1

def select_competition(section, index):
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

    for i, comp_title in enumerate(competition_list):
        print(f'{i + 1} ' + comp_title)

    ##____ Choose competition seciton depending on input ____##
    choice = choice_index(competition_list)

    # Get and click selected competition
    selected_competition = competition_list[choice]
    competition_div_map[selected_competition].click()


section, index = select_section()
select_competition(section, index)

##________##
input("Press Enter to cancel...")
driver.quit()