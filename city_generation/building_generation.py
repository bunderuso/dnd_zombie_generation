import random
from city_generation.special_zombies_d6 import special_zombie_rolls


def city_block():

  #define zombie variables
  tank_zombies = 0
  special_zombies = 1
  normal_zombies = 6
  witch_zombies = 0
  boomer_zombies = 0
  smoker_zombie = 0
  hunter_zombie = 0

  #define building variables 
  civ_buildings = 6
  medical_buildings = 0
  police_buildings = 0
  military_buildings = 0

  #defining d20 roll list
  d20_rolls = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]




  #iterating through the rolls
  for index in range(len(d20_rolls)):

    #checking tank zombies 
    if(d20_rolls[index] == 1):
      print("Tank zombie")
      tank_zombies = tank_zombies + 1 

    #checking special zombies
    elif(d20_rolls[index] in range(2,3)):
      print("special zombie") 
      special_zombies = special_zombies + random.randint(1,6)


    #checking normal zombies
    elif(d20_rolls[index] in range(4,7)):
      print("normal zombies")
      normal_zombies = normal_zombies + 1
    
    #checking civ buildings
    elif(d20_rolls[index] in range(8, 14)):
      print("civ buildings")
      civ_buildings = civ_buildings + 1

    #checking medical buildings
    elif(d20_rolls[index] in range(15, 17)):
      print("medical building")
      if(medical_buildings == 2):
        d20_rolls[index] = random.randint(1,20)
        index = index - 1
      else:
        medical_buildings = medical_buildings + 1

    #checking police buildings
    elif(d20_rolls[index] in range(18,19)):
      print("Police building")
      if(police_buildings == 2):
        d20_rolls[index] = random.randint(1,20)
        index = index - 1
      else: 
        police_buildings = police_buildings + 1

    #checking military buidlings
    elif(d20_rolls[index] == 20):
      print("military buildings")
      if(military_buildings == 1):
        d20_rolls[index] = random.randint(1,20)
        index = index - 1
      else:
        military_buildings = military_buildings + 1

  print("\nout of loop\n")

  #doing the special zombies
  (witch_zombies, boomer_zombies, smoker_zombie, hunter_zombie) = special_zombie_rolls(special_zombies)


