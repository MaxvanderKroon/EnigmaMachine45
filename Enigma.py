alphabet = "abcdefghijklmnopqrstuvwxyz"
UIlist = []

while True:
  UI = input("Please enter the encrypted/decrypted string:\n")
  print(list(UI))
  UIlist = [UI.lower]

  while True:
    if input("Would you like to try again? please enter 'yes' or 'no'\n") == "yes":
      break
    else:
      print("terminating programme")
