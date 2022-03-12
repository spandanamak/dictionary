d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in d1:
    for j in d2:
        if i in d2:
            dic[i]=d1[i]+d2[i]
        elif j not in d1:
            dic[j]=d2[j]
        elif i not in d2:
            dic[i]=d1[i]
print(dic)












