import time
import swimmer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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
wait = WebDriverWait(driver, 20)
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

# Close the WebDriver after the action
input("Press Enter to cancel...")
driver.quit()
