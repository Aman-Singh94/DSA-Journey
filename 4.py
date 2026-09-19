#Armstrong Number Explained 
a=int(input("enter a number "))
num=a
r=0
while num>0:
    id=num%10
    r=(r*10)+id
    num=num//10

if a==r:
    print("it is armstrong number ")  
else:
    print("it is not a armstrong number")
