#Chris Charles
#Rayen Ben Aoun
#The code in this file holds the filter functions designed to
#click the disired filters on the Abe Books search page
import os
from selenium import webdriver
import constants as const
from selenium.webdriver.common.by import By

#Product type: Choose one of them or all of them (only books, magazines, and comics)
#Try/except methods needed in case the option is not available
def filterProduct(productType, driver):
    if productType == "books":
        try:
            my_element = driver.find_element(By.ID, "product-type-2")
            my_element.click()
        except:
            print(productType+" product type unavailable")
    elif productType == "magazines&periodicals":
        try:
            my_element = driver.find_element(By.ID, "product-type-3")
            my_element.click()
        except:
            print(productType+" product type unavailable")
    elif productType == "comics":
        try:
            my_element = driver.find_element(By.ID, "product-type-4")
            my_element.click()
        except:
            print(productType+" product type unavailable")
    else:
        try:
            my_element = driver.find_element(By.ID, "product-type-2")
            my_element.click()
        except:
            print(productType+" product type unavailable")
        try:
            my_element = driver.find_element(By.ID, "product-type-3")
            my_element.click()
        except:
            print(productType+" product type unavailable")
        try:
            my_element = driver.find_element(By.ID, "product-type-4")
            my_element.click()
        except:
            print(productType+" product type unavailable")

#Condition: choose new or used or default is both
#Try/except methods needed in case the option is not available
def filterCondition(condition, driver):
    if condition == "new":
        try:
            my_element = driver.find_element(By.ID, "new-books").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print(condition+" condition unavailable")
    elif condition == "used":
        try:
            my_element = driver.find_element(By.ID, "used-books").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print(condition+" condition unavailable")
    else:
        pass

#Binding: choose hardcover or softcover or default is both
#Try/except methods needed in case the option is not available    
def filterBinding(binding, driver):
    if binding == "hardcover":
        try:
            my_element = driver.find_element(By.ID, "hard-cover").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print(binding+" binding unavailable")
    elif binding == "softcover":
        try:
            my_element = driver.find_element(By.ID, "soft-cover").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print(binding+" binding unavailable")
    else:
        pass

#Seller Rating: Choose >=2 stars, >=3 stars, >=4 stars, 5 stars, or all sellers as default
#Try/except methods needed in case the option is not available    
def filterRating(sellerRating, driver):
    if sellerRating == "atleast2":
        try:
            my_element = driver.find_element(By.ID, "ratingtwostar").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print("seller rating of "+sellerRating+" unavailable")
    elif sellerRating == "atleast3":
        try:
            my_element = driver.find_element(By.ID, "ratingthreestar").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print("seller rating of "+sellerRating+" unavailable")
    elif sellerRating == "atleast4":
        try:
            my_element = driver.find_element(By.ID, "ratingfourstar").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print("seller rating of "+sellerRating+" unavailable")
    elif sellerRating == "5":
        try:
            my_element = driver.find_element(By.ID, "ratingfivestar").find_element(By.CLASS_NAME, "refinement-link")
            my_element.click()
        except:
            print("seller rating of "+sellerRating+" unavailable")
    else:
        pass
