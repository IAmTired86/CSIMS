# Create store information management system

# create class Vetements(Clothes)
class Vetements:
    def _print(self):
        pass

# create class Shirt and shirt list
class Shirt(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"
    
            

shirts = []

# create class Pants and pants list
class Pants(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    @property
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"

pants = []

# create class Shoes and shoes list
class Shoes(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    @property
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"

shoes = []

# create class dress and dress list
class Dress(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    @property
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"
dress = []


# create class skirt and skirt list
class Skirt(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    @property
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"
skirt = []

# create class underwear and underwear list
class UnderWear(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def size(self):
        return self.__size

    @property
    def gender(self):
        return self.__gender
    
    @property
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"
underwear = []

for i in range(1,2,1):
    name = input("Enter name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    size = input("Enter size: ")
    gender = input("Enter gender:")
    shirts.append(Shirt(name,price,quantity,size,gender))

for shirt in shirts:
    print(shirt)
# while True:
#     print("1. Input information")
#     print("2. Show information")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         pass
#     elif choice == 2:
#         pass
#     elif choice == 3:
#         break
#     else:
#         print("Invalid choice")