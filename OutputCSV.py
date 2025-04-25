#This function will accept the Book List Data and output it into
#a csv file

import csv

def OutputCSV(books, fileName):
    with open(fileName+'.csv', mode='w') as csvfile:
        fieldNames = ['Title', 'ISBN', 'Author', 'Condition', 'Publisher', 'Date Published', 'Format', 'Rating', 'Price', 'Link']
        writer = csv.DictWriter
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

        for book in books:
            writer.writerow({
                'Title': book.title,
                'ISBN': book.isbn,
                'Author': book.author,
                'Condition': book.condition,
                'Publisher': book.publisher,
                'Date Published': book.datePublished,
                'Format': book.format,
                'Rating': book.rating,
                'Price': book.price,
                'Link': book.link
            })