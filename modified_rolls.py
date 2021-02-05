import random

def modified_rolls():
    # define d100 dice
    d100 = random.randint(1, 100)

    # define d20 dice
    #d20 = random.randint(1, 20)

    # define d12 dice
    #d12 = random.randint(1, 12)

    # define d8 dice
    #d8 = random.randint(1, 8)

    # define d6 dice
    #d6 = random.randint(1, 6)

    # define d4 dice
    #d4 = random.randint(1, 4)


    #define options
    print("Option 1: D20 dice")
    print("Option 2: D12 dice")
    print("Option 3: D8 dice")
    print("Option 4: D6 dice")
    print("Option 5: D4 dice")
    print("Option 6: D100 dice")
    dice_choice = int(input("What dice are you rolling: "))

    #define d20 instructions
    if(dice_choice == 1):
        #asking for user input
        multiples = int(input("How many D20s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d20 = random.randint(1, 20)
            total = total + d20
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total

    # define d12 instructions
    elif(dice_choice == 2):
        #asking for user input
        multiples = int(input("How many D12s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d12 = random.randint(1, 12)
            total = total + d12
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total


    # define d8 instructions
    elif(dice_choice == 3):
        #asking for user input
        multiples = int(input("How many D8s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d8 = random.randint(1, 8)
            total = total + d8
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total

    # define d6 instructions
    elif(dice_choice == 4):
        #asking for user input
        multiples = int(input("How many D6s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d6 = random.randint(1, 6)
            total = total + d6
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total

    # define d4 instructions
    elif(dice_choice == 5):
        #asking for user input
        multiples = int(input("How many D4s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d4 = random.randint(1, 4)
            total = total + d4
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total

    # define d100 instructions
    elif(dice_choice == 6):
        #asking for user input
        multiples = int(input("How many D100s to roll: "))
        modifier = int(input("What is the modifier: "))

        #defining while loop variable
        rolls = 1
        total = 0
        while rolls <= multiples:
            d100 = random.randint(1, 100)
            total = total + d100
            rolls = rolls + 1

        #adding in the modifer
        total = total + modifier
        return total
