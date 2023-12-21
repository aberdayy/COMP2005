# hire method for employee -> employer obj as an argunment and will compare the work area of the argument expertise field of the object
#  If they are not the same, or any of them is None, you will generate an exception from the exception class you defined and occupation will be None, otherwise Employer object will be assigned to occupation.
#  Create two objects of the Employee class and one object of the Employer class. Specify the Employer object's workspace as carpentry, one of the Employee objects as expertise Computer Hardware, and the other as carpentry, call hire method of both Employee objects, providing the Employer object as argument.

#2. Define a class named Person. Name and Age attributes will be determined in the constructor (default values ("" and 0).
class person():
    def __init__(self,name = "", age=0):
        self.name = name
        self.age = age
    def name_setter(self,p):
        self.name = self.p
    def name_getter(self):
        return self.name
    def age_setter(self,p):
        self.age = self.p
    def age_getter(self):
        return self.age

# 3. Define the Employer (additional attribute: work_area, default: None)
class employer(person):
    def __init__(self, work_area=None):
        self.work_area = work_area
# Define Employee (additional attributes: expertise, occupation default: None, None)
class employe(person):
    def __init__(self, expertise=None, occupation = None):
        self.expertise = expertise
        self.occupation = occupation

# 1. Define an exception class named Uncompatible.
class Uncompatible:
    print("The work area of the employer does not match the expertise of the employee")


def hire(self, employer):
    # Compare the work_area of the employer with the expertise of the employee
    if employer.work_area == self.expertise:
        # Assign the employer to the occupation of the employee
        self.occupation = employer
        print("burasi calisti")
    elif (employer.work_area or self.expertise)==None:
        # Raise exception
        Uncompatible()
        print("hata1")
        # Set the occupation of the employee to None
        self.occupation = None
    else:
        # Raiseexception
        Uncompatible()
        # Set the occupation of the employee to None
        self.occupation = None
        print("hata2")

# Create two objects of the Employee class and one object of the Employer class.
# Specify the Employer object's workspace as carpentry, one of the Employee objects as expertise Computer Hardware, and the other as carpentry,
# call hire method of both Employee objects, providing the Employer object as argument.

# ------TEST---------

e = employe()
er = employer()
er.name = "ata"
er.age=22
er.work_area ="carpentary"
e.expertise="Computer Hardware"

e2 = employe()
er2 = employer()
er2.name = "tadic"
er2.age=37
er2.work_area ="carpentary"
e2.expertise="carpentary"
hire(e2,er2)
