#Find second largest element

arr = [12, 45, 2, 67, 33, 89, 5]

arr.sort()
print("Second largest:", arr[-2])   # -2 = second last index



#12 → largest=12
#45 → 45>12, to second=12, largest=45
#67 → 67>45, to second=45, largest=67
#89 → 89>67, to second=67, largest=89
#5  → na bada hai na second se bada, ignore

largest = second = float('-inf')   # dono ko minus infinity se start karo

for num in arr:
    if num > largest:
        second = largest    # purana largest ab second largest ban gaya
        largest = num       # naya largest mil gaya
    elif num > second and num != largest:
        second = num

print("Second largest:", second)