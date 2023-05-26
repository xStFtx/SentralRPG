import random
from .Items import Sword, Potion, Axe

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
        print("Damage:", self.damage)
        print("XP:", self.xp)

    def attack(self, target):
        damage = random.randint(1, self.damage)
        target.take_damage(damage)
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
        super().__init__("Goblin", 1, 20, 5, 10)
        self.strength = 2
        self.experience_points = 10

    def loot(self):
        loot_items = []
        loot_items.append(Sword("Sword", 5))
        loot_items.append(Potion("Health Potion", "Health", 10))
        return random.choice(loot_items)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("Skeleton", 2, 30, 8, 15)
        self.strength = 5
        self.experience_points = 15

    def loot(self):
        loot_items = []
        loot_items.append(Sword("Sword", 8))
        loot_items.append(Potion("Health Potion", "Health", 15))
        return random.choice(loot_items)


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 3, 50, 12, 20)
        self.strength = 10
        self.experience_points = 20

    def loot(self):
        loot_items = []
        loot_items.append(Axe("Axe", 15))
        loot_items.append(Potion("Health Potion", "Health", 20))
        return random.choice(loot_items)


class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 5, 100, 20, 30)
        self.strength = 18
        self.experience_points = 30

    def loot(self):
        loot_items = []
        loot_items.append(Sword("Fire Sword", 25))
        loot_items.append(Potion("Health Potion", "Health", 30))
        return random.choice(loot_items)


class SkeletonBoss(Enemy):
    def __init__(self):
        super().__init__("Skeleton Boss", 8, 200, 30, 50)
        self.strength = 25
        self.experience_points = 40

    def loot(self):
        loot_items = []
        loot_items.append(Sword("Ancient Sword", 40))
        loot_items.append(Potion("Health Potion", "Health", 50))
        return random.choice(loot_items)


class OrcBoss(Enemy):
    def __init__(self):
        super().__init__("Orc Boss", 10, 500, 50, 75)
        self.strength = 30
        self.experience_points = 55

    def loot(self):
        loot_items = []
        loot_items.append(Axe("War Axe", 60))
        loot_items.append(Potion("Health Potion", "Health", 75))
        return random.choice(loot_items)
