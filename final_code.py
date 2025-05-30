from abc import ABC, abstractmethod # type: ignore

# Abstract base class - Person
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Abstract method must be implemented by subclasses
    @abstractmethod
    def calculate_fine(self, days):
        pass

    # A general method that can be overridden in subclasses
    def get_info(self):
        return f'{self.name}'

# ------------------- Inheritance --------------------

class Member(Person):  # Member inherits from Person
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id

    # Polymorphism: Overriding get_info
    def get_info(self):
        return {"name": self.name, "member_id": self.member_id}

    # Implementing the abstract method
    def calculate_fine(self, days):
        return days * 2  # Simple fine calculation


class Librarian(Person):  # Librarian inherits from Person
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    # Polymorphism: Overriding get_info
    def get_info(self):
        return [self.name, self.salary]

    # Implementing the abstract method
    def calculate_fine(self, days):
        return self.salary - days  # Not realistic, just for example

# ------------------- Encapsulation --------------------

class Library:
    def __init__(self, name, location):
        self.lib_name = name
        self.lib_location = location
        self.__expenses = {"salary_exp": 1232, "KE_BILL": 14500}  # Private attribute

    # Getter method for private expenses
    def get_expenses(self):
        return self.__expenses

    # Setter method to update expenses
    def update_expenses(self, update_exp):
        self.__expenses = update_exp
        return self.__expenses

    # Adding a book
    def add_book(self, new_book_name):
        return f'{new_book_name} has been added to the library'

    # Removing a book
    def remove_book(self, remove_book):
        return f'{remove_book} has been removed from the library'

    # Returning a list of books
    def get_books(self):
        return ["Book1", "Book2", "Book3"]

# ------------------- Testing All Concepts --------------------

# Creating instances of Member and Librarian
member = Member("Ahmed", "ahmed@gmail.com", "member--001")
librarian = Librarian("Smith", "smith@gmail.com", 2393)

# Polymorphism: get_info() from both classes
print("Member Info:", member.get_info())       # {'name': 'Ahmed', 'member_id': 'member--001'}
print("Librarian Info:", librarian.get_info()) # ['Smith', 2393]

# Encapsulation: create a library object
my_lib = Library("The Library", "Karachi")

# Use the object's methods (not class methods)
print("Library Expenses:", my_lib.get_expenses())  # Getter
print("Updated Expenses:", my_lib.update_expenses({"salary_exp": 1500, "KE_BILL": 1300}))  # Setter

# Abstraction: calling implemented abstract methods
print(f"Fine for Member (Ahmed): {member.calculate_fine(5)}")     # 10
print(f"Fine for Librarian (Smith): {librarian.calculate_fine(5)}")  # 2388

# Library actions
print(my_lib.add_book("New Book"))       # Adding a book
print(my_lib.remove_book("Book1"))       # Removing a book
print("Books in Library:", my_lib.get_books())  # Getting list of books
