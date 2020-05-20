# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import json
slov = {}

my_dict = {}
# заполнение словаря и запись в файл
while True:
    surname = input('Surname:')
    if surname == "": break
    salary = int(input(f'Enter salary for {surname}'))
    my_dict.update({surname: salary})
with open('5.3.json','w+') as f:
        json.dump(my_dict, f)

# загрузка из файла
new_dict = {}
with open ('5.3.json','r') as f:
    new_dict.update(json.load(f))

list_of_values = []
for value in new_dict.values():
    if value < 20000:
        list_of_values.append(value) # все значения , которые меньше 20000 в этом листе

def list_small(dict_source): #функция вывода в лист фамилий меньше 20000
    spisok_el = []
    d = dict_source
    rev_d = {}
    for k, v in d.items():
        rev_d[v] = rev_d.get(v, []) + [k]
    for key in rev_d:
        if key < 20000:
          spisok_el.append(rev_d.get(key))
    return spisok_el

def middle_keys(dict_vvod): #  функция  вычисления среднего значения
    a = {}
    a = dict_vvod
    b = []
    total = 0
    fin_total = 0
    for value in a.values():
        b.append(value)
    for value in a.values():
        total += value
    fin_total = total / len(b)
    return fin_total
print("Список сотрудников, ЗП которых меньше 20000: ", ",".join(str(x) for x in list_small(new_dict)))
print(f"Среднее ЗП по компании:{middle_keys(new_dict)}")


