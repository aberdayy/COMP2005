'''
Define a list, lights with values red, yellow and green
Create a variable, current_light, assign the value red
Create a loop, change the value of current_light iterating through lights
Display these messages;
    if light is red = STOP
    if light is yellow = Get Ready
    if light is green = Go
    otherwise message is Unknown light color
'''
# exercise part 1. Only with if else blocks

lights = ["red","yellow","green"]

def exercise_1 (list_of_lights):
    for light in list_of_lights:
        if light == "red":
            print("STOP")
        elif light == "yellow":
            print("Get Ready")
        elif light == "green":
            print("GO")
        else:
            print(f"light is {light} error!")
        break

exercise_1(lights)

# exercise part 2. counter controlled loop with mach case

def exercise_2(list_of_lights):
    for num in range(len(list_of_lights)):
        currentLight = lights[num]
        match(currentLight):
            case "red":
                print(f"light is {currentLight} STOP!")
            case "yellow":
                print(f"light is {currentLight} Get Ready")
            case "green":
                print(f"light is {currentLight} GO!")
                break
            case _:
                print(f"light is {currentLight} ERROR!")
                break
exercise_2(lights)
# Exercise 3. Define a dictionary, where keys are from light and the values are the messages you have displayed.
# Alter your loop to chechl the colors from the dictionary and display messages using the dictionary as well

def exercise_3 (list_of_lights):
    myDict  = {}
    messages = ["Light is Red STOP","Light is Yellow Get Ready", "Light is Green GO"]
    for num in range(len(list_of_lights)):
        myDict[list_of_lights[num]] = messages[num]

    for light, message in myDict.items():
        if light == "red":
            print(message)
        elif light == "yellow":
            print(message)
        elif light == "green":
            print(message)
        else:
            print("error!")

exercise_3(lights)