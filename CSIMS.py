# Create store information management system

# create class Vetements(Clothes)
class Vetements:
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


# create class Shirt
class Shirt(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)

# create class Pants
class Pants(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)

# create class Shoes
class Shoes(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)

class Dress(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)

class Skirt(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)

class UnderWear(Vetements):
    def __init__(self, name, price, quantity, size, gender):
        super().__init__(name, price, quantity, size, gender)