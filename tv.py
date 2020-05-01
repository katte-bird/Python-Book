# 30.04.2020
# tv as an object

class TV(object):
    """TV"""
    def __init__(self, name, tv_channel = 0, volume = 5):
        self.name = name
        self.tv_channel = tv_channel
        self.volume = volume
        print("TV object", self.name, "created")

    def talk(self):
        print("\nWelcome to the", self.name, "TV control panel")

    def channel(self):
        print("You can select any channel from 1 to 10")
        tv_channel = input("\nWhich channel would you like to watch? ")
        try:
            tv_channel = int(tv_channel)
            if 0 < tv_channel <= 10:
                self.tv_channel = tv_channel 
                print("\nChannel", tv_channel, "switched on! Enjoy watching!")
            else:
                print("There is no such channel. Try again")
                self.channel()
        except ValueError:
            print("There is no such channel. Try again")
            self.channel()

    def sound(self):        
        while True:
            print("\n\nCurrent sound level:", self.volume, "\nThe maximum volume level is 10")
            print("""
                  <  - decrease by one
                  >  - increase by one
                  x  - exit
                  """)
            sound_volume = input("Your choice: ")
            if sound_volume == "<":
                if self.volume > 0:
                    self.volume -= 1
                elif self.volume == 0:
                    print("Your sound level is at the minimum")
            elif sound_volume == ">":
                if self.volume < 10:
                    self.volume += 1
                elif self.volume == 10:
                    print("Your sound level is at the maximum")
            elif sound_volume == "x":
                return
            else: 
                print("There is no such option. Try again")
            

def main():
    tv = TV("Sony")
    tv.talk()
    choice = None
    while choice != "0" :
        print("""\n
              0 - switch off
              1 - select channel
              2 - set up sound 
              """)
        choice = input("Your choice: ")
        if choice == "0":
            print("Switch off...")
        elif choice == "1":
            tv.channel()
        elif choice == "2":
            tv.sound()
        else:
            print("There is no such option. Try again")
    
# main code
main()