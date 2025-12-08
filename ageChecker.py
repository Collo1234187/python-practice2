from datetime import datetime

year_of_birth = int (input("enter your year of birth? "))
current_year = datetime.now().year
age = current_year - year_of_birth

print(f"you are {age} years olds")

if age<=18:
    print("your are under age")
elif age > 18 and age<=30:
    print("you are and adult")
else:
    print("the year entered is invalid")