# Define the Book class
class Book:
    # The constructor method to initialize the object
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    # Method to return a description of the book
    def describe(self):
        return f"The interesting book I've read is '{self.title}' by {self.author}, published in {self.year_published}."

# Create an instance of the Book class
my_book = Book("1984", "George Orwell", 1949)

# Print the description of the book
print(my_book.describe())

#-------------------------------------------------#

class Car:
    # The constructor method to initialize the object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to return a description of the car
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Print the description of the car
print(my_car.describe())
