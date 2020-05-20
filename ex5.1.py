
with open('11.txt', 'w+') as f:
    while True:
        current = input('data: ')
        if current == "": break
        f.write(f'{current}\n')
