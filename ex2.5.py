
my_list = [7, 5, 3, 3, 2]
enter = int(input("Enter number: "))
srh = my_list.count(enter)
for element in my_list:
    if srh > 0:
        i = my_list.index(enter)
        my_list.insert(i, enter)
        break
    else:
        if enter > element:
            big = my_list.index(element)
            my_list.insert(big, enter)
            break
        elif enter < my_list[len(my_list) - 1]:
            my_list.append(enter)

print(my_list)

