# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('5.5.txt', 'w+') as f:
    vvod = input("Vvedite posledovatel'nost' chisel: ")
    f.write(vvod)

with  open('5.5.txt', 'r') as f:
    my_list = f.read()
    my_list = my_list.split()
    summat = 0
    for i in my_list:
        my_list[i] = int(my_list[i])
        summat += my_list[i]
    print(my_list)
    print(summat)
