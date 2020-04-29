# 28.04.2020
# атрибуты класса и статические методы

class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("\nВсего зверюшек сейчас", Critter.total)
    def __init__(self, name):
        self.name = name
        print("Создана новая зверюшка по имени: ", self.name)
        Critter.total += 1

# основная часть
print("Нахожу значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("\nСоздаю зверюшек:")
crit_1 = Critter("Раз")
crit_2 = Critter("Два")
crit_3 = Critter("Три")
Critter.status()
print("\nОбращаюсь к атрибуту класса через объект:", end=" ")
print(crit_1.total)
input("\n\nНажмите Enter, чтобы выйти...")