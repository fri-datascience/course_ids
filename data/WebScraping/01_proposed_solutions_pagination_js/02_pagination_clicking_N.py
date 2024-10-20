from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Scrapes N_PAGES_TO_SCRAPE pages of quotes from https://quotes.toscrape.com/js (10 quotes in total) and saves them to a JSON file.


MAIN_URL = "https://quotes.toscrape.com/js"
print(f"Scraping URL: {MAIN_URL}")
N_PAGES_TO_SCRAPE = 5

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
for i in range(N_PAGES_TO_SCRAPE - 1):
    final_result.extend(parse_one_page(driver)) # the first page is already loaded (driver.get(MAIN_URL))
    # Find and click the "Next" button
    next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
    print(f"Scraping URL: {next_button.get_attribute('href')}")
    next_button.click()

# Save the result to a JSON file
with open("02_pagination_clicking_N_quotes.json", "w") as f:
    json.dump(final_result, f, indent=4)

driver.close()