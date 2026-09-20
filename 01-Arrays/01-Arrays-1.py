numbers = [12, 45, 2, 67, 33, 89, 5]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))

#dsa
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)