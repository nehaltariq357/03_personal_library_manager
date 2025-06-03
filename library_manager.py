
class Book:
    def __init__(self,title,author,year,genre,read):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    def __str__(self):
        read_status = "Read" if self.read else "unread"
        return f"{self.title} by {self.author} ({self.year}) - {self.genre} - {read_status}"
    

class Library(Book):
    Books = []
    def __init__(self, title, author, year, genre, read):
        super().__init__(title, author, year, genre, read)

    def add_book(self):
        title = input("enter title: ")
        author = input("enter author: ")
        year = input("enter publish year: ")
        genre = input("enter genre: ")
        read = input("have you read book(yes/no): ")
        books = {
            "title":title,
            "author":author,
            "year":year,
            "genre":genre,
            "read":read,
        }

        self.Books.append(books)
        print(f"{self.title} was added successfully!")
        pass
    def remove_book(self):
        pass
    def search_book(self):
        pass
    def display_book(self):
        pass
    def display_statistics(self):
        pass
    def exit(self):
        pass


b1 = Library("python","nehal",2025,"eduation",True)
b1.add_book()
print(Library.Books)