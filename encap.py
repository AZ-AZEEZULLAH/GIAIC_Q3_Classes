class Person():
    def __init__(self,name,email):
        self.name = name
        self.email = email

class Library():

    # constructor

    def __init__(self, name , location):

        # Class attributes / class variable / paremeter

        self . lib_name = name
        self. lib_location = location

        # Declaring a private attribute 

        self._expenses = {"salary Exp " : 1234 , "KE_BILL" : 14000}

        # getter function 


    def get_expensive(self):
        return self._expenses
    


    # Setter Function 

    def update_expensive(self, update_exp):
       # self._expenses = {"salaryExp": 12345 ,"KE_BILL":12345, "furniture":50987}

       self. _expenses = update_exp
       return self._expenses
    

    # class methods / function 


    def add_book(self, new_book_name):
        return self.books.append(new_book_name)
    
    def remove_book(self, remove_book):
        return self.remove(remove_book)
    

    def get_get_book(self):
        return self.books
    

    # Making an object / Creating Instance of a class


my_lib = Library("The Library", "Karachi")

print(my_lib.get_expensive())

print(my_lib.update_expensive({"salary_exp":1234, "KE_Bill": 5600, "furniture":50098}))


