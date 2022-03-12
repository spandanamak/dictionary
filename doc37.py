n={}
key=["x","y","z"]
values=[[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40]]
for i in key:
    for j in values:
        n[i]=j
        values.remove(j)
        break
n=int(input("enter no:"))
print(n,["x"][n])
print(n,["y"][n])
print(n,["z"][n])
