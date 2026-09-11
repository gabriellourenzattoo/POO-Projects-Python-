#Library Py

""" Dicts person and books """
books = []
peoples = []

class Book():
    def __init__(self, name: str, year:int, author: str, borrowed: bool=False):
        self.name = name.title()
        self.year = year
        self.author = author.title()
        self.borrowed = borrowed
        self.borrowed_by = None
    
    def change(self, choice: str, new):
        match choice:
            case 'name':
                self.name = new
                print(f"name successfully changed. Changed the name to: {new}")
            case 'year':
                self.year = new
                print(f"Year successfully changed. Changed the year to: {new}")
            case 'author':
                self.author = new
                print(f"Author successfully changed. Changed the Author to: {new}")
            case _:
                print("Invalid option.")
        return self
    
    def viewer(self):
        print(f'\nName: {self.name}')
        print(f'Year: {self.year}')
        print(f'Author: {self.author}')
        print(f'Borrowed: {"Borrewed" if self.borrowed else "Available"}')
        print(f'Borrewed by: {self.borrowed_by}')
        
class People():
    def __init__(self, name: str, age: int):
        self.name = name.title()
        self.age = age
        self.book = None
    
    def get_a_book(self, book: Book):
        if not book.borrowed:
            self.book = book
            book.borrowed = True
            book.borrowed_by = self.name
            print(f"Book: '{book.name}' borrowed successfully.")
        else: 
            print(f"I couldn't get the book: '{book.name}' because it's already checked out.")
        return self 
        
    def return_a_book(self, book: Book):  
        if book.borrowed:
            if book.borrowed_by == self.name:
                self.book = None
                book.borrowed_by = None
                book.borrowed = False
                print(f"The book: {book.name} was returned successfully.")
            else:
                print(f"This person '{self.name}' not pick up a this book {book.name} ")
        else:
            print(f"The book: {book.name} isn't loaned out.") 
        return self        
    
    def viewer(self):
        print(f'\nName: {self.name}')
        print(f'Age: {self.age}')
        print(f'Book : {"none" if self.book == None else self.book.name }')

def login(people: People):
    while True:
        print(f"\nPerson Menu...\n",
              f"\n",
              f"1. Get a book\n",
              f"2. Return a book\n",
              f"3. View a person\n"
              f"4. Exit\n",)
        
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                name_book_input = input("Name of book: ")
                for book in books:
                    if book.name.lower() == name_book_input.lower():
                        if book.borrowed:
                            print("This book is already borrowed.")
                        else:
                            people.get_a_book(book)
                        break
                else:
                    print("Book not found.")
            case 2:
                name_book_input = input("Name of book: ")
                for book in books:
                    if book.name.lower() == name_book_input.lower().strip():
                        if book.borrowed:
                            people.return_a_book(book)
                        else:
                            print("This book isn't borrowed.")
                        break
                else:
                    print("Book not found.")    
            case 3:
                people.viewer()
            case 4:
                print("\nExit...\n")
                break
            case _:
                print(f"\nInvalid choice\n")
                
while True:
    print(f"\nWelcome to Py Library\n",
          f"\n",
          f"1. Login\n",
          f"2. Register a person\n",
          f"3. Register a book\n",
          f"4. Exit\n",)
    choice = int(input("Enter a choice: "))
    print()
    
    match choice:
        case 1:
            print("Login...\n ")
            name_person_input = input("Name of people: ")
            for person in peoples:
                if person.name.lower() == name_person_input.lower():
                    print("Person login with sucessfull.")
                    login(person)
                    break
            else:
                print("People not found. \n")

        case 2:
            print("Register...\n")
            
            person_name = input("Person's name: ")
            age = int(input("Age of people: "))
            
            for person in peoples:
                if person.name.lower() == person_name.lower():
                    print("This person Already exist.\n")
                    break
            else: 
                person = People(person_name, age)
                peoples.append(person)
                print("\nPerson registered successfully.\n")

        case 3:
            name = input("Name of book:")
            year = int(input("Year of book: "))
            author = input("Author of book: ")
            for book in books:
                if book.name.lower() == name.lower():
                    print("\nThis book Already exist.")
                    break
            else:
                book = Book(name, year, author)
                books.append(book)
                print("\nBook registered successfully.\n")
        case 4:
            print("Exit...\n")
            break
        case _:
            print("Invalid choice\n")
