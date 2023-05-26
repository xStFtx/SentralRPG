import random

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, target):
        damage = random.randint(1, self.strength)
        target.health -= damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage.")

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
            self.health -= damage
            if self.health < 0:
                self.health = 0
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
