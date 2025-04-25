#Chris Charles
#Rayen Ben Aoun
#This file will scrape and parse the relevant information from the target site
#and store in a list that is passed to it, will continue until there are no
#more pages to scrape
from bs4 import BeautifulSoup
import requests
import constants as const
import BookClass as BookData

def ScrapeBook(siteURL, bookList):
    HEADER = const.header                                   #used to get access to websites
    html_text = requests.get(siteURL, headers=HEADER)
    soup = BeautifulSoup(html_text.text, 'lxml')
    books = soup.find_all('li', class_='cf result-item')    #encompasses all book results on page
    for book in books:                                      #for loop that goes through each book result individually
        title = book.find('meta', itemprop='name')['content']
        try:                                                #each try/except is needed in case information is not found
            isbn = book.find('meta', itemprop='isbn')['content']
        except:
            isbn = "N/A"
        try:
            author = book.find('meta', itemprop='author')['content']
        except:
            author = "N/A"
        try:
            condition = book.find('span', class_='opt-subcondition').text
            condition = condition.split()[1]
        except:
            condition = "N/A"
        try:
            publisher = book.find('meta', itemprop='publisher')['content']
        except:
            publisher = "N/A"
        try:
            datePublished = book.find('meta', itemprop='datePublished')['content']
        except:
            datePublished = "N/A"
        try:
            bookFormat = book.find('meta', itemprop='bookFormat')['content']
        except:
            bookFormat = "N/A"
        try:
            bookRating = book.find('p', class_='bookseller-rating').find('a', rel='nofollow').find('img')['alt']
            bookRating = bookRating.split()[0]
        except:
            bookRating = "N/A"
        try:
            bookPrice = book.find('p', class_='item-price').text
        except:
            bookPrice = "N/A"
        try:
            link = "https://www.abebooks.com"+book.find('a', itemprop='url')['href']
        except:
            link = "N/A"

        #store book data in a class object
        B1 = BookData.Book(title, isbn, author, condition, publisher, datePublished, bookFormat, bookRating, bookPrice, link)

        #store/add book data to list
        bookList.append(B1)


    try:                     #if next page button exists, go to it and repeat scrape
        almostURL = soup.find('section', class_='paging-bottom').find('nav', id='bottom-nav').find('ul', class_='pagination-b').find('a', id='page-next-bottom-nav')['href']
        URL = "https://www.abebooks.com"+almostURL
        ScrapeBook(URL, bookList)
    except:                 #if next page button dsnt exist, end scrape
        return 



