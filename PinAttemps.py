attempts = 0
while True:
  code = int(input("PIN:"))
  attempts += 1
  if attempts == 1 and code == 4321:
    print("Correct! It took you one single attempt!")
    break
  elif code == 4321:
      print(f"Correct! It took you {attempts} attempts")
      break
  elif code != 4321:
     print("Wrong")