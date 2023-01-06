from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.indianhealthyrecipes.com/dal-makhani-recipe/')

# when some websites don't work
#scraper = scrape_me('https://...', wild_mode=True)

scraper.title()
scraper.total_time()
scraper.yields()
scraper.ingredients()
scraper.instructions()  # or alternatively for results as a Python list: scraper.instructions_list()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available

# Starting from version 14.0.0 you also have an option to scrape from html-like content
import requests
from recipe_scrapers import scrape_html



url = "https://www.indianhealthyrecipes.com/dal-makhani-recipe/"
html = requests.get(url).content

scraper = scrape_html(html=html, org_url=url)

p= scraper.title()
scraper.total_time()
scraper.yields()
s = scraper.ingredients()
scraper.instructions()  # or alternatively for results as a Python list: scraper.instructions_list()
scraper.image()
scraper.host()
scraper.links()
n = scraper.nutrients()  
# etc...
print(p)
print(s) 
print(n)  
