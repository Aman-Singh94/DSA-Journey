# Print All Factors of a Given Number
number=int(input("enter a number you want to chek the factor "))
num=number
n=int(number/2)
for i in range(1,n+1):
    if num%i==0:
        print(i)

    