#This function will take in a list of class:Book and print it
#This is mainly for testing data accuracy purposes

def PrintBookList(books):
    for book in books:
        print(book.title)
        print(book.isbn)
        print(book.author)
        print(book.condition)
        print(book.publisher)
        print(book.datePublished)
        print(book.format)
        print(book.rating)
        print(book.price)
        print(book.link)