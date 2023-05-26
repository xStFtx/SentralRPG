import random

class SkillBook:
    def __init__(self, name, skill_type, skill_bonus):
        self.name = name
        self.skill_type = skill_type
        self.skill_bonus = skill_bonus

    def use(self, character):
        print(f"Using skill book: {self.name}")
        if self.skill_type == "Health":
            character.health += self.skill_bonus
            print(f"Health increased by {self.skill_bonus}. New health: {character.health}")
        elif self.skill_type == "Attack":
            character.attack += self.skill_bonus
            print(f"Attack increased by {self.skill_bonus}. New attack: {character.attack}")
        elif self.skill_type == "Defense":
            character.defense += self.skill_bonus
            print(f"Defense increased by {self.skill_bonus}. New defense: {character.defense}")

class Equipment:
    def __init__(self, name, stat_type, stat_bonus):
        self.name = name
        self.stat_type = stat_type
        self.stat_bonus = stat_bonus

    def equip(self, character):
        print(f"Equipping {self.name}: {self.stat_type} +{self.stat_bonus}")
        if self.stat_type == "Defense":
            character.defense += self.stat_bonus
            print(f"Defense increased by {self.stat_bonus}. New defense: {character.defense}")
        elif self.stat_type == "Damage":
            character.attack += self.stat_bonus
            print(f"Attack increased by {self.stat_bonus}. New attack: {character.attack}")

class Potion:
    def __init__(self, name, potion_type, stat_bonus):
        self.name = name
        self.potion_type = potion_type
        self.stat_bonus = stat_bonus

    def use(self, character):
        print(f"Using potion: {self.name}")
        if self.potion_type == "Health":
            character.health += self.stat_bonus
            print(f"Health increased by {self.stat_bonus}. New health: {character.health}")
        elif self.potion_type == "Mana":
            character.mana += self.stat_bonus
            print(f"Mana increased by {self.stat_bonus}. New mana: {character.mana}")

class Shield(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, "Defense", defense)

class Armor(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, "Defense", defense)

class Weapon(Equipment):
    def __init__(self, name, damage):
        super().__init__(name, "Damage", damage)

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Axe(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Dagger(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

class Staff(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
