a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))

def num(a,b,c):
    if (a>b):
        if (a>c):
            return a
        else:
            return c
    else:
        return b
    if (b>c):
        if (b>a):
            return b
        else:
            return a
    else:
        return c
max=num(a,b,c)
print("The greatest value is: " + str(max))
