## Web scraping demo

We will be scraping quotes from a site specifically prepared for learning web scraping. Conveniently the site has multiple versions requiring different scraping techniques:
1. https://quotes.toscrape.com/js (A dynamic Javascript (JS) website, Selenium is needed as JS loads the quotes, 10 quotes per page, 10 pages total.)
2. https://quotes.toscrape.com/scroll (A dynamic JS website, quotes are loaded in batches by scrolling to the bottom, Selenium is needed.)
3. https://quotes.toscrape.com/ (A static version of the website, 10 quotes per page, 10 pages total. Selenium is not needed.)

There are 100 quotes total. The above links only differ by how the data (quotes) are loaded. Even the quotes are the same and in the same order.

**The solutions for sources 1. 2. and 3. are available in the correspondingly numbered folders in this repo.**

The results, regardless of the method used for scraping should be saved as a JSON file, containing all 100 quotes:

```json
[
    {
        "quote": "\u201cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.\u201d",
        "by": "Albert Einstein",
        "tags": [
            "change",
            "deep-thoughts",
            "thinking",
            "world"
        ]
    },

    {
        "quote": "\u201cThere are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\u201d",
        "by": "Albert Einstein",
        "tags": [
            "inspirational",
            "life",
            "live",
            "miracle",
            "miracles"
        ]
    },
    ...
   {
        "quote": "\u201c... a mind needs books as a sword needs a whetstone, if it is to keep its edge.\u201d",
        "by": "George R.R. Martin",
        "tags": [
            "books",
            "mind"
        ]
    }
]
```



The Python environment can be reproduced with conda from the `environment.yml` file in this repository:
```
conda env create -f environment.yml
conda activate idswebscraping
```

or from scratch with conda:
```
conda create -n idswebscraping python=3.12 selenium beautifulsoup4 requests -c conda-forge
conda activate idswebscraping
```

or with pip (recommended to make a virtual environment with venv first)
```
pip install selenium requests beautifulsoup4
```
