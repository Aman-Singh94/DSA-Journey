#Check if array is sorted
arr=[2,4,8,12,13,25]
is_short=True
for i in range (len(arr)-1):
    if arr[i]>arr[i+1]:
        is_short=False
        break
if is_short==True:
    print("Array is sorted")
else:
    print("Array is not sorted")
    