import argparse

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from bs4 import BeautifulSoup
import pandas as pd


parser = argparse.ArgumentParser(description="Scrape companies from Y Combinator")
parser.add_argument("scroll_count", type=int, help="Number of times to scroll down the page")
args = parser.parse_args()

URL = "https://www.ycombinator.com/companies"
SLEEP = 5

# Set up the options for Firefox
options = Options()
options.binary_location = "/usr/bin/firefox"  # Update this path if needed
options.add_argument("--headless")  # Run in headless mode
options.log.level = "trace"  # Enable verbose logging

# Set up the Firefox WebDriver with the Service class
service = Service(GeckoDriverManager().install())

print("Starting Firefox...")
driver = webdriver.Firefox(service=service, options=options)
print("Firefox started successfully.")

# Now you can use driver to interact with web pages
driver.get(URL)

print("Entered website, loading compaines")
for i in range(args.scroll_count):
    print(f"Loaded page : {i+1}")
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

    time.sleep(SLEEP)


print("Scraping Website")
html = driver.page_source

# Close the driver
driver.quit()


soup = BeautifulSoup(html, 'html.parser')

company_details = []

print("Extracting sections")
for element in soup.find_all('a', class_="_company_86jzd_338"):
    title = element.find('span', class_="_coName_86jzd_453").text  # Get company description
    description = element.find('span', class_="_coDescription_86jzd_478").text
    location = element.find('span', class_="_coLocation_86jzd_469").text  # Get company location
    # Ensure we are only getting tags related to the current company
    tags = ",".join([tag.text for tag in element.find_all('span', class_="pill _pill_86jzd_33") if tag])  # Filter to ensure only valid tags are included
    company_details.append([title, description, location, tags])

print("Converting to csv")
df = pd.DataFrame(company_details,
                  columns=["name", "Description", "Location", "tags"])

for col in df.columns:
    df[col] = df[col].astype(str)

print(df.dtypes)

df.to_csv("companies.csv", index=False)
