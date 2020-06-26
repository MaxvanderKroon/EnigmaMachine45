alphabet = "abcdefghijklmnopqrstuvwxyz"
UIlist = []

class Enigma:
  def MachineParts(self, rotors, steckerbrett):
    self.rotors = rotors
    self.steckerbrett = steckerbrett

while True:
  UI = input("Please enter the encrypted/decrypted string:\n")
  print(list(UI))
  UIlist = [UI.lower()]

  i = 3
  while i == 3:
    TryAgain = input("Would you like to try again? please enter 'yes' or 'no'\n")
    if TryAgain == "yes":
      break
    else:
      i = i + 1
      if i != 3:
        print("terminating programme...")
  if i != 3:
   break
print("Programme sucessfully terminated")
