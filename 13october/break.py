sum = 0
# while True:
#     number = int(input("Please enter a number:"))
#     if number == -1:
#         break
#     sum += number

number = 0
while number != -1:
  number = int(input("Enter the number:"))
  if number != -1:
    sum += number

print("The sum is:" , sum)