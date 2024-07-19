from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument("--headless=new") 

url = "https://live.swimify.com"
driver.get(url)

# Wait until the root element is present
wait = WebDriverWait(driver, 20)
# root_div = wait.until(EC.presence_of_element_located((By.ID, "root")))

# Define the CSS selector for the desired elements
selector = 'div[class^="MuiBox-root css-"][role="article"][aria-labelledby^="competition-title-"]'

# Wait until at least one element matching the selector is present
competitions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

# Lists to store competition titles and clickable elements
competition_titles = []
clickable_elements = []

# Check if competitions were found
if competitions:
    print(f"Found {len(competitions)} competitions:")
    for i, competition in enumerate(competitions):
        # Find the specific child <p> element with the competition title
        title_element = competition.find_element(By.CSS_SELECTOR, 'p[class="MuiTypography-root MuiTypography-body1 MuiTypography-noWrap css-1nn2qy0"]')
        if title_element:
            title = title_element.text
            competition_titles.append(title)
            
            # Assuming the clickable element is the competition container itself or a specific child element
            clickable_element = competition  # Might need to be adjusted based on actual clickable element
            clickable_elements.append(clickable_element)
            print(f"Competition {i + 1}: {title}")
else:
    print("No competitions found")

# Function to click on a competition based on its index
def click_competition_by_index(index):
    if 0 <= index - 1 < len(clickable_elements):
        clickable_elements[index - 1].click()
        print(f"Clicked on competition {index}: {competition_titles[index - 1]}")
    else:
        print("Invalid index")

# Example usage: Click on the competition with the specified index
try:
    index_to_click = int(input("Enter the index of the competition to click: "))
    click_competition_by_index(index_to_click)
except ValueError:
    print("Please enter a valid integer index.")

# Close the WebDriver after the action
input("Press Enter to cancel...")
driver.quit()

