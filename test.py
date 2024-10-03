from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

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
driver.get("https://www.ycombinator.com/companies")
print(driver.title)

# Close the driver
driver.quit()
