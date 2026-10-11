hourlyWage = float(input("Hourly wage:"))
hoursWorked = float(input("Hours worked:"))
dayOfTheWeek = input("Day of the week:")

if dayOfTheWeek == "Sunday":
  dailyWages= hourlyWage*hoursWorked*2
  print(f"Daily wages: {dailyWages} euros");
else:
  dailyWages= hourlyWage*hoursWorked
  print(f"Daily wages: {dailyWages} euros");
