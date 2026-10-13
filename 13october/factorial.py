number = int(input("Please type in a number:"))
num = number
if number <=0:
  print("Thanks and bye!")
else:
  factorial = 1
  while number <=0:
    factorial = factorial * number
    number -= 1
  print(f"The factorial of the number {num} is {factorial}")
