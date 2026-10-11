password = input("Password:")
while True:
  repeatPassword = input("Repeat Password:")
  if repeatPassword != password:
    print("They do not match!");
  else:
    print("User account created!")
    break