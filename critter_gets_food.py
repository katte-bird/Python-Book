# 30.04.2020
# pet care

class Critter(object):
    """Virtual pet"""

    def __init__(self, name, hunger = 0, boredom = 0):
        print("A new pet was born!")
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
            m = "great"
        elif 5 <= unhappiness <= 10 :
            m = "not bad"
        elif 11 <= unhappiness <= 15:
            m = "so-so"
        else:
            m = "awful"
        return m

    def talk(self):
        print("Hi! My name is", self.name, "and now I feel", self.mood, "\n")
        print("hunger -", self.hunger, "boredom -", self.boredom)
        self.__pass_time()

    def mistake(self):
        print("Incorrect input, you need to select a number from 1 to 10. Try again")

    def eat(self):
        food = input("\nHow much food to give your pet? (1-10):")
        try:
            food = int(food)
            if 0 < food <= 10:
                print("Mrr ... thanks!")
                self.hunger -= food
                if self.hunger < 0 :
                    self.hunger = 0
            else:
                self.mistake()
                self.eat()
        except ValueError:
            self.mistake()
            self.eat()
        self.__pass_time()


    def play(self):
        fun = input("\nHow many minutes do you want to play with your pet? (1-10):")
        try:
            fun = int(fun)
            if 0 < fun <= 10:
                print("Wiii!")
                self.boredom -= fun
                if self.boredom < 0 :
                    self.boredom = 0
            else:
                self.mistake()
                self.play()
        except ValueError:
            self.mistake()
            self.play()
        self.__pass_time()

def main():
        crit_name = input("What is the name of your pet? ")
        crit = Critter(crit_name)
        choice = None
        while choice != "0":
            print \
            ("""
            My pet
            0 - exit
            1 - check well-being
            2 - to feed
            3 - to play
            """)
            choice = input("Your choice: ")
            print()

            # exit
            if choice == "0":
                print("Bye!")

            # talk
            elif choice == "1":
                crit.talk()

            # to feed
            elif choice == "2":
                crit.eat()

            # to play
            elif choice == "3":
                crit.play()

            # wrong choice
            else:
                print("There is no such item in the menu", choice)

# main code
main()