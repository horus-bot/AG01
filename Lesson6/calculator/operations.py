def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero."
    return a/b

if __name__=="__main__":
    print("Addition:",add(5,3))
