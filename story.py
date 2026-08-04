codes = ""
prevWord = ""
while True:
  code = input("Please type in a word:")
  # codes +=  code + " "
  if code == "end" or code == prevWord:
    # print(codes);
    break
  
  if codes == "":
    codes = code
  else:
    codes= codes+" "+code;
  prevWord = code

print(codes)