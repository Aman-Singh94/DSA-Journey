a=[10,20,30,40,50,60,70]
#1  print all number in array 
for i in range (len(a)):
    print(a[i])   


#2sum of all number in array
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print("sum of all number is ",sum)


#3find any number index
num=int(input("enter your number "))
for i in range(len(a)):
    if a[i]==num:
        print(f"mil gaya ooy {i} index par")

#3.1
mil_gaya = False                
for i in range(len(a)):
    if a[i] == num:
        print(f"mil gaya ooy, {i} index par")
        mil_gaya = True        
        break                    

if not mil_gaya:                
    print(f"esa koi number {num} hai hei nhi")