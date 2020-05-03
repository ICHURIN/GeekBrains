def delenie(chilo_1, chislo_2):

    if chislo_2 != 0:
        summa = chilo_1 / chislo_2
        return summa
    else:
        result = 'error'
        return result
a = int(input("Chilo-1:"))
b = int(input("Chislo-2:"))
print(delenie(a,b))
5