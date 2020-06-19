alphabet = "abcdefghijklmnopqrstuvwxyz"
print(list(alphabet))
i = 1
while i < 6:
  UI = input("Please enter a letter:\n")
  print(f'You entered {UI}')
  if UI == "A":
    print("processing A")
  else:  
    print ("okay")
