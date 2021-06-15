'''
f=open("isha.txt","r")
data=f.read()
print (data)
f.close()

f=open("isha.txt","w")
f.write("experiments")
f.close()

f=open("isha.txt","a")
f.write("\n I am appending")
f.close()

with open("isha.txt","r") as f:
    a=f.read()
print(a)
'''
with open("isha.txt","w") as f:
    a=f.write("by Isha")
print(a)