from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument("--headless=new") 

url = "https://live.swimify.com/competitions/sum-sim-50m-2024-2024-07-10/events/entries/1/1"
driver.get(url)

# Wait until the root element is present
wait = WebDriverWait(driver, 20)
root_div = wait.until(EC.presence_of_element_located((By.ID, "root")))


## Find all buttons
# selector = 'button[class^="MuiButtonBase-root MuiTab-root MuiTab-textColorPrimary"][tabindex][type="button"][role="tab"][aria-selected]'

# Wait until at least one element matching the selector is present
# buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

# if buttons:
#     print(f"Found {len(buttons)} buttons:")
#     for i, button in enumerate(buttons):
#         print("Start")
#         print(f"Button {i + 1}: {button.get_attribute('outerHTML')}")
#         print("Stop")

# else:
#     print("No buttons found")

selector = 'div[class="MuiBox-root css-qlbhet"]'

sessions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

if sessions:
    print(f"Found {len(sessions)} buttons:")
    for i, session in enumerate(sessions):
        print("Start")
        print(f"Button {i + 1}: {session.get_attribute('outerHTML')}")
        print("Stop")

else:
    print("No buttons found")

input("Press Enter to continue...")
driver.quit()