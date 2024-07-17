import swimmer
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# chrome_options = Options()
# chrome_options.add_argument("--headless=new") 
# driver = webdriver.Chrome(options = chrome_options)

driver = webdriver.Chrome()

url = "https://live.swimify.com/competitions/sum-sim-50m-2024-2024-07-10/events/entries/1/1"
driver.get(url)

# Wait until the button element is present
wait = WebDriverWait(driver, 20)

# # Find all buttons
# selector = 'button[class^="MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary"][tabindex][type="button"][role="tab"][aria-selected]'

# # Wait until at least one element matching the selector is present
# buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

# if buttons:
#     print(f"Found {len(buttons)} buttons:")
#     for i, button in enumerate(buttons):  
#         print(f"Button {i + 1}: {button.get_attribute('outerHTML')}")

# else:
#     print("No buttons found")


# Enter the "Swimmers" menu to locate the clubs 
try:
    # Wait for the button to be clickable
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.//p[contains(text(), "Swimmers")]]')))
    
    # Scroll into view if necessary
    driver.execute_script("arguments[0].scrollIntoView();", button)
    
    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", button)

    # Dictionary to store the club names and their corresponding WebElements
    club_elements = {}
    club_names    = []

    # Locate all the parent div elements containing the club information
    club_divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiBox-root.css-1eukt2p')))

    for club_div in club_divs:
        try:
            # Locate the club name within the parent div
            club_name_element = club_div.find_element(By.CSS_SELECTOR, 'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-1bpwwm7')
            club_name = club_name_element.text

            club_names.append(club_name)
            # Store the WebElement in the dictionary with the club name as the key
            club_elements[club_name] = club_div
        except Exception as e:
            print(f"Error processing club div: {e}")
finally:
    print("Search OK \n\n")

# # Output the dictionary
# for club_name, club_div in club_elements.items():
#     print(f"Club Name: {club_name}, WebElement: {club_div}")
print("Available clubs listed below. Enter index of club of interest.")
for i, name in enumerate(club_names):
    print(f'Club {i +  1}: ' + name)

def click_club_by_index(index):
    if 0 <= index < len(club_elements):
        print(f'Selected competition {index}: ' + club_names[index - 1])
        club_elements[club_names[index - 1]].click()
        print("Selected club clicked")
        return club_names[index - 1]
    else:
        print("Invalid index")
        return None
    
try:
    index_to_click = int(input("Enter the index of the competition to click: "))
    selected_club = click_club_by_index(index_to_click)
except ValueError:
    print("Please enter a valid integer index.")


# Dictionary to store the names and their corresponding WebElements
swimmer_div_dictionary = {}

# Locate all the parent div elements containing the names
swimmer_divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-1hbn5fk')))

for swimmer_div in swimmer_divs:
    try:
        # Locate the name within the parent div
        name_element = swimmer_div.find_element(By.CSS_SELECTOR, 'p.MuiTypography-root.MuiTypography-body1.MuiTypography-noWrap.css-lc08jz')
        name = name_element.text
        # Store the WebElement in the dictionary with the name as the key
        name_list = name.split()
        first_name = name_list[0]
        
        if 2 < len(name_list):
            last_name = name_list[1] + " " + name_list[2]
        else:
            last_name = name_list[-1]
        if not name == selected_club:
            swimmer_key = swimmer.Swimmer(first_name, last_name, selected_club)
            swimmer_div_dictionary[swimmer_key] = swimmer_div
        else:
            print("Relays not yet handled")

    except Exception as e:
        print(f"Error processing name div: {e}")

# Output the dictionary
for swimmer, swimmer_div in swimmer_div_dictionary.items():
    print(swimmer.to_string())
    swimmer_div.click()
    
    try:
        # Locate all the p elements with the given class
        # Locate the parent div elements with the specified class
        parent_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.MuiGrid-root.MuiGrid-container.MuiGrid-item.css-h9dk79')))
        
        for parent_element in parent_elements:
            # Locate the p element with the specific class within the parent element
            p_element = parent_element.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-2ijh4t > p.MuiTypography-root.MuiTypography-body1.css-151uy7p')
            # Extract the text content and add it to the list
            swimmer.add_event(p_element.text)
        swimmer.print_events()

    except Exception as e:
        print(f"No entries found. Error {e}")

input("Press Enter to cancel...")
driver.quit()