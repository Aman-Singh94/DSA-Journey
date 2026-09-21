a = [1, 3, 0, 6, 5, 0, 8, 0, 6]

new = 0                    # yahan agla non-zero jayega
for i in range(len(a)):
    if a[i] != 0:
        a[new], a[i] = a[i], a[new]   # swap karo
        new += 1

print(a)   # [1, 3, 6, 5, 8, 6, 0, 0, 0]

