from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Sample list of strings to search for
sample_list = ['25m Fjäril', '25m Ryggsim', '50m Frisim', '200m Medley', '1500m Frisim']

# Set up the Selenium WebDriver (assuming you have downloaded the Chrome WebDriver)
driver = webdriver.Chrome()  # or use `webdriver.Firefox()` if using Firefox

# Open the webpage (after form submission and navigating to the results page)
driver.get("https://www.tempusopen.se/swimmers")  # Replace with the actual URL

# Give the page some time to load
time.sleep(5)

# Create dictionaries to store the found sample times
result_times = {
    "Kortbana (25m)": None,
    "Långbana (50m)": None
}

# Search in the Kortbana (25m) div
kortbana_div = driver.find_element(By.XPATH, "//h5[text()='Kortbana (25m)']/following-sibling::div")
kortbana_rows = kortbana_div.find_elements(By.XPATH, ".//tr")

for row in kortbana_rows:
    # Find the SAMPLE STRING (first <td>) and SAMPLE TIME (fourth <td>) in each row
    sample_string = row.find_element(By.XPATH, ".//td[1]").text
    sample_time = row.find_element(By.XPATH, ".//td[4]").text

    # If the sample string matches any string in the sample_list, store the time
    if sample_string in sample_list:
        result_times["Kortbana (25m)"] = sample_time
        break  # Since we only want one match per div, we break after finding the first match

# Search in the Långbana (50m) div
langbana_div = driver.find_element(By.XPATH, "//h5[text()='Långbana (50m)']/following-sibling::div")
langbana_rows = langbana_div.find_elements(By.XPATH, ".//tr")

for row in langbana_rows:
    # Find the SAMPLE STRING (first <td>) and SAMPLE TIME (fourth <td>) in each row
    sample_string = row.find_element(By.XPATH, ".//td[1]").text
    sample_time = row.find_element(By.XPATH, ".//td[4]").text

    # If the sample string matches any string in the sample_list, store the time
    if sample_string in sample_list:
        result_times["Långbana (50m)"] = sample_time
        break  # Since we only want one match per div, we break after finding the first match

# Output the results
print("Sample times found:")
print(result_times)

# Optionally, close the browser after the interaction
driver.quit()
