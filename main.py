def newage (num1,num2):
  sumage = num1 + num2
  return sumage
def agediff (num1,num2):
  ageminus = num1 - num2
  return ageminus
computerAge = 20
print("Hi there! Nice to meet you, I am",computerAge,"years old")
currentAge = int(input("What is your current age? "))
addYears = int(input("How many years do you want to add? "))
usernewage = newage(currentAge,addYears)
if usernewage > computerAge:
  agecalcdiff = agediff(usernewage,computerAge)
  oldyoung = "older"
elif computerAge > usernewage:
  agecalcdiff = agediff(computerAge,usernewage)
  oldyoung = "younger"
else:
  oldyoung = 0
print("You will be",usernewage,"years old in",addYears,"years!")
if oldyoung != 0:
  print("Did you know that in",addYears,"years, you will be",agecalcdiff,"years",oldyoung,"than me today?")
else:
  print("Wow! You will be the same age as me today in",addYears,"years from now!")
