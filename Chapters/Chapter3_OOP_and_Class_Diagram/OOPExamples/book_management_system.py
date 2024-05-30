


class Book:
    def __init__(self, book_name, price, author=None):
        self.name = book_name
        self.price = price
        self.author = author

    def update_book(self, book_name=None, book_price=None, author=None):
        if book_name:
            self.name = book_name
        if book_price is not None:
            self.price = book_price
        if author is not None:
            self.author = author
        

    def show_detail(self):
        print("Book name:", self.name)
        print("Book price:", self.price)
        print("Book author:", self.author)

book1 = Book("Design Principle", 5000)
book1.show_detail()
print("----------------------------------------------------------------")
book1.update_book(book_price=3500, author="Dipak Niroula")

