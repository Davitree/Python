value = int(input("Value of gift:"))
if value < 5000:
  print("No tax!");
elif 5000 <= value < 25000:
  x = 100 + ((value - 5000)*0.08);
  print(f"Amount of tax: {x} euros")
elif 25000 <= value < 55000:
  x = 1700 + ((value -25000)*0.1);
  print(f"Amount of tax: {x} euros")
elif  55000 <= value < 200000:
  x = 4700 + ((value - 55000)*0.12);
  print(f"Amount of tax: {x} euros")
elif 200000 <= value < 1000000:
  x = 22100 + ((value - 200000)*0.15);
  print(f"Amount of tax: {x} euros");
elif value >100000:
   x = 142100 + ((value - 1000000)*0.17)
   print(f"Amount of tax: {x} euros")