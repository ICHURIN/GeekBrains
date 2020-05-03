
a = int(input('первое'))
b = int(input("второе"))
c = int(input("третье"))


def max_of_two(a,b,c):
    all = [a, b, c]
    result = []
    pervoe = max(all)
    result.append(pervoe)
    all.remove(pervoe)
    vtoroe = max(all)
    result.append(vtoroe)
    final = sum(result)
    return final

print(max_of_two(a, b, c))