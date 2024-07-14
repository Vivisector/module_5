class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def isinst(self):
        return isinstance(self.num_of_floors, int)

    def isClass(self, House):
        return isinstance(self, House)

    def __lt__(self, other):
        if self.isinst() and other.isinst():
            return self.num_of_floors < other.num_of_floors
        else:
            raise TypeError('число этажей должно целым положительным числом!')

    def __le__(self, other):
        return self.num_of_floors <= other.num_of_floors

    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors

    def __eq__(self, other):
        return self.num_of_floors == other.num_of_floors

    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.num_of_floors + value)
        raise TypeError('кол-во этажей должно целым положительным числом!')

    def __iadd(self, value):
        if isinstance(value, int):
            self.num_of_floors += value
            return self
        raise TypeError('кол-во этажей должно целым положительным числом!')

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f'Название: «{self.name}», кол-во этажей: {self.num_of_floors}'


#### служебная функция-переводчик результата сравнения
def translate_bool(value):
    return 'Да' if value else 'Нет'

'''''рабочие процедуры'''''
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(f'Число этажей у «{h1.name}» и «{h2.name}» равно? - {translate_bool(h1==h2)}')  # __eq__
h1 = h1 + 10  # __add__
print(f'Теперь число этажей у «{h1.name}» равно {h1.num_of_floors}')
print(f'Теперь число этажей у «{h1.name}» и «{h2.name}» равно? - {translate_bool(h1==h2)}')  # __eq__

h1 += 10  # __iadd__
print(f'Теперь число этажей у «{h1.name}» равно {h1.num_of_floors}')

h2 = 10 + h2 # __radd__
print(f'Теперь число этажей у «{h2.name}» равно {h2.num_of_floors}')

# print(h1 > h2) # __gt__
print(f'Число этажей у «{h1.name}» больше, чем у «{h2.name}»? - {translate_bool(h1>h2)}, равно')

# print(h1 >= h2) # __ge__
print(f'Число этажей у «{h1.name}» больше или равно, чем у «{h2.name}»? - {translate_bool(h1>=h2)}, равно')

# print(h1 < h2) # __lt__
print(f'Число этажей у «{h1.name}» меньше, чем у «{h2.name}»? - {translate_bool(h1<h2)}, равно')

# print(h1 <= h2) # __le__
print(f'Число этажей у «{h1.name}» меньше или равно, чем у «{h2.name}»? - {translate_bool(h1<=h2)}, равно')

# print(h1 != h2) # __ne__
print(f'Число этажей у «{h1.name}» не равно числу этажей у «{h2.name}»? - {translate_bool(h1!=h2)}, равно')