class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors
        #House.houses_history.append(self.name)

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')
        House.houses_history.remove(self.name) # обновление списка построенных комплексов


h1 = House('ЖК Эльбрус', 10)
print(f'Итого построено: {House.houses_history}')
h2 = House('ЖК Акация', 20)
print(f'Итого построено: {House.houses_history}')
h3 = House('ЖК Матрёшки', 20)
print(f'Итого построено: {House.houses_history}')

print(f'Было построено [до удаления))]: {House.houses_history}')

# Удаление объектов
del h2

del h3

print(f'Осталось: {House.houses_history}')
