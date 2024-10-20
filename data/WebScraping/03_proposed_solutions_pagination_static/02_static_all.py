from bs4 import BeautifulSoup
import requests
import json

# We saved the links to pages of quotes in a file called "links.txt", so we can read it line by line and scrape each URL with requests and BeautifulSoup.

links = []
with open("links.txt") as f:
    links = f.read().splitlines()

print(links)

result = []
for link in links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    # Let's find all boxes with quotes (all divs that have the class "quote")
    quotes_divs = soup.select("div.quote")
    print(f"Found {len(quotes_divs)} quotes on {link}.")
    assert len(quotes_divs) > 0, "No quotes found on the page."
    assert len(quotes_divs) == 10, f"Expected 10 quotes divs, found {len(quotes_divs)}."

    for quote_div in quotes_divs:
        entry = {
            "quote": quote_div.select_one("span.text").text,
            "by": quote_div.select_one("span small.author").text,
            "tags": [tag.text for tag in quote_div.select("div.tags a.tag")]
        }
        result.append(entry)

# Save the result to a JSON file
with open("02_static_all_quotes.json", "w") as f:
    json.dump(result, f, indent=4)

