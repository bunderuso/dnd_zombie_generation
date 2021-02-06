import random

#define zombie variables
tank_zombies = 0
witch_zombies = 0
boomer_zombies = 0
smoker_zombie = 0
hunter_zombie = 0

#define building variables 
civ_buildings = 6
medical_buildings = 0
police_buildings = 0
military_buildings = 0

#defining d20 die roll dictionary
d20_rolls = {"die_1" : random.randint(1, 20), "die_2" : random.randint(1, 20), "die_3" : random.randint(1, 20), "die_4" : random.randint(1, 20), "die_5" : random.randint(1, 20), "die_6" : random.randint(1, 20), "die_7" : random.randint(1, 20), "die_8" : random.randint(1, 20), "die_9" : random.randint(1, 20), "die_10" : random.randint(1, 20)}

for dies in d20_rolls:
  print(dies, d20_rolls[dies])

#iterating through the rolls
for die in d20_rolls:
  #tank zombie spawns
  if (d20_rolls[die] == 1):
    tank_zombies = tank_zombies + 1
  #special zombie spawns
  elif(d20_rolls[die] in range(2, 3)):
    print("Special spawns")
    #place holder for special spawn functions
  elif(d20_rolls[die] in range(4, 7)):
    print("normal zombie spawns")
    #place holder for normal spawn functions
  elif(d20_rolls[die] in range(8, 14)):
    print("civ buildings")
    #place holder for Civ functions
  elif(d20_rolls[die] in range(15, 17)):
    print("medical buildings")
    if(medical_buildings == 2):
      d20_rolls[die] = random.randint(1, 20)
      die = die - 1


print(tank_zombies)