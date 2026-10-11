print("Welcome to the tip Calculator!!")
totalBill = float(input("What was the total bill? $ "))
tip = int(input("How much would you like to give ? 10, 12 , or 15 ?"))
noOfPeople = int(input("How many people to split the bill ?"))

price = ((totalBill +totalBill *(tip/100) )/noOfPeople)
print(round(price,2))