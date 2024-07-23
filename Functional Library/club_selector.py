from selenium.webdriver.common.by import By

import time
import driver_handler
import html_renderer


def run(url):
    ##____ Set up the Chrome WebDriver ____##
    driver, wait = driver_handler.setup_driver(\
        url, 20)
    
    club_url = select_club(driver, wait)

    # Wait for closure
    driver.quit()
    return club_url

##____ Choose competition section depending on input ____##
def choice_index(list_of_choices):
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
    ##____ Enter the "Swimmers" menu to locate the clubs ____#
    try:
        # Wait for the button to be clickable
        button = html_renderer.find_element(wait, '//button[.//p[contains(text(), "Swimmers")]]', By.XPATH)
        
        # Click the button using JavaScript
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)

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
        choice = choice_index(club_names)
        club_div_map[club_names[choice]].click()

        print("Found Club URL: " + driver.current_url)

        return club_names[choice], driver.current_url

    except Exception as e:
        print(f'Error: {e}')

## Test  
# run("https://live.swimify.com/competitions/smpara-smjsm-50m-2024-2024-07-03/events/summary/1/146")