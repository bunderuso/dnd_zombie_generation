test = {"1" : 1, "2" : 2, "3" : 3 }

for key in test:
  print(key, test[key])
  if test[key] == 2:
    key = key - 1
    print(key, test[key])