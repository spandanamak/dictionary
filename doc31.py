dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
a=[]
for b in dict:
    a.append(dict[b])
max=0
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
max2=0
for j in range(len(a)):
    if a[j]>max2:
        if a[j]<max:
            max2=a[j]
max3=0
for k in range(len(a)):
    if a[k]>max3:
            if a[k]<max2:
                max3=a[k]
print("first maximum:",max)
print("second maximum:",max2)
print("third maximum",max3)

