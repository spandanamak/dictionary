d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
n=input("enter")
for i in range (len(d)):
    if d[i]["id"]==n:
        del d[i]
        break
    elif d[i]["color"]==n:
        del d[i]
        break
print(d)

