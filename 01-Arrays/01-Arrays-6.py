#Move all zeros to the end
nums =[1,3,8,0,8,0,7,9,0,8,0]
# Input list


new_list = []          # khaali list banayi — yahan answer banega

# pehle saare non-zero numbers utha lo
for num in nums:            # list ke har number pe jao
    if num != 0:           # kya number 0 nahi hai?
        new_list.append(num)   #toh new list me daal do

#ab zeroes gino
count = 0                    # zero ka counter
for num in nums:             # phir se har number pe jao
    if num == 0:             # kya yeh zero hai?
        count = count + 1    # haan? toh count badha do

# utne zeroes end me daal do
for i in range(count):       # jitne zeroes the, utni baar
    new_list.append(0)       # ek zero daal do



print(new_list)

