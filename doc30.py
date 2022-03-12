dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
d={}
for i in dict:
    c=" "
    j=0
    while j<len(i):
        if i[j]!=" ":
            c+=i[j]
        j+=1
    d[c]=dict[i]
print(d)