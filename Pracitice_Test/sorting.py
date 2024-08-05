lst = [99,10,12,1,5,6,2]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

print(lst)