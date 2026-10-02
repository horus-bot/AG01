class Character:
    def __init__(self,name,health):
        self.name = name 
        self.health = health

    def attack(self):
        print(self.name,"attacks hehe ")

    def take_damege(self,damage):
        self.health -= damage
        print("ahh health is down by ",damage)

    def get_health(self):
        print(self.health)

class Warrior(Character):
    def __init__(self,name,health,weapon):
        super().__init__(name,health)
        self.weapon = weapon

    def attack(self):
        print("harsh attacks")

swathi = Character("swathi",1000)
harsh = Warrior("harsh",100,"slash attack")

swathi.attack()
harsh.attack()