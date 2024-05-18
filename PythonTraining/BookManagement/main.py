
books = []

def list_books():
    return books

def add_book(name, author, price, p_year):
    book = {
        "name": name,
        "author": author,
        "price_npr": price,
        "published_year": p_year
    }
    books.append(book)
    return True

def get_book(name):
    for book in books:
        if book["name"] == name:
            return book
        
def edit_book(name, key_to_edit, new_value):
    for book in books:
        if book["name"] == name:
            book[key_to_edit] = new_value
            return True


def main():
    while True:
        print("Starting book management system...")
        print("Enter l for getting book list")
        print("enter n for adding new book")
        print("enter d for book detail")
        print("enter x for deleting book")
        print("enter e for editing book information")
        print("enter q for exiting the application")
        user_input = input("User input: ")
        if user_input == "l":
            all_books = list_books()
            print("Listing all books...")
            for book in all_books:
                print(book)
        elif user_input == "n":
            book_name = input('Enter book name: ')
            author = input('Enter book author: ')
            price = int(input("Enter book price: "))
            published = input("Enter book published year: ")
            add_book(book_name, author, price, published)
        elif user_input == "d":
            book_name = input("Enter book name: ")
            book = get_book(book_name)
            print(book)
        elif user_input == "x":
            ...
        elif user_input == "e":
            book_name = input("Enter book name: ")
            book = get_book(book_name)
            print(book)
            key_to_change = input("Which information you want to change? ")
            new_value = input("Enter new value: ")
            edit_book(book_name, key_to_change, new_value)
            book = get_book(book_name)
            print(book)

        elif user_input == "q":
            exit()
        else:
            print("Your input is invalid")

main()