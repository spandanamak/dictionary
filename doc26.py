dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in dict:
    print(i,end="")
print("\n")
a=[]
for i in dict:
    b=dict[i]
    a.append(b)
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=a[i][j]
        print(sum,end="")
        j+=1
    print()
    i+=1


