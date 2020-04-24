A = int(input("Введите ваш первый результат:"))
b = int(input("Введите вашу цель"))
d = 1
print("{}-й день: {}".format(d, A))
if A == b:
    print("Поздравляю!")
elif A > b:
    print("Введите корректные данные")
else:
    while A <= b:
        A = A + 0.1 * A
        d = d + 1
        print("{}-й день: {:.1f}".format(d, A))









#while A >= b:
#   if A < b:
        #A = A + 0.1 * A
       # d = d + 1
        #print("{}-й день: {}".format(d, A))
#    elif A == b:
#        print("Ты достиг цели")
#    else:
#        print("Введите коректные данные!!")