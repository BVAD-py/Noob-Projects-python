import random 
import time

class Character:
    def __init__(self):
        self.name = random.choice(["Eren","Reiner", "Luffy","Croc","Naruto","Pain"])
        self.hp = random.randint(90,180)
        self.attack = random.randint(40,85)
        self.defense = random.randint(60,120)
        self.speed = random.randint(60,120)
    
    def showcard(self):
        print("==========================================")
        print(self.name.center(42))
        print("==========================================")
        print("Hp:    ", self.hp)
        print("Attack:", self.attack)
        print("Defense", self.defense)
        print("Speed  ", self.speed)

class Opp(Character):
    def __init__(self):
        super().__init__()
        self.special = random.choice(["Titan Form", "Gear 5th", "Rinnegan"])
        if self.special == "Titan Form":
            self.defense += 30
        elif self.special == "Gear 5th":
            self.attack += 15
            self.speed += 15
            self.hp -= 10
        elif self.special == "Rinnegan":
            self.hp += 10
            self.defense += 10

    def showcard(self):
        super().showcard()          #whatever after super is the method u want to add on.
        print("Special Move:", self.special)


char1 = Character()
char1.showcard()
char2 = Opp()
char2.showcard()


roundnum = 1

while True:
    choiceselection = input("Do You Want To Battle?: Y , N")
    if choiceselection == "Y":

        while char1.hp > 0 and char2.hp > 0:
            char2.hp = char2.hp - char1.attack + (char2.defense - char1.speed - char2.defense/20)
            char1.hp -= char2.attack + (char1.defense - char2. speed - char1.defense/20)
            print("")
            print("Round",roundnum),
            if char1.speed > char2.speed:
                print(f"{char1.name} will go first".center(42))
                print("Battling".center(42))
                time.sleep(0.4)
                print(f"{char1.name} delt {char1.attack} to {char2.name}".center(42))
                if char2.hp <= 0:
                    print(f"🎉🎉🎉{char1.name} WON🎉🎉🎉")
                    break
        
                print(f"{char2.name} new Hp:{char2.hp}".center(42))
        
                print(" ")
                print(f"{char2.name} will go now".center(42))
                print("Battling".center(42))
                time.sleep(0.4)
                print(f"{char2.name} delt {char2.attack} to {char1.name}".center(42))
                if char1.hp <= 0:
                    print(f"🎉🎉🎉{char2.name} WON🎉🎉🎉")
                    break
                
                print(f"{char1.name} new Hp:{char1.hp}".center(42))
            roundnum += 1

            if char2.speed > char1.speed:
                print(f"{char2.name} will go first".center(42))
                print("Battling".center(42))
                time.sleep(0.4)
                print(f"{char2.name} delt {char2.attack} to {char1.name}".center(42))
                if char1.hp <= 0:
                    print(f"🎉🎉🎉{char2.name} WON🎉🎉🎉")
                    break

                print(f"{char1.name} new Hp:{char1.hp}".center(42))
        
                print(" ")
                print(f"{char1.name} will go now".center(42))
                print("Battling".center(42))
                time.sleep(0.4)
                print(f"{char1.name} delt {char1.attack} to {char2.name}".center(42))
                if char2.hp <= 0:
                    print(f"🎉🎉🎉{char2.name} WON🎉🎉🎉")
                    break
            


        
        break
    elif choiceselection == "N":
        print("No battle will happen")
        break
    else:
        print("Enter Y or N")
        
for i in range(16):
    print(f"ending in {i} seconds")
    time.sleep(1)