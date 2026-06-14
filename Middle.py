firstLetter = input("1st letter:")
secondLetter = input("2nd letter:")
thirdLetter = input("3rd letter:")
lst = [firstLetter,secondLetter,thirdLetter]
lst.sort()
print(f"The letter in the middle is {lst[1]}")