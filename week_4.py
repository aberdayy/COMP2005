'''
design a function with the following requirements:

has two args, sec arg has default val true.
write docstring to explain the func.
Within the function
first check the value of the second argument, if it is not True, return None and exit the function
then check the value of the first argument, it is less then zero, return absolute value of the argument. If it is greater then 100, return argument minus 100. Otherwise, return 1/10 of the argument (integer division)

Call your user-defined function with different valued arguments to test (print the arguments and return values) and get help about the function
Call the function using the values entered by the user. Read the first argument only. Print the result

'''
def exercise_1 (val, defVal = True):

    '''
    :param val:  
    :param defVal: 
    :return: 
    '''
    if defVal !=True:
        print("Exiting")
        exit()
    if val < 0:
        return abs(val)
    elif val >100:
        return  val-100
    else:
        return val//10

print(exercise_1(5))

'''
Design a function with following requirements:

Function should return the average of the numbers provided by the argument(s)
There is no restriction about the number of arguments to the function
Do not forget document string
Call your user-defined function with different arguments to test and get help about the function
'''
def exercise_2 (*args):
    numOfArgsGiven = 0
    total = 0
    for arg in args:
        numOfArgsGiven +=1
        total +=arg
    if numOfArgsGiven == 0:
        return 0
    return total/numOfArgsGiven

print(exercise_2(5,4,1,4,7,8,9,3,25))
'''
There is a dict named phonebook and you need to populate it. (Create phonebook as empty dict.)
Design a function to add key(Name) value (phone number) pairs to phonebook.
Keys and values are provided as arguments to the function. Function should be capable of working on different phonebooks and adding multiple records at a time.
'''
def exercise_3(phonebook, **kwargs):
    for key,value in kwargs.items():
        phonebook[key] = value

phonebook  = {}
exercise_3(phonebook,mert=905050010022,ali=905050001100)
print(phonebook)