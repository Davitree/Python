# print("Please type in integer numbers. Type in 0 to finish.")
sum = 0
count = 0
mean = 0
posCount = 0
negCount = 0
while True:
  num = int(input("Number:"))
  if num == 0:
    break
  if num > 0:
    posCount+=1
  else:
    negCount +=1
  count += 1;
  sum += num
mean = sum/count
# print("... the program asks for numbers")
# print(f"Numbers typed in {count} ")
print(f"The sum of numbers is {sum}")
# print(f"The Mean of numbers is {mean}")
# print(f"Positive Numbers:{posCount}")
# print(f"Negative Numbers:{negCount}")