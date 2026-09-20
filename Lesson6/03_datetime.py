###
import datetime

now = datetime.datetime.now()

print("Current date and time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

##
import datetime

today = datetime.date.today()

print("Today's date:", today)



###
import datetime

birth_year = int(input("Enter your birth year: "))

current_year = datetime.date.today().year

age = current_year - birth_year

print("Your approximate age:", age)