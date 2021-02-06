import random

def special_zombie_rolls(special_zombies):
  rolls = 1
  witch_zombies = 0
  boomer_zombies = 0
  smoker_zombie = 0
  hunter_zombie = 0

  while rolls <= special_zombies:
    d4 = random.randint(1,4)
    
    #checking for witch zombies
    if(d4 == 1):
      witch_zombies = witch_zombies + 1
    
    #checking for boomer zombies
    elif(d4 == 2):
      boomer_zombies = boomer_zombies + 1

    #checking for smoker zombies
    elif(d4 == 3):
      smoker_zombie = smoker_zombie + 1

    elif(d4 == 4):
      hunter_zombie = hunter_zombie + 1

    rolls = rolls + 1

  return (witch_zombies, boomer_zombies, smoker_zombie, hunter_zombie)