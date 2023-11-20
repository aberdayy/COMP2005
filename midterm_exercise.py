# Create a class called rectangle has a length and width attributes. write a method to calculate area
print("--------q1--------")
class rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_area(self):
        area = self._length * self._width / 2
        return area

rec = rectangle(5,3)
print(rec.calculate_area())
print("--------q2--------")
# Do Inheritance
class Animal:
    def ISleep(self):
        return ("I do sleep")
    def IEat(self):
        return ("I do eat")
    def ISound(self):
        return ("I have a sound")
class Dog(Animal):
    def Sound(self):
        return ("woof!")

myDog = Dog()
print(myDog.ISound())
print(myDog.Sound())
print("--------q3--------")
# Do encapsulation
class bank_account:
    def __init__(self):
        self._balance = 0
    def deposit(self,e):
        self._balance += e
        return f"Guncel bakiye: {self._balance} TRY"
    def withdraw(self,e:int):
        if self._balance >= e:
            self._balance -= e
            return f"Guncel bakiye: {self._balance} TRY\nCekilen Miktar: {e}"
        else:
            return "unsufficient balance"

MyAccount = bank_account()
print(MyAccount.deposit(100))
print(MyAccount.deposit(100))
print(MyAccount.withdraw(75))
print("--------q4--------")
# Do Polymorphism
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius**2

class rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calculate_area(self):
        area = self._length * self._width / 2
        return area
def calculate_area(obj):
    return obj.calculate_area()
ucgen = rectangle(10,8)
daire = Circle(5)
print(calculate_area(ucgen))
print(calculate_area(daire))
print("--------q5--------")
# Write a Python function that takes a list of numbers as a parameter and
# returns the sum of all even numbers in the list
sayilar = [1,2,3,4,5,6,7,8,9]
def even_nums(list):
    total = 0
    for i in range(len(list)):
        if (list[i] % 2) == 0:
            total += list[i]
    return total
print(even_nums(sayilar))
print("--------q6--------")
# is_prime

def is_prime(param):
    for i in range(2, param):
        if param % i==0:
            return False
    return True

print(is_prime(15))
print("--------q7--------")
def find_max(param):
    max = param[0]
    for i in range(len(param)):
        if param[i] > max:
            max = param[i]
    return max

a =[4, 9, 2, 7, 11, 5]
print(find_max(a))
print("--------q8--------")
