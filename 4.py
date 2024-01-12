import random

class Warrior:
    def __init__(self, name, health=100, armor=100, endurance=100):
        self.name = name
        self.health = health
        self.armor = armor
        self.endurance = endurance

    def attack(self, enemy):
        if self.endurance >= 10:
            damage = random.randint(10, 30)
            enemy.defend(damage)
            self.endurance -= 10
            print(f"{self.name} атакует {enemy.name}. {self.name} теряет 10 очков выносливости.")
        else:
            damage = random.randint(0, 10)
            enemy.defend(damage)
            print(f"{self.name} не может атаковать из-за недостатка выносливости и теряет {damage} очков здоровья.")

    def defend(self, damage):
        if self.endurance > 0:
            self.endurance -= 10
            if random.choice([True, False]):  # Решаем защищаться или нет
                armor_damage = random.randint(0, 10)
                self.armor -= armor_damage
                print(f"{self.name} решает защищаться и теряет {armor_damage} очков брони.")
            else:
                health_damage = random.randint(0, 20)
                self.health -= health_damage
                print(f"{self.name} решает не защищаться и теряет {health_damage} очков здоровья.")
        else:
            damage = random.randint(10, 30)
            self.health -= damage
            print(f"{self.name} не может защищаться из-за недостатка выносливости и теряет {damage} очков здоровья.")

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.health > 10 and warrior2.health > 10:
    action1 = random.choice(['attack', 'defend'])
    action2 = random.choice(['attack', 'defend'])

    if action1 == 'attack':
        warrior1.attack(warrior2)
    else:
        warrior1.defend(0)

    if action2 == 'attack':
        warrior2.attack(warrior1)
    else:
        warrior2.defend(0)

if warrior1.health <= 10:
    print(f"{warrior2.name} победил!")
    user_input = input("Хотите убить проигравшего воина? (yes/no): ").lower()
    if user_input == "yes":
        print(f"{warrior1.name} был убит.")
    else:
        print(f"{warrior1.name} был прощен.")
else:
    print(f"{warrior1.name} победил!")
    user_input = input("Хотите убить проигравшего воина? (yes/no): ").lower()
    if user_input == "yes":
        print(f"{warrior2.name} был убит.")
    else:
        print(f"{warrior2.name} был прощен.")
