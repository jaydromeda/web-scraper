import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup 
import csv
import datetime

# Function to scrape Amazon
def scrape_amazon():
    # Path to chromedriver.exe
    DRIVER_PATH = '/path/to/chromedriver.exe'

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Start the WebDriver and create a new session
    with webdriver.Chrome(service=Service(DRIVER_PATH), options=chrome_options) as driver:
        # Load the page
        driver.get("https://www.amazon.com/Dog-Man-Scarlet-Shedder-Underpants/dp/1338896431/ref=mp_s_a_1_1?dib=eyJ2IjoiMSJ9.oFFW3RrIceLIoA20KpxG_dbVUgO8xhy1uCox0KPdS07SP0KC9uxQSX9vTKs8kWL9W_fM1W7TGP9b5LWxvMcgnAGutrwhsUTj8zBMep14BcDnHtgmRT_5EkH1KvzliZBIBxz-dvCsnBT5eY1sYf1O6pQn_EmI2IbL4EoNBWVnkeUqUhfSKuhg89WU0YAm22WHIUeXFuuPqbV49nF5xlzRdw.yPqPJ0B8Hi2FNHvqoBLtZ5lx7J-E31e8kxkQoJn1zrU&dib_tag=se&qid=1713993245&s=books&sr=1-1&srs=17143709011")

        # Wait for the page to load
        time.sleep(5)

        # Get page source
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find title and price elements
        title = soup.find("span", id="productTitle").get_text().strip()
        price = soup.find("span", class_="a-price-whole").get_text().strip()

        # Clean up the data
        price = price.strip()[1:]

        # Create a Timestamp for your output to track when data was collected
        today = datetime.date.today()

        # Write data to CSV
        header = ['Title', 'Price', 'Date']
        data = [title, price, today]

        with open('Amaz.csv', 'a', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

# Schedule the scraping function to run daily
scrape_amazon()

while True:
    schedule.run_pending()
    time.sleep(1)
