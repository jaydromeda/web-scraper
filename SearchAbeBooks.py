#Chris Charles
#Rayen Ben Aoun
#The code in this file will go through firefox, then abeBooks, then search the users
#search input, then filter the results. then return the page url to be scraped
import os
from selenium import webdriver
import constants as const
import FilterSearch as filt
from selenium.webdriver.common.by import By

#takes in the search input and 4 filter options, returns URL of search results
def SearchAbeBook(searchInput, productType, condition, binding, sellerRating):
    os.environ['PATH'] += const.env_var     #sets a path to location of firefox driver
    driver = webdriver.Firefox()
    driver.get(const.targetSite)            #opens up target site with firefox
    driver.implicitly_wait(4)
    my_element = driver.find_element(By.ID, "header-searchbox-input")   #finds the site searchbar
    my_element.click()
    my_element.send_keys(searchInput)
    my_element = driver.find_element(By.ID, "header-searchbox-button")  #finds the site searchbutton
    my_element.click()

    #error handling for no results
    try:
        my_element = driver.find_element(By.CLASS_NAME, "m-z-b")
        print("No Matching Results Found")
        return
    except:
        pass

    #Product type: Choose one of them or all of them (only books, magazines, and comics)
    filt.filterProduct(productType, driver)

    #Condition: choose new or used or default is both
    filt.filterCondition(condition, driver)

    #Binding: choose hardcover or softcover or default is both
    filt.filterBinding(binding, driver)

    #Seller Rating: Choose >=2 stars, >=3 stars, >=4 stars, 5 stars, or all sellers as default
    filt.filterRating(sellerRating, driver)

    return driver.current_url           #returns website url after traversing


