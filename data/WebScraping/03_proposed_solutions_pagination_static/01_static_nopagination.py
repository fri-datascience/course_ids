from bs4 import BeautifulSoup
import requests
import json

# Same as 01_proposed_solutions_static/01_nopagination.py but without Selenium, we are working with a static site, so BeautifulSoup and requests are enough.
# Selenium is not needed because the site doesn't need JS to load the quotes.

MAIN_URL = "https://quotes.toscrape.com"
response = requests.get(MAIN_URL)
soup = BeautifulSoup(response.text, "html.parser")

# Let's find all boxes with quotes (all divs that have the class "quote")
quotes_divs = soup.select("div.quote")
print(f"Found {len(quotes_divs)} quotes on the page.")
assert len(quotes_divs) > 0, "No quotes found on the page."
assert len(quotes_divs) == 10, f"Expected 10 quotes divs, found {len(quotes_divs)}."

result = []
for quote_div in quotes_divs:
    entry = {
        "quote": quote_div.select_one("span.text").text,
        "by": quote_div.select_one("span small.author").text,
        "tags": [tag.text for tag in quote_div.select("div.tags a.tag")]
    }
    result.append(entry)

# Save the result to a JSON file
with open("01_static_nopagination_quotes.json", "w") as f:
    json.dump(result, f, indent=4)

