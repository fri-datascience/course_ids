from selenium import webdriver
from selenium.webdriver.common.by import By
import json

# Navigate to https://quotes.toscrape.com/ and print the first quote and its author and tags.

MAIN_URL = "https://quotes.toscrape.com/"
driver = webdriver.Chrome() # <- this line is usually problematic, please please contact me if you can't open and navigate to a page with Selenium
driver.get(MAIN_URL)

# Find boxes with quotes (all divs that have the class "quote")
divs = driver.find_elements(By.CSS_SELECTOR, "div.quote")
# Failsafe checks (we know there are exactly 10 quotes on the page and that's what we expect Selenium to find)
assert len(divs) > 0, "No quotes found on the page."
assert len(divs) == 10, f"Expected 10 quotes divs, found {len(divs)}."
print(f"Found {len(divs)} quotes on the page.")

# Let's print the HTML of the first quote div
print("HTML of the first quote div:")
print(divs[0].get_attribute("outerHTML"))
quote_div = divs[0]
quote = quote_div.find_element(By.CSS_SELECTOR, "span.text").text
author = quote_div.find_element(By.CSS_SELECTOR, "span small.author").text
tags = quote_div.find_elements(By.CSS_SELECTOR, "div.tags a.tag")
print(f"Quote: {quote}")
print(f"Author: {author}")
print("Tags:")
for tag in tags:
    print(tag.text)

# Save the quote, author, and tags to a JSON file
with open("demo.json", "w") as f:
    json.dump({
        "quote": quote,
        "by": author,
        "tags": [tag.text for tag in tags]
    }, f, indent=4)
