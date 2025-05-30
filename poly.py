# Base class or parent class
class Person():
    def __init__(self, name, email):
        # Instance variables
        self.name = name
        self.email = email

    # A method that can be overridden by child classes
    def get_info(self):
        return f'{self.name}'  # Returns just the name as a string


# Child class inheriting from Person
class Member(Person):
    def __init__(self, name, email, mem_id):
        # Calling the constructor of the parent class using super()
        super().__init__(name, email)
        self.mem_id = mem_id  # New attribute specific to Member

    # Overriding the get_info method (Polymorphism)
    def get_info(self):
        # Returns member-specific information as a dictionary
        return {'name': self.name, 'mem_id': self.mem_id}


# Creating a Member object
member = Member('Ali', 'ali@gmail.com', 'mem-001')

# Accessing the mem_id attribute
print(member.mem_id)  # Output: mem-001

# Accessing overridden get_info method
print(member.get_info())  # Output: {'name': 'Ali', 'mem_id': 'mem-001'}


# Another child class inheriting from Person
class Librarian(Person):
    def __init__(self, name, email, salary):
        # Call the parent class constructor
        super().__init__(name, email)
        self.salary = salary  # New attribute specific to Librarian

    # Overriding the get_info method (Polymorphism)
    def get_info(self):
        # Returns librarian-specific information as a list
        return [self.name, self.salary]


# Creating a Librarian object
libraian = Librarian('Smith', 'smith@gmail.com', 2393)

# Accessing the name attribute (inherited from Person)
print(libraian.name)  # Output: Smith
