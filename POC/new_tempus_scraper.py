from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import driver_handler 
import html_renderer
import time

# Set up the Selenium WebDriver (assuming you have downloaded the Chrome WebDriver)
driver, wait = driver_handler.setup_driver("https://www.tempusopen.se/swimmers", 20)

# driver = driver = webdriver.Chrome() 
# driver.get("https://www.tempusopen.se/swimmers")
# Find the input elements by their 'name' attribute

first_name_input = html_renderer.find_element(wait, "first_name", By.NAME)
last_name_input = html_renderer.find_element(wait, "last_name", By.NAME)
club_input = html_renderer.find_element(wait, "club", By.NAME)

# Enter text in the fields
first_name_input.send_keys("Filip")
last_name_input.send_keys("Salbrink")
club_input.send_keys("Simklubben Poseidon")

# Find the submit button by its class or other unique properties
submit_button = html_renderer.find_element(wait, "//button[@type='submit' and contains(text(), 'Sök')]", By.XPATH)

# Click the submit button
html_renderer.click_element(driver, submit_button)


# Find the first <tr> element in the table
first_result_row = html_renderer.find_element(wait, "//tr[@class='even:bg-gray-50 odd:bg-white border-b border-gray-200'][1]", By.XPATH)

# Find the "Visa" link inside the first <tr> and click it
visa_link = html_renderer.find_sub_element(first_result_row, ".//a[@class='text-tempus-dark-blue']", By.XPATH)
html_renderer.click_element(driver, visa_link)

sample_list = ['25m Fjäril', '25m Ryggsim', '50m Frisim', '200m Medley', '1500m Frisim']

# Create dictionaries to store the found sample times
short_course_times = {}
long_course_times = {}
time.sleep(5)
# Find the div element that contains the "Kortbana (25m)" table using CSS Selector
[sc, lc] = html_renderer.find_all_elements(wait, "div > h5.font-semibold.text-xl.mb-2", By.CSS_SELECTOR)

# Check if the header is "Kortbana (25m)" and select the parent div
if sc.text == "Kortbana (25m)":
    parent_div = sc.find_element(By.XPATH, "./..")  # Select the parent <div> of the <h5>
    
    # Find all <tr> elements inside the table within this div
    rows = parent_div.find_elements(By.CSS_SELECTOR, "tr.even\\:bg-gray-50, tr.odd\\:bg-white")

    # List to store tuples of ['Sample string', 'Sample time']
    data_list = []

    for row in rows:
        # Find the first <td> and fourth <td> for 'Sample string' and 'Sample time'
        sample_string = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
        sample_time = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text

        # Append as tuple to the list
        data_list.append((sample_string, sample_time))

    # Print the list of tuples
    print(data_list)
else:
    print("Kortbana (25m) section not found!")

# Check if the header is "Långbana (50m)" and select the parent div
if lc.text == "Långbana (50m)":
    parent_div = lc.find_element(By.XPATH, "./..")  # Select the parent <div> of the <h5>
    
    # Find all <tr> elements inside the table within this div
    rows = parent_div.find_elements(By.CSS_SELECTOR, "tr.even\\:bg-gray-50, tr.odd\\:bg-white")

    # List to store tuples of ['Sample string', 'Sample time']
    data_list = []

    for row in rows:
        # Find the first <td> and fourth <td> for 'Sample string' and 'Sample time'
        sample_string = row.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
        sample_time = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
        sample_date = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
        sample = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        print(row.text)
        # Append as list to the list
        data_list.append([sample_string, sample_time, sample_date, sample])

    # Print the list of tuples
    print(data_list)
else:
    print("Långbana (50m) section not found!")
# Optionally, you can close the browser after interaction
driver.quit()
