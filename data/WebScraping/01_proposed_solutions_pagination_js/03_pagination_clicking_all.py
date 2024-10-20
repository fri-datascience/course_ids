from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json

# Scrapes all pages of quotes from https://quotes.toscrape.com/js and saves them to a JSON file.

MAIN_URL = "https://quotes.toscrape.com/js"
print(f"Scraping URL: {MAIN_URL}")

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

final_result = []
while True:
    final_result.extend(parse_one_page(driver)) # the first page is already loaded (driver.get(MAIN_URL))
    # Try to find the "Next" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        print(f"Scraping URL: {next_button.get_attribute('href')}")
        next_button.click()
    except NoSuchElementException:
        break # no more pages to scrape, break the infinite loop

# Save the result to a JSON file
with open("03_pagination_clicking_all_quotes.json", "w") as f:
    json.dump(final_result, f, indent=4)

driver.close()