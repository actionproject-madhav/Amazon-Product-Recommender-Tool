from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up WebDriver in non-headless mode to see if it's working
options = webdriver.ChromeOptions()
# Comment out headless mode so that the browser opens visibly
# options.add_argument('--headless')  # Uncomment this line to hide the browser

# Install the driver automatically using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a simple URL to see if it loads
driver.get('https://www.google.com')

# Wait for a while to make sure the page loads
time.sleep(5)

# Close the driver after check
driver.quit()
