n=int(input("Enterthe value of n: "))
sum=0
if n<=0:
    print("Enter a positive number!!!")
while n>0:
    sum=sum+n
    n=n-1
print("Sum of n natural numbers is:",sum)
