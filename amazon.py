from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from bs4 import BeautifulSoup

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.amazon.com")
input("Press Enter to continue after logging in...")

URL = input('enter the url')
driver.get(URL)

wait = WebDriverWait(driver, 20)
review_section = wait.until(
    EC.presence_of_element_located((By.ID, 'cm_cr-review_list'))
)

reviews = []

# Define a function to scroll down the page
def scroll_page():
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, arguments[0]);", scroll_height)
    time.sleep(5)  # Wait for content to load

# Collect reviews and handle pagination
while True:
    soup = BeautifulSoup(driver.page_source, "lxml")
    review_divs = soup.find_all("div", {"data-hook": "review"})

    for review in review_divs:
        name = review.select_one('[class="a-profile-name"]').text.strip() if review.select_one('[class="a-profile-name"]') else 'N/A'
        stars = review.select_one('[data-hook="review-star-rating"]').text.strip() if review.select_one('[data-hook="review-star-rating"]') else 'N/A'
        title = review.select_one('[data-hook="review-title"]').text.strip() if review.select_one('[data-hook="review-title"]') else 'N/A'
        date = review.select_one('[data-hook="review-date"]').text.strip() if review.select_one('[data-hook="review-date"]') else 'N/A'
        description = review.select_one('[data-hook="review-body"]').text.strip() if review.select_one('[data-hook="review-body"]') else 'N/A'

        reviews.append({
            'Name': name,
            'Stars': stars,
            'Title': title,
            'Date': date,
            'Description': description
        })

    scroll_page()

    try:
        next_button = driver.find_elements(By.CSS_SELECTOR, "li.a-last a")
        if next_button and next_button[0].is_displayed():
            print("Next page button found, loading next page...")
            next_button[0].click()  # Go to the next page
            time.sleep(5)  # Wait for the next page to load
            scroll_page()  # Scroll to load more reviews
        else:
            print("No more pages, scraping done.")
            break
    except Exception as e:
        print(f"Error while moving to the next page: {e}")
        break

# Create a pandas DataFrame and save to CSV
df_reviews = pd.DataFrame(reviews)
print(df_reviews)  # Print reviews to verify they were scraped
df_reviews.to_csv('reviews.csv', index=False)

driver.quit()
