
my_list = ["Winter", "Spring", "Summer", "Autumn"]
Dict_moth = {"Summer": (6, 7, 8), "Winter":(1,2,12), "Spring":(3,4,5), "Autumn":(9,10,11)}
number = int(input("Enter number of month(1-12):"))
if number == 12 or number == 1 or number == 2:
    print("in my_list     {} - {}".format(number, my_list[0]))
elif number == 3 or number == 4 or number == 5:
    print("in my_list     {} - {}".format(number, my_list[1]))
elif number == 6 or number == 7 or number == 8:
    print("in my_list     {} - {}".format(number, my_list[2]))
elif number == 9 or number == 10 or number == 11:
    print("in my_list     {} - {}".format(number, my_list[3]))
for key in Dict_moth.keys():
    if number in Dict_moth[key]:
        print("in Dict_month   {} - {}".format(number, key))



