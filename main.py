import random
from modified_rolls import modified_rolls
from city_generation.test import test


choice = -99

while choice != 0:
    print("Option 1: Roll a D20")
    print("Option 2: Roll a D12")
    print("Option 3: Roll a D8")
    print("Option 4: Roll a D6")
    print("Option 5: Roll a D4")
    print("Option 6: Roll a D100")
    print("Option 7: Roll a modified")
    print("Option 8: Roll for City Generation")
    print("Option 9: ")

    choice = int(input("Pick your option: "))
    print()

    #define choices
    if(choice == 1):
        print("Rolling a D20")
        d20 = random.randint(1, 20)
        print("Result", d20)
        print()

    elif(choice == 2):
        print("Rolling a D12")
        d12 = random.randint(1, 12)
        print("Result", d12)
        print()

    elif(choice == 3):
        print("Rolling a D8")
        d8 = random.randint(1, 8)
        print("Result", d8)
        print()

    elif(choice == 4):
        print("Rolling a D6")
        d6 = random.randint(1, 6)
        print("Result", d6)
        print()

    elif(choice == 5):
        print("Rolling a D4")
        d4 = random.randint(1, 4)
        print("Result", d4)
        print()

    elif(choice == 6):
        print("Rolling a D100")
        d100 = random.randint(1, 100)
        print("Result", d100)
        print()

    elif(choice == 7):
        print("Rolling a modified")
        print(modified_rolls())
    
    elif(choice == 8):
        print("Generating City Block")
        print(test())


    elif(choice == 0):
        print("Thanks for rolling!")
        choice = 0