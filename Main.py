import random

while True:
      characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*']
      length = input("Enter number of characters. Greater than 8: ")
      length = int(length)
      password = ""
      if length < 8:
            print("Inadequate characters for strong password. Do you want to proceed?")
            res = input("y/n")
            if res == 'n':
                  continue
      else:
            for i in range(length):
                  x = random.choice(characters)
                  characters.remove(x)
                  password = password + x

      print("Password is " + password)   

      query = input("Do you want to continue? (y/n): ")
      if query == "y":
            continue
      else:
            print("Thank You!")
            break
      