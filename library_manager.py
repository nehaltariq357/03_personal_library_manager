
class Book:
    def __init__(self,title,author,year,genre,read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    # def __str__(self):
    #     read_status = "Read" if self.read else "unread"
    #     return f"{self.title} by {self.author} ({self.year}) - {self.genre} - {read_status}"
    

class Library():
    def __init__(self):
        self.Books=[]
        
    def add_book(self):
        title = input("enter title: ")
        author = input("enter author: ")
        year = input("enter publish year: ")
        genre = input("enter genre: ")
        read_input = input("have you read book(yes/no): ")
        read = "Read" if read_input=="yes" else "Unread"
        books = {
            "title":title,
            "author":author,
            "year":year,
            "genre":genre,
            "read":read,
        }

        self.Books.append(books)
        print(f"{title} was added successfully!")
        pass
    def remove_book(self):
        delete_book = input("enter the title of the book to remove: ")
        for book in self.Books:
            if book["title"].lower() == delete_book.lower():
                self.Books.remove(book)
                print(f"{delete_book} removed successfully! ")
                return # use return to exit the method immediately after successfully removing the book
        else:
            print(f"{delete_book} was not in the book list")
        pass
    def search_book(self):
        print("search by: ")
        print("1. Title")
        print("2. Author")
        pass
    def display_book(self):
        if not self.Books:
            print("book not found")
        else:
            for idx, book in enumerate(self.Books,1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['read']}")
        pass
    def display_statistics(self):
        pass
    def exit(self):
        pass


b1 = Library()
b1.add_book()
b1.display_book()
b1.remove_book()
b1.display_book()