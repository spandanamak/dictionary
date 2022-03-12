x={"key1":1,"key2":3,"key3":2}
y={"key1":1,"key2":2}
for i in x:
    for j in y:
        w=x[i]
        r=y[j]
        if i==j and w==r:
            print(i,":",w,"is present in both x and y")
