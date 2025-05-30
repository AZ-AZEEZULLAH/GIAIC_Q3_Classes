# Base class: Person
class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def walk(self):
        print('Walking')

# Subclass: Member inherits from Person
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)  # Calls Person constructor
        self.mem_id = mem_id

# Create a Member instance
member = Member('Ali', 'ali@gmail.com', 'mem-001')
print(member.mem_id)      # Output: mem-001
print(member.walk())      # Output: Walking

# Subclass: Librarian inherits from Person
class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

# Create a Librarian instance
libraian = Librarian('Smith', 'smith@gmail.com', 2393)
print(libraian.name)      # Output: Smith

# Library class to manage books
class Library():
    def __init__(self, name, location):
        self.books = []               # List to store book names
        self.lib_name = name
        self.lib_location = location

    def add_book(self, new_book_name):
        return self.books.append(new_book_name)

    def remove_book(self, remove_book):
        return self.books.remove(remove_book)

    def get_book(self):
        return self.books

# Book class to define book details
class Book():
    def __init__(self, name, author, availability):
        self.book_name = name
        self.author_name = author
        self.availability = availability

    def borrow(self):
        self.availability  # (method does nothing yet)

# Creating book instances
book1 = Book('Poetry', 'Allama Iqbal', True)
print(book1.author_name)  # Output: Allama Iqbal

book2 = Book('Comedy', 'Umer Sharif', True)
book3 = Book('Tragedy', 'Ahemd', True)

# Create a Library instance and add books
mylib2 = Library('The library', 'Karachi')
print(mylib2.add_book(book2.book_name))  # Adds Comedy
print(mylib2.add_book(book3.book_name))  # Adds Tragedy

print(mylib2.get_book())  # Output: ['Comedy', 'Tragedy']

# Remove a book and display updated list
print(mylib2.remove_book('Tragedy'))     # Removes Tragedy
print(mylib2.get_book())                 # Output: ['Comedy']
