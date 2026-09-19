#Armstrong Number Explained 
a = int(input("enter a number "))

num = a

t = 0

l = len(str(a))

while num > 0:

    id = num % 10

    t = t + (id ** l)

    num = num // 10
    t == a
print(t)
