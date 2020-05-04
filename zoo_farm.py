# 02.05.2020
# zoo farm

import random

class Animal(object):
    """Zoo farm"""
    total = 0
    mistake = "Wrong input! Try again!"
    farm = []

    def __init__(self, critter, hunger = 0, boredom = 0):
        self.critter = critter
        self.hunger = hunger
        self.boredom = boredom
        self.hunger = random.randrange(10)
        self.boredom = random.randrange(15)
        print(f"A {self.critter} appeared on the farm.")
        __class__.total += 1

    def __str__(self):
        return f"\n{self.critter}\nHunger: {self.hunger}\nBoredom: {self.boredom}"

    def eat(self):
        food = input(f"\nHow much food to give this animal? {self.critter} /1-10: ")
        try:
            food = int(food)
            if 0 < food <= 10:
                print("Thanks!")
                self.hunger -= food
                if self.hunger < 0 :
                    self.hunger = 0
            else:
                print(__class__.mistake)
                self.eat()
        except ValueError:
            print(__class__.mistake)
            self.eat()

    def to_play(self):
        time = input(f"\nHow many minutes to play with the animal? {self.critter} /1-10: ")
        try:
            time = int(time)
            if 0 < time <= 10:
                print("Wiiii...")
                self.boredom -= time
                if self.boredom < 0 :
                    self.boredom = 0
            else:
                print(__class__.mistake)
                self.to_play()
        except ValueError:
            print(__class__.mistake)
            self.to_play()


    @staticmethod
    def print_mistake_animals():
        print(f"Wrong input, you have to choose between 1 and {len(__class__.farm)}. Try again!")

    @staticmethod
    def status():
        print(f"There are {__class__.total} animals on the farm")

    @staticmethod
    def add_animal(animal):
        __class__.farm.append(animal)

    @staticmethod
    def names():
        critters = []
        for animal in __class__.farm:
            name = animal.critter
            critters.append(name)
        return critters

    @staticmethod
    def feed():
        animal = None
        while animal != "0":
            print("\nWhat animal to feed?")
            __class__.display()
            try:
                animal = int(input("\nYour choice: "))
                if animal > len(__class__.farm):
                    __class__.print_mistake_animals()
                elif animal == 0:
                    return
                else:
                    __class__.farm[animal - 1].eat()
            except ValueError:
                __class__.print_mistake_animals()
        __class__.pass_time()

    @staticmethod
    def display():
        critters = Animal.names()
        print("0 - exit")
        for number, name in enumerate(critters, start=1):
            print(f"{number} - {name}")

    @staticmethod
    def play():
        animal = None
        while animal != 0:
            print("\nWhich animal to play with?")
            __class__.display()
            try:
                animal = int(input("\nYour choice: "))
                if animal > len(__class__.farm):
                    __class__.print_mistake_animals()
                elif animal == 0:
                    return
                else:
                    __class__.farm[animal - 1].to_play()
            except ValueError:
                __class__.print_mistake_animals()
        __class__.pass_time()

    @staticmethod
    def check_condition():
        for animal in __class__.farm:
            print(animal)
        __class__.pass_time()

    @staticmethod
    def pass_time():
        for animal in __class__.farm:
            animal.hunger += 1
            animal.boredom += 1
   
def main():
    animal_1 = Animal("Cow")
    animal_2 = Animal("Pig")
    animal_3 = Animal("Rabbit")
    Animal.add_animal(animal_1)
    Animal.add_animal(animal_2)
    Animal.add_animal(animal_3)
    Animal.add_animal(Animal("Horse"))
    Animal.add_animal(Animal("Chicken"))
    Animal.add_animal(Animal("Duck"))
    Animal.add_animal(Animal("Turkey"))
    Animal.add_animal(Animal("Goose"))
    Animal.status()

    choice = None
    while choice != "0":
        print \
        ("""
        My farm
        0 - exit
        1 - check condition for all animals
        2 - feed
        3 - play
        """)
        choice = input("\nYour choice: ")
        print()
    
        if choice == "0":
            print("Bye!")

        elif choice == "1":
            Animal.check_condition()

        elif choice == "2":
            Animal.feed()

        elif choice == "3":
            Animal.play()

        else:
            print(Animal.mistake)

main()