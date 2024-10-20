from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Scrapes the first page of quotes from https://quotes.toscrape.com/js (10 quotes in total) and saves them to a JSON file.

MAIN_URL = "https://quotes.toscrape.com/js"
driver = webdriver.Chrome() # <- this line is usually problematic, please please contact me if you can't open and navigate to a page with Selenium
driver.get(MAIN_URL)

# Let's find all boxes with quotes (all divs that have the class "quote")
quotes_divs = driver.find_elements(By.CSS_SELECTOR, "div.quote")
print(f"Found {len(quotes_divs)} quotes on the page.")
assert len(quotes_divs) > 0, "No quotes found on the page."
assert len(quotes_divs) == 10, f"Expected 10 quotes divs, found {len(quotes_divs)}."

result = []
for quote_div in quotes_divs:
    entry = {
        "quote": quote_div.find_element(By.CSS_SELECTOR, "span.text").text,
        "by": quote_div.find_element(By.CSS_SELECTOR, "span small.author").text,
        "tags": [tag.text for tag in quote_div.find_elements(By.CSS_SELECTOR, "div.tags a.tag")]
    }
    result.append(entry)

# Save the result to a JSON file
with open("01_nopagination_quotes.json", "w") as f:
    json.dump(result, f, indent=4)

driver.close()