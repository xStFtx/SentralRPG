import random

class Enemy:
    def __init__(self, name, level, health, damage, xp):
        self.name = name
        self.level = level
        self.health = health
        self.damage = damage
        self.xp = xp


    def display_enemy_info(self):
        print("Name:", self.name)
        print("Level:", self.level)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("XP:", self.xp)

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


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 1, 50, 10, 10)
        self.strength = 10


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 2, 75, 15, 15)
        self.strength = 15


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 3, 100, 20, 20)
        self.strength = 20


class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 5, 200, 30, 30)
        self.strength = 25


class SkeletonBoss(Enemy):
    def __init__(self):
        super().__init__("Skeleton Boss", 8, 500, 40, 50)
        self.strength = 35


class OrcBoss(Enemy):
    def __init__(self):
        super().__init__("Orc Boss", 10, 1000, 50, 75)
        self.strength = 55
