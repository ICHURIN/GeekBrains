

def sum_func ():
    final = 0
    uslovie = 1
    while uslovie == 1:
        vvod = input('Input numbers or Q for quit - ').split()
        tek_result = 0
        for i in range(len(vvod)):
            if vvod[i] == 'q' or vvod[i] == 'Q':
                uslovie = 0
                break
            else:
                tek_result = tek_result + int(vvod[i])
        final = final + tek_result
        print("Tekushy result = {}".format(final))
    return final

print("Itogovaya summa - {}".format(sum_func()))


