
list_tovar = []
tovar_tuple = ()
a = ()
l = 1
task2 = {}
while input("New good?(yes/no)") == "yes":
    n = input("Vvedite nazvanie:")
    p = input("Vvedite price:")
    a = input("Vvedite kolichestvo:")
    m = input("Vvedite ed.izmereniya:")
    parametri = dict({'name': n, 'price': p,
                 'amount': a, 'masure':m})
    list_tovar.append((l, parametri))
    l = l + 1
print(list_tovar)
