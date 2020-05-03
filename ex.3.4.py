

def my_func(chislo_1, chislo_2):
    stepen = chislo_1 ** chislo_2
    return stepen
print(my_func(3, -3))

def my_func_manual(chislo_1_m, chislo_2_m):
    step_abs = abs(chislo_2_m)
    per_step = 1 / chislo_1_m
    final = 1
    if step_abs == 1:
        final = 1 / chislo_1_m
        return final

    while step_abs > 0 :
        final = final * per_step
        step_abs = step_abs - 1
    return final

print(my_func_manual(3, -3))