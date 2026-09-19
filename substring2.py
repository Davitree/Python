string = input("Please type in a string:")
i=1
while i <= len(string): 
  print(string[len(string)-i:len(string)])
  i += 1

