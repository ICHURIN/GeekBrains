Figure1 = input("Введите целое положительное число:")
Figure = int(Figure1)
maximum = Figure % 10
Figure = Figure // 10
while Figure > 0:
    if Figure % 10 > maximum:
        maximum = Figure % 10
    Figure = Figure // 10
print ("цифра {} в числе {} является максимальной" .format(maximum, Figure1))









