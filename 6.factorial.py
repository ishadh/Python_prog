n=int(input("Enter the number whose factorial you want to find out: \n"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
    print(f"the factorial of {n} is : {factorial}")

