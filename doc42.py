a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
b=int(input("enter your value"))
for i in a.values():
    if b==i:
        print("all are 12 in the dictionary")
    else:
        print("all are not in the dictionary")
