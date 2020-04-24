amount_seconds = input("Введите количество секунд:")
amount_seconds = int(amount_seconds)
hour = amount_seconds // 3600
minutes = (amount_seconds - (hour * 3600)) // 60
seconds = amount_seconds - hour * 3600 - minutes * 60
print("Вы ввели {} секунд: {}ч {}м {}с" .format(amount_seconds, hour, minutes, seconds))

