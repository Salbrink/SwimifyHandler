import time
import event
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless=new") 
driver = webdriver.Chrome(chrome_options)

#url = "https://live.swimify.com/competitions/sum-sim-50m-2024-2024-07-10/events/entries/1/1"
url = "https://live.swimify.com/competitions/smpara-smjsm-50m-2024-2024-07-03/events/summary/1/146"
driver.get(url)

# Wait until the root element is present
wait = WebDriverWait(driver, 20)
root_div = wait.until(EC.presence_of_element_located((By.ID, "root")))

selector = 'div[class="MuiBox-root css-qlbhet"]'

session_divs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

# Dictionary for session web elements
sessions = {}

# Find and store all session elements with keys of type "session x | day h:m
for session_div in session_divs:
    ## Find the name strings
    session_name_element = session_div.find_element(By.CSS_SELECTOR, 'p.MuiTypography-root.MuiTypography-body1.css-xu169k')
    session_time_element  = session_div.find_elements(By.CSS_SELECTOR, 'p.MuiTypography-root.MuiTypography-body1.css-bxnpil')
    
    session_name = session_name_element.text + " | " + session_time_element[0].text + " " + session_time_element[-1].text
    sessions[session_name] = session_div

# Dictionary for events per session
session_events = {}
session_event_lists = []

# For all sessions, load all events
for session in sessions:

    sessions[session].click()
    time.sleep(1)
    print(session)

    session_event_list = []

    try:
        # Locate all <a> elements with the specific style
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@display='flex']")))

        for element in elements:
            # Extract the time
            start_time = element.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-z9ki6v > p').text.strip()
            
            # Extract the event
            session_event = element.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-6771j6 > p').text.strip()
            
            # Add the extracted time and event to the list
            session_events[session] = [start_time, session_event]

            session_event_list.append(event.Event(session_event))

            # Output the list of times and events
            print("\t" + session_events[session][0] + " " + session_events[session][1])
            session_event_lists.append(session_event_list)

    except Exception as e:
        print(f"An error occurred: {e}")
 
input("Press Enter to cancel...")
driver.quit()