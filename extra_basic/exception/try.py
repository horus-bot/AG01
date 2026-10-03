try:
    a = int(input("give a number dumbass"))
    print(10/a)
except ZeroDivisionError:
    print("zero cant be a divisor")

except ValueError:
    print("enter a valid number ")