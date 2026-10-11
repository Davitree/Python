from math import sqrt

num = int(input("Please type in a number:"))
if num < 0:
    print("Invalid number")
elif num > 0:
    print(sqrt(num))
while True:
    num2 = int(input("Please type in a number:"))
    if num2 > 0:
        print(sqrt(num2))
    elif num2 < 0:
        print("Invalid number")
    elif num2 == 0:
        print("Exiting...")
        break
