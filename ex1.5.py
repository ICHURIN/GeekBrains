profit = int(input("Ваша прибыль:"))
costs = int(input("Ваши расходы:"))
if profit - costs <= 0:
    print("Ваше предприятие не получает прибыль")
else:
    emp = int(input("Введите количество человек в вашей компании:"))
    profitemp = (profit - costs) / emp
    print ("Подравляем! Ваша прибыль в расчете на одного сотрудника составлет: {}".format(profitemp))
