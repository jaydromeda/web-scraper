#Chris Charles
#Rayen Ben Aoun
#This will hold the constants that are used by the other files in the scraper
import os
#website targeted to be searched through then scraped
targetSite = "https://www.abebooks.com/"
#internal path to webdriver for firefox (should be placed in Scraper folder)
env_var = r"Scraper\geckodriver.exe"
#required to request url from amazon website
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}