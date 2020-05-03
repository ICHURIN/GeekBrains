
def int_func(stroka):
    stroka = stroka.title()
    return stroka

vvod = []
vvod = input("Vvedite stroku:").split()
for el in range(len(vvod)):
    vvod[el] = int_func(vvod[el])

print(' '.join(vvod))
