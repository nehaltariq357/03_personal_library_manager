
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
        print(f"{delete_book} was not in the book list")
            
        pass
    def search_book(self):
        print("search by: ")
        print("1. Title")
        print("2. Author")
        choice = int(input("enter your choice: "))
        if choice == 1:
            print("search by title")
            title = input("enter the title: ")
            found_books = []
            for book in self.Books:
                if title.lower() in book["title"].lower():
                    found_books.append(book)

        elif choice == 2:
            print("search by author")
            author = input("enter the author: ")
            found_books = []
            for book in self.Books:
                if author.lower() in book["author"].lower():
                    found_books.append(book)
        else:
            print("invalid choice")
            return
        
        if found_books:
            print("matching books:")
            for idx,book in enumerate(found_books,1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['read']}")
        else:
            print("no matching book found")
        pass
    def display_book(self):
        if not self.Books:
            print("book not found")
        else:
            for idx, book in enumerate(self.Books,1):
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {book['read']}")
        pass
    def display_statistics(self):
        total_books = len(self.Books)
        if total_books ==0:
            print("no book in the library")
            return
        read_book = 0
        for book in self.Books:
            if book["read"] == "read" or "Read":
                read_book +=1
        percentage_read = (read_book/total_books) *100 if total_books > 0 else 0
        print("total book:", total_books)
        print("percentage read:", round(percentage_read,2),"%")
        pass
    def exit(self):
        pass

class Menu:
    def __init__(self):
        self.library = Library()
        pass

    def show_menu(self):
        print("\n---------welcome to library management sysytem---------\n")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics (total books, percentage read)")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.library.add_book()
            elif choice == "2":
                self.library.remove_book()
            elif choice == "3":
                self.library.search_book()
            elif choice == "4":
                self.library.display_book()
            elif choice == "5":
                self.library.display_statistics()
            elif choice == "6":
                print("\nGoodbye!\n")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.\n")



if __name__ == "__main__":
    menu = Menu()
    menu.run()