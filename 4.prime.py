n=int(input("Enter the number:"))
prime=True
for i in range(2,n):
    if(n%i ==0 ):
        prime=False
        break
if prime:
    print("Prime number")
else:
    print("Composite number")