import random
class EldenRing:
    blood = 200
    def __init__(self, name):
        self.name = name

    def defense(self, ins):
        if ins == 1:
            print(f"{self.name} use the 盾牌")
            return 0.5
        elif ins == 2:
            print(f"{self.name} is using 翻滾")
            return random.choice([0,1])

class Titan(EldenRing):
    def attack(self,ins):
        if ins == 1:
            print(f"{self.name} is using Titan smash!")
            return 100
        elif ins == 2:
            print(f"{self.name} is using fire !!!")
            return random.randint(10,300)
        
class Tarnished(EldenRing):
    def attack(self,ins):
        if ins == 1:
            print(f"{self.name} is using knife attack!")
            return 80
        elif ins == 2:
            print(f"{self.name} is using magic power !!!")
            return random.randint(50, 150)
        
user = input("enter your name: ")
player = Tarnished(user)
enemy = Titan("FireTitan")
value = random.choice([1,2])

while True:
    attack_ins = int(input("please select 1 attck ins: (1)knife (2)magic \n"))
    tarnished_attack = player.attack(attack_ins)
    minus = int(enemy.defense(value) * tarnished_attack)
    enemy.blood -= minus
    if enemy.blood <= 0:
        print(f"{enemy.name}lose, {player.name} win !!")
        break
    else:
        print(f"{enemy.name} - {minus} damage , now left blood: {enemy.blood}")
        print("")
        
    
    defense_ins = int(input("please select 1 defense ins: (1)盾牌 (2)翻滾 \n"))
    titan_attack = enemy.attack(value)
    minus = int(player.defense(defense_ins) * titan_attack)
    player.blood -= minus
    if player.blood <= 0:
        print(f"{player.name}lose, {enemy.name} win !!")
        break
    else:
        print(f"{player.name} - {minus} damage , now left blood: {player.blood}")
        print("")
    



'''
T1 = Tarnished("mike",100)
B1 = Titan("joe",500)
print(T1.level)
T1.defense()
B1.defense()
B1.fire()
'''