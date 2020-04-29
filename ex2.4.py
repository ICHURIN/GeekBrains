
String = input("Enter string :").split()
i = 1
for el in String:
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}) {el}")
    i = i + 1
