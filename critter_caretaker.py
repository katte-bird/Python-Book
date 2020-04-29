# 29.04.2020
# питомец, о котором можно заботиться

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger = 0, boredom = 0):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5 :
            m = "прекрасно"
        elif 5 <= unhappiness <= 10 :
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Привет! Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "\n")
        print("голод", self.hunger, "скука", self.boredom)
        self.__pass_time()

    def eat(self, food = 4):
        print("Мрр... спасибо!")
        self.hunger -= food
        if self.hunger < 0 :
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= 4
        if self.boredom < 0 :
            self.boredom = 0
        self.__pass_time()

def main():
        crit_name = input("Как назвать зверюшку? ")
        crit = Critter(crit_name)
        choice = None
        while choice != "0":
            print \
            ("""
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии
            2 - Покормить
            3 - Поиграть
            """)
            choice = input("Ваш выбор: ")
            print()

            # выход
            if choice == "0":
                print("До свидания!")

            # беседа
            elif choice == "1":
                crit.talk()

            # кормление
            elif choice == "2":
                crit.eat()

            # игра
            elif choice == "3":
                crit.play()

            # непонятный ввод пользователя
            else:
                print("В меню нет такого пункта", choice)

# основная часть
main()