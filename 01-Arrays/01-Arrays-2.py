#Reverse an array in-place


arr = [12, 45, 2, 67, 33, 89, 5]
left = 0                  # shuru wali position
right = len(arr) - 1      # aakhri position (len-1 isliye kyunki index 0 se start hota hai)

while left < right:        # jab tak dono milte nahi (ya cross nahi karte) — chalte raho
    arr[left], arr[right] = arr[right], arr[left]   # dono ki jagah badlo (swap)
    left += 1             # left ek kadam aage
    right -= 1            # right ek kadam peeche
print(arr)


#In Python
arr1 = [12, 45, 2, 67, 33, 89, 5]
arr1[:] = reversed(arr1)
print(arr1)

