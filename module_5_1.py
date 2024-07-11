class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor < self.floors:
            print(f'Нижележащие этажи в {self.floors}-этажном «{self.name}»:')
            for i in range(1, new_floor):
                print(i, end=' ')
            print()
        else:
            print(f'\n{new_floor}-го этажа в {self.floors}-этажном комплексе «{self.name}» не существует')


elbrus = House('ЖК Эльбрус', 40)
elbrus.go_to(5)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(7)
h2.go_to(10)