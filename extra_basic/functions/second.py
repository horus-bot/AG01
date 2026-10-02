def max(*args):
    temp=args[0]
    for i in args :
        if i > temp:
            temp = i
    return temp        
    

print(max(1,2,3,4,89))