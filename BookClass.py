class Book:
    def __init__(self, title, isbn, author, condition, publisher, datePublished, format, rating, price, link):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.condition = condition
        self.publisher = publisher
        self.datePublished = datePublished
        self.format = format
        self.rating = rating
        self.price = price
        self.link = link

    def to_dict(self):
        return {
            'Title': self.title,
            'ISBN': self.isbn,
            'Author': self.author,
            'Condition': self.condition,
            'Publisher': self.publisher,
            'Date Published': self.datePublished,
            'Format': self.format,
            'Rating': self.rating,
            'Price': self.price,
            'Link': self.link
        }
