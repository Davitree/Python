string = input("Word:")
n = len(string)
gaps = (28 - n) //2
gap = int(gaps)


print("*" * 30)
print("*" + " "*gap+string+" "*(28-n-gaps)+"*")
print("*" * 30)
