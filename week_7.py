from abc import abstractmethod, ABC


class Parent:
    def __init__(self, value):
        self.set_value(value)
    def set_value(self, value):
        self.value = value
    def get_value(self):
        return self.value
    def __str__(self): # use this method instead of display
        return "Parent display method ", self.get_value()

class Child(Parent):
    def set_value(self, value):
        self.value = -value
    def get_value(self):
        return self.value//2
    def __str__(self):
        return "Child display method ", self.get_value()



c = Child(3)
print(c.__str__())

l = [Parent(5), Child(5)]
for obj in l:
    print(obj.__str__())


class Abst(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def display(self):
        print(self.value)

class Child2(Abst):
    pass

obj = Abst(5)

