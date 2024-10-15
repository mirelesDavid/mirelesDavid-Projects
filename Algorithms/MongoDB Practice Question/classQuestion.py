# Your local municipality is opening a new library and is looking for a backing developer to build its backend system. You have been tasked to build a few features in this system.

# Background knowledge:
# Books are organized by author and genre.
# Bookcases hold books of a certain genre and are ordered by author, then by title
# Books are held in bookcases labeled by genre

# Please build the inventory system so that it includes the following methods:
# addToCatalog that inserts a book into the bookshelf
# getBookcaseContents that accepts a bookcase's genre (string) and returns an array of books sorted by author, title
# checkOutBook that either checks out the book if its available, or prints a message stating that the book is unavailable
# returnBook that returns the book to the bookcase
from collections import defaultdict
import heapq

class Book:
    def __init__(self, author, genre, title):
        self.author = author
        self.genre = genre
        self.title = title
        self.availability = True

class BookShelf:
    def __init__(self):
        self.bookShelf = defaultdict(list)

    def addToCatalog(self, book):
        if isinstance(book, Book):
            self.bookShelf[book.genre].append(book)
        else:
            return "Not a Book"

    def getBookCaseContents(self, genre):
        if genre in self.bookShelf:
            availableBooks = [book for book in self.bookShelf[genre] if book.availability]
            sortedBooks = sorted([(book.author, book.title) for book in availableBooks])
            return sortedBooks
        return "Genre not found"

    def checkOutBook(self, book):
        if isinstance(book, Book):
            if book.genre in self.bookShelf:
                for idx, shelfBook in enumerate(self.bookShelf[book.genre]):
                    if shelfBook == book and shelfBook.availability:
                        self.bookShelf[book.genre][idx].availability = False
                        return shelfBook.title, "Book Checked Out"
                return "Book Not Found in BookShelf"
            return "Book Genre not in BookShelf"
        return "Not a Book"

    def returnBook(self, book):
        if isinstance(book, Book):
            if book.genre in self.bookShelf:
                for idx, shelfBook in enumerate(self.bookShelf[book.genre]):
                    if shelfBook == book and not shelfBook.availability:
                        self.bookShelf[book.genre][idx].availability = True
                        return shelfBook.title, "Book Returned"
                return "Book Not Found in BookShelf"
            return "Book Genre not in BookShelf"
        return "Not a Book"

if __name__ == '__main__':
    book1 = Book('J.K. Rowling', 'Fantasy', 'Harry Potter and the Philosopher\'s Stone')
    book2 = Book('J.R.R. Tolkien', 'Fantasy', 'The Hobbit')
    book3 = Book('George Orwell', 'Dystopian', '1984')
    book4 = Book('Aldous Huxley', 'Dystopian', 'Brave New World')

    # Initialize BookShelf and add books to catalog
    bookShelf = BookShelf()
    bookShelf.addToCatalog(book1)
    bookShelf.addToCatalog(book2)
    bookShelf.addToCatalog(book3)
    bookShelf.addToCatalog(book4)

    # Get contents of the 'Fantasy' genre bookcase
    print(bookShelf.getBookCaseContents('Fantasy'))
    print(bookShelf.getBookCaseContents('Dystopian'))

    # Check out 'The Hobbit'
    print(bookShelf.checkOutBook(book2))

    # Check contents of the 'Fantasy' genre bookcase again
    print(bookShelf.getBookCaseContents('Fantasy'))

    # Return 'The Hobbit'
    print(bookShelf.returnBook(book2))

    # Check contents of the 'Fantasy' genre bookcase again
    print(bookShelf.getBookCaseContents('Fantasy'))
