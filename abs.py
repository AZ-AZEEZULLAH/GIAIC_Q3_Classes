from abc import ABC, abstractmethod  # type: ignore # Import abstract base class tools

# Abstract base class
class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Abstract method that must be implemented in subclasses
    @abstractmethod
    def calculate_fine(self, days):
        pass

# Subclass representing a library member
class Member(Person):
    def __init__(self, name, email, member_id):
        super().__init__(name, email)
        self.member_id = member_id

    # Implementing the abstract method
    def calculate_fine(self, days):
        return days * 2

# Creating an instance of Member
member = Member("Ahmed", "ahmed@gmail.com", "member--001")
print("Member ID:", member.member_id)
print("Fine on member:", member.calculate_fine(10))

# Subclass representing a librarian
class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def get_info(self):
        return [self.name, self.salary]

    # Implementing the abstract method
    def calculate_fine(self, days):
        return self.salary - days  # Example logic

# Creating an instance of Librarian
librarian = Librarian("Smith", "smith@gmail.com", 2999)
print("Fine on librarian:", librarian.calculate_fine(5))
