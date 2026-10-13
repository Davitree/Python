string = input("Please type in a sentence:")
count = 0
i = 0
while i <= len(string)-1:
   if i == 0:
      print(string[0])
   if string[i] == " ":
      print(string[i+1])   
   i += 1

  