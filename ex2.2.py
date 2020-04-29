
my_list = []
print("Vvedite znacheniya v spisok, dlya zaversheniya vvoda vvedite 'ok'")
v = " "
n = " "
while v != "ok":
    v = input("Vvedite element spiska")
    my_list.append(v)
    if v == "ok":
        n = my_list.pop()
print(my_list)
l = len(my_list)
print("Dlina spiska ={}".format(l))
for i in range(1, l, 2):
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)



