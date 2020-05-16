
import random
my_list = []
for i in range(10):
    my_list.append(random.randint(0, 20))
print(f'Изначальный список {my_list}')
new_list = [el for el in my_list if el > my_list[i-1]]
print(new_list)



