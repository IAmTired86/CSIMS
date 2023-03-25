# Create store information management system

# create class Vetements(Clothes)

class Vetement():
    def __init__(self, name, price, quantity, size, gender):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__size = size
        self.__gender = gender

    @property
    def _getName(self):
        return self.__name

    @property
    def _getPrice(self):
        return self.__price
    
    @property
    def _setPrice(self,price):
        self.__price = price

    @property
    def _getQuantity(self):
        return self.__quantity

    @property
    def _getSize(self):
        return self.__size

    @property
    def _getGender(self):
        return self.__gender
    
    def __str__(self):
        return f"Name: {self.__name}\t Price: {self.__price}\t Quantity: {self.__quantity}\t Size: {self.__size}\t Gender: {self.__gender}"


vetements = []

#Create class Employee
class Employee():
    def __init__(self,Fname,Lname,id, position, workday, salary):
        self.__Fname = Fname
        self.__Lname = Lname
        self.__id = id
        self.__position = position
        self.__workday = workday
        self.__salary = salary
    
    def __str__(self):
        return f"First name: {self.__Fname}\t Last name: {self.__Lname}\t ID: {self.__id}\t Position: {self.__position}\t Workday: {self.__workday}\t Salary: {self.__salary}"
    
    @property
    def Fname(self):
        return self.__Fname
    
    @property
    def Lname(self):
        return self.__Lname

    @property
    def id(self):
        return self.__id

    @property
    def position(self):
        return self.__position

    @property
    def workday(self):
        return self.__workday

    @property
    def salary(self):
        return self.__salary

employees = []




class Receipt():
    def __init__(self, customer, vetements,bill):
        self.__customer = customer
        self.__vetements = vetements
        self.__bill = bill

    @property
    def customer(self):
        return self.__customer
    
    @property
    def vetements(self):
        return self.__vetements
    
    @property
    def bill(self):
        return self.__bill



def inputVetement():
    number = int(input("Enter number of clothes: "))
    for i in range(number):
        name = input("Enter name: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        size = input("Enter size: ")
        gender = input("Enter gender:")
        vetements.append(Vetement(name,price,quantity,size,gender))

def showVetement():
    for i in vetements:
        print(i)


def inputEmployee():
    number = int(input("Enter number of employee: "))
    for i in range(number):
        Fname = input("Enter first name: ")
        Lname = input("Enter last name: ")
        id = input("Enter id: ")
        position = input("Enter position: ")
        workday = int(input("Enter workday: "))
        salary = int(input("Enter salary: "))
        employees.append(Employee(Fname,Lname,id,position,workday,salary))

def CountTotal():
    while True:
        showVetement()
        choice = input("Enter your choice: ")
        for vetement in vetements:
            if vetement._name == choice:
                print("Enter quantity: ")
                quantity = int(input())
                bill = quantity * vetement._getPrice()
                print("Total: ",bill)
                break
            else:
                print("Invalid choice")
                break

    

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