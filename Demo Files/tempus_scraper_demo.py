import time
import swimmer

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument("--headless=new") 

# Set up the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.tempusopen.se/index.php?r=Swimmer"
driver.get(url)

# Wait until the input element is present
wait = WebDriverWait(driver, 20)

# Create sample swimmer
sample_swimmer = swimmer.Swimmer("Filip", "Salbrink", "Simklubben Poseidon")

# Find search bars
first_name = wait.until(EC.presence_of_element_located((By.ID, "Swimmer_first_name")))
last_name  = wait.until(EC.presence_of_element_located((By.ID, "Swimmer_last_name")))
club_name  = wait.until(EC.presence_of_element_located((By.ID, "Swimmer_swimmer_club")))

# Interact with the input elements
if first_name:
    first_name.send_keys(sample_swimmer.first_name)
    print("First name element found and text entered.")
else:
    print("First name element not found.")

if last_name:
    last_name.send_keys(sample_swimmer.last_name)
    print("Last name element found and text entered.")
else:
    print("Last name element not found.")

if club_name:
    club_name.send_keys(sample_swimmer.club)
    print("Club name element found and text entered.")
else:
    print("Club name not found")

# Search swimmer and enter page

# Find and click search button
selector = 'input[type="submit"][name="yt0"][value="Sök"]'
button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

if button:
    button.click()
    print("Search button found and pressed")
else:
    print("Search button not found")

time.sleep(1)

# Wait until the desired row is present
row_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tr.odd td.name-column')))

# Locate the <a> tag with class "view" within the specific row
# Using XPath to locate the specific <a> tag with class "view"
view_link = wait.until(EC.presence_of_element_located((By.XPATH, '//tr[@class="odd"]//a[@class="view"]')))


# Trigger the click event
if view_link:
    view_link.click()
    print("Clicked on the 'view' link.")
else:
    print("View link not found.")


#### This will be input from other classes 

# Predefined list of events
events = ["25m fjärilsim", "1500m frisim", "100m ryggsim", "200m medley"]  # Example list
print("Events of interest:")
for event in events:
    print("\t" + event)
#####

## Create a dictionary to store all events with the short course PB and 
## date of race
short_course_map = {}


## Locate all elements of interest in the tempus html page
try:
    # Locate the header for Kortbana (25m)
    kortbana_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Kortbana (25m)']")))
    
    # Find the table following the Kortbana header
    kortbana_table = kortbana_header.find_element(By.XPATH, "following-sibling::div[@class='grid-view']/table")

    # Locate all table rows of the specified type (both odd and even) within the Kortbana table
    table_rows = kortbana_table.find_elements(By.CSS_SELECTOR, 'tbody tr.odd, tbody tr.even')
    
    for row in table_rows:
        # Find the event name cell and extract the event name
        event_name_cell = row.find_element(By.CSS_SELECTOR, 'td.name-column')
        event_name = event_name_cell.text.split('\n')[0].strip().lower()
        
        # Check if the event name is in the predefined list
        if event_name in events:
            # Extract the date and time from the respective cells
            date = row.find_elements(By.TAG_NAME, 'td')[2].text.strip()
            time = row.find_elements(By.TAG_NAME, 'td')[3].text.strip()
            
            # Add the date and time as a tuple to the list
            short_course_map[event_name] = (date, time)
    
    # Output the list of event details
    print("Short Course Details List:", short_course_map)

except Exception as e:
    print(f"An error occurred: {e}")


#### Same thing for longcourse
long_course_map = {}

try:
    # Locate the header for Långbana (50m)
    kortbana_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Långbana (50m)']")))
    
    # Find the table following the Kortbana header
    kortbana_table = kortbana_header.find_element(By.XPATH, "following-sibling::div[@class='grid-view']/table")

    # Locate all table rows of the specified type (both odd and even) within the Kortbana table
    table_rows = kortbana_table.find_elements(By.CSS_SELECTOR, 'tbody tr.odd, tbody tr.even')
    
    for row in table_rows:
        # Find the event name cell and extract the event name
        event_name_cell = row.find_element(By.CSS_SELECTOR, 'td.name-column')
        event_name = event_name_cell.text.split('\n')[0].strip().lower()
        
        # Check if the event name is in the predefined list
        if event_name in events:
            # Extract the date and time from the respective cells
            date = row.find_elements(By.TAG_NAME, 'td')[2].text.strip()
            time = row.find_elements(By.TAG_NAME, 'td')[3].text.strip()
            
            # Add the date and time as a tuple to the list
            long_course_map[event_name] = [date, time]
    
    # Output the list of event details
    print("Long Course Details List:", long_course_map)

except Exception as e:
    print(f"An error occurred: {e}")

####

## Printing events with personal best times:
print(sample_swimmer.to_string())

for event in events:
    try:
        print("\t" + event + " PB Short course: " + short_course_map[event][1] + " date " + short_course_map[event][0])    
    except KeyError:
        print("\tNo personal best for " + event + " Sc")

    try:
        print("\t" + event + " PB Long course: " + long_course_map[event][1] + " date " + long_course_map[event][0])    
    except KeyError:
        print("\tNo personal best for " + event + " LC")

# Close the WebDriver after the action
input("Press Enter to cancel...")
driver.quit()
