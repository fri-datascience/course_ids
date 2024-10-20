from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

# Scrapes all quotes on https://quotes.toscrape.com/scroll (infinite scroll) and saves them to a JSON file.
# Same as 01_infinitescroll_naive.py, but this one is better because it checks if any new quotes were loaded after scrolling to the bottom of the page.

MAIN_URL = "https://quotes.toscrape.com/scroll"

def parse_one_page(driver):
    # Let's find all boxes with quotes (all divs that have the class "quote")
    quotes_divs = driver.find_elements(By.CSS_SELECTOR, "div.quote")
    assert len(quotes_divs) > 0, "No quotes found on the page."

    result = []
    for quote_div in quotes_divs:
        entry = {
            "quote": quote_div.find_element(By.CSS_SELECTOR, "span.text").text,
            "by": quote_div.find_element(By.CSS_SELECTOR, "span small.author").text,
            "tags": [tag.text for tag in quote_div.find_elements(By.CSS_SELECTOR, "div.tags a.tag")]
        }
        result.append(entry)

    return result

driver = webdriver.Chrome()
driver.get(MAIN_URL)
sleep(1) # wait for the quotes to load in

# load everything by scrolling to the bottom and checking if any new quotes were loaded
while True:
    # scroll to the bottom of the page
    previous_num_quotes = len(driver.find_elements(By.CSS_SELECTOR, "div.quote"))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    # check if the number of quotes has changed (if not, we've loaded everything)
    current_num_quotes = len(driver.find_elements(By.CSS_SELECTOR, "div.quote"))
    if current_num_quotes == previous_num_quotes:
        break

# Since everything is loaded, but on one page, we can parse it all at once
final_result = parse_one_page(driver)
print(f"Scraped {len(final_result)} quotes.")

# Save the result to a JSON file
with open("02_infinitescroll_better_quotes.json", "w") as f:
    json.dump(final_result, f, indent=4)

driver.close()