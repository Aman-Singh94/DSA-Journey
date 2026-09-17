#Count the Number of Digits in an Integer
a = 2345432
count = 0
while a > 0:
    count += 1
    a = a // 10
print(count)
