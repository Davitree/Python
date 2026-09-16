string = input("Word:")
n = len(string)
gaps = (28 - n) /2
gap = int(gaps)

if n % 2 == 0:
  print("*" * 30)
  print("*" + " "*gap+string+" "*gap+"*")
  print("*" * 30)
else:
  print("*" * 30)
  print("*" + " "*(gap-1)+string+" "*gap+"*")
  print("*" * 30)