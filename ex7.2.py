
class general:
    def __init__(self, razmer, rost):
        self.razmer = razmer
        self.rost = rost
    def razmer_palto(self):
        s1 = self.razmer / 6.5 + 0.5
        return s1
    def rarmer_kostuma(self):
        s2 = self.rost * 2 + 0.3
        return s2

    @property
    def full_cost(self):
        return str(f'Площадь ткани {(self.razmer / 6.5 + 0.5) + (self.rost * 2 + 0.3)}')


class Palto(general):
    def __init__(self, razmer, rost):
        super().__init__(razmer, rost)
        self.razmer_palto_1 = round(self.razmer / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь пальто {self.razmer_palto_1}'


class Kostum(general):
    def __init__(self, razmer, rost):
        super().__init__(razmer, rost)
        self.razmer_kostum_1 = round(self.rost * 2 + 0.3)

    def __str__(self):
        return f'Площадь костюма {self.razmer_kostum_1}'

kost = Kostum(3, 4)
pal = Palto(2, 4)
print(pal)
print(kost)
print(kost.full_cost)
print(pal.full_cost)


