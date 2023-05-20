import datetime

from bs4 import BeautifulSoup, Tag
from data_processing import save_to_json
from utils import safe_parsing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def parse(*args, **kwargs):
    base_url = "https://www.vegrecipesofindia.com/recipes/?fwp_recipe_cuisines=indian"

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode to avoid opening a browser window
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the Chrome driver executable path (update it to match your system)
    webdriver_service = Service(ChromeDriverManager().install())

    try:
        # Launch the Chrome browser with the configured options
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    except Exception as err:
        print("Encountered an exception!")
        raise err
    
    # Navigate to the URL
    driver.get(base_url)

    # Use explicit wait to wait for recipe elements to load
    wait = WebDriverWait(driver, 20)

    # Get the page source (which will contain the dynamically generated content)
    page_source = driver.page_source
    driver.quit() # close driver
    
    recipes = extract(page_source)
    save_to_json(recipes)
    print(recipes)

def extract(page_source) -> dict:
    # Use BeautifulSoup to parse the page source and extract the data you need
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract elements
    recipe_articles = soup.find_all('article', class_='post-summary primary')

    new_data = {}
    for index, article in enumerate(recipe_articles):
        if index < 250:
            new_data[index] = parse_result(article)
    return new_data

def parse_result(article) -> dict:
    recipe_data = {}

    recipe_data["crawled_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    recipe_data["name"] = safe_parsing(article.find('h3', class_='post-summary__title'))
    recipe_data["category"] = safe_parsing(article.find('p', class_='entry-category'))
    recipe_data["prep_time"] = safe_parsing(article.find('span', class_='wprm-recipe-time wprm-block-text-bold'))
    recipe_data["difficulty"] = safe_parsing(article.find('span', class_='wprm-recipe-difficulty wprm-block-text-bold'))
    recipe_data["href"] = safe_parsing(article.find('a', href=True).get('href'))
    recipe_data["image"] = safe_parsing(article.find('img').get('src'))

    return recipe_data
