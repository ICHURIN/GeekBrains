# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} В движении'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} = {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скороть  {self.name} = {self.speed}')

        if self.speed > 40:
            return f'{self.name} превышает скоростной режим'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed}')

        if self.speed > 60:
            return f'{self.name} превышает скоростной режим'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - Полиция'
        else:
            return f'{self.name} - не Полиция'


ferrari = SportCar(140, 'Red', 'Ferrari', False)
kia = TownCar(50, 'Brown', 'kia', False)
vaz = WorkCar(70, 'Blue', 'vaz', False)
ford = PoliceCar(90, 'Silver',  'ford', True)
print(ferrari.show_speed())
print(kia.show_speed())
print(vaz.show_speed())
print(ford.police())
print(ford.show_speed())
print(f'Если сейчас {ford.turn_left()} то {ferrari.stop()} ')