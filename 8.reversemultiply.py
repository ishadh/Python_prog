n=int(input("Enter the number:"))
a=range(1,11)
b=reversed(a)
for i in b:
    print(f"{n} x {i}= {n*i}")