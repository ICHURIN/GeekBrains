
my_list = []
while True:
    current = input('data: ')
    if current == "": break
    my_list.append(current)
with open('5.2.txt','w+') as f:
    f.writelines("%s\n" % line for line in my_list)

with open('5.2.txt','r') as f:
    new_list = []
    for line in f.readlines():
        new_list = line.split()
        print(new_list)
        print(f'{line.strip()} - kol-vo slov v stroke {len(new_list)}')
    f.seek(0)
    print(f"Kol-vo strok {len(f.readlines())}")


