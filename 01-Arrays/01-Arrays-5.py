#Remove duplicates from sorted array
arr = [1, 1, 2, 2, 2, 3, 4, 4]
arr = list(set(arr))
print(arr)

#Start: i = 0 (arr[0]=1 unique maana)
#j=1: arr[1]=1, arr[i]=1 — same, skip
#j=2: arr[2]=2 ≠ 1 — naya! i=1, arr[1]=2 → [1, 2, ...]
#j=3: 2 == 2, skip
#j=4: 2 == 2, skip
#j=5: 3 ≠ 2 — naya! i=2, arr[2]=3 → [1, 2, 3, ...]
#j=6: 4 ≠ 3 — naya! i=3, arr[3]=4 → [1, 2, 3, 4, ...]
#j=7: 4 == 4, skip
#Remove duplicates from sorted array (in-place)

arr1 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 9,]

i = 0                                  # last unique element ka index

for j in range(1, len(arr1)):            # j pehle se end tak scan karo
    if arr1[j] != arr1[i]:                # naya unique element mila?
        i += 1                          # i aage badho
        arr1[i] = arr1[j]                 # usko unique walo ke end me rakho

print("Unique elements:", arr1[:i + 1])  # pehle i+1 elements hi answer hai

