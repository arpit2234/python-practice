yearAge=int(input("Whats your Age/Year of birth"))

isAge=False
isYear=False

if yearAge<125:
    isAge=True

else :
    isYear=True

if yearAge<1900 and isYear:
    print("you seem to be the oldest person on earth")
    exit()
if(yearAge>2020):
    print("you are not born yet")
    exit()

if isAge:
    yearAge=2020-yearAge



print(f"You will be 100 years old in {yearAge+100}")