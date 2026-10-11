a = input("1st letter:")
b = input("2nd letter:")
c = input("3rd letter:")
if a>b>c or a<b<c:
  middle = b;
elif b<a<c or b>a>c:
  middle = a;
else:
  middle =c
print("The letter in the middle is",middle)