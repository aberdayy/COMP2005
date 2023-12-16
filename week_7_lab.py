# create class named rectangele the class should have attributes lenght and width.
# Include a method called calculate_area that calculates and returms the area of
# the rectangle. create a instance of this class with len 5 wid 3 then print area



class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def start_engine(self):
        self.engine.start()

car = Car()
car.start_engine()  # Output: Engine started



# List - Mutable
my_list = [1, 2, 3]
my_list[0] = 5  # Modifying an element
my_list.append(4)  # Adding an element
print(my_list)  # Output: [5, 2, 3, 4]

# Tuple - Immutable
my_tuple = (1, 2, 3)
# This line would raise an error since tuples are immutable:
my_tuple[0] = 5
print(my_tuple)  # Output: (1, 2, 3)







class Animal:
    def make_sound(self):
        print("Some generic sound")

class Flyable:
    def fly(self):
        print("Flying high")

class Bird(Animal, Flyable):
    def __init__(self, species):
        self.species = species

bird = Bird("Sparrow")
bird.make_sound()  # Output: Some generic sound
bird.fly()         # Output: Flying high


class Bird:
    def fly(self):
        print("Flying high")

class Airplane:
    def fly(self):
        print("Flying at high speed")

def lift_off(entity):
    entity.fly()

bird = Bird()
plane = Airplane()

lift_off(bird)  # output: Flying high
lift_off(plane) # output: Flying at high speed










# q1
class Rectangle:
    def __init__(self, len, width):
        self._len = len
        self._width = width

    def calc_area(self):
        return self._len * self._width / 2

ucgen = Rectangle(5,2)

print(ucgen.calc_area())

'''
Create a base class called animal include an 
attrubute species, make_sound. 
Create a divered class called dog that iherits from animal and includes a method that prints woof
create instance of Dog class and demostrate both
'''
# q2
class Animal:
    def eat(self):
        return 'it eats'
    def sleep(self):
        return 'it sleeps'

class Dog(Animal):
    def bark(self):
        return 'woof!'


animal = Animal()
kopek = Dog()
print(kopek.bark())
print(kopek.sleep())


class BankAccount:
     def __init__(self):
         self._balance = 0 # Encapsulated attribute
     def deposit(self, amount):
         self._balance += amount
     def withdraw(self, amount):
         if amount <= self._balance:
             self._balance -= amount
         else:
             print("Insufficient funds")
     def get_balance(self):
         return self._balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
print(account.get_balance())

'''
Create a class named BankAccount with private attributes balance and account_holder.
Implement methods deposit and withdraw to modify the balance. 
Use encapsulation to protect the attributes. 
Create an instance of this class and demonstrate the deposit and withdrawal operations.
'''

# encapsulation calis
# polymorphism calis
#q4
class erkekler:
    def favori_renk(self):
        return ("erkekler pembe am sever")
    def favoriAraba(self):
        return ("erkekler ferrari sever")

class kizlar:
    def favori_renk(self):
        return ("kizlar pembe sever")
    def favoriAraba(self):
        return ("kizlar bmw sever")

kiz_renk = kizlar()
erkek_renk = erkekler()
print(kiz_renk.favori_renk())
print(erkek_renk.favori_renk())


# tuple tanimina calis
# list tanimina calis
#q5
def hesap(liste):
    sum = 0
    for e in range(len(liste)):
        if liste[e] % 2==0:
            sum += liste[e]

    print(sum)

hh = [1,2,3,4,5,6]
hesap(hh)
print("---------------------")
#q6
def is_prime(e):
    if e % 2 == 0 and e % 3 == 0 and e % 5 == 0:
        return False
    elif e == 1 :
        return "sayi 1"
    else:
        return True

print(is_prime(125))

#q7
def find_max(e):
    max = e[0]
    for num in e:
        if num > max:
            max = num
    return max


a = [4, 9, 2, 7, 11, 5]
print(find_max(a))