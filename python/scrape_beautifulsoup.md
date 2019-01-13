# Simple scraping using beautifulsoup4 python
Here's the skeleton code:
```python
import bs4
import requests

url = "www.something.com"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text, "html.parser")
rows = soup.findAll("td", {'class': "colomn_border"})
# rows is a list of soup objects all matches
# something = soup.findAll("html_tag", {"attribute : "value"})
row = soup.find("td")
# row is a single soup object which is the first match
row.value #It's the value between tags

# finding all urls
for a in soup.find_all('a', href=True):
    print(f"Found the URL: {a['href']}")
```

**Note: ** Websites that load dynamically can not be scraped with bs4, use selenium for that. It's simple too.

