from imports.Character import Character

class SkillBook:
    def __init__(self, name, skill, skill_type):
        self.name = name
        self.skill = skill
        self.skill_type = skill_type

    def use(self):
        print(f"Using skill book: {self.name}")
        if self.skill_type == "Health":
            Character.health += self.skill
        elif self.skill_type == "Attack":
            Character.attack += self.skill
        elif self.skill_type == "Defense":
            Character.defense += self.skill

class Equipment:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def equip(self):
        print(f"Equipping {self.name}: {self.stat}")
        if self.stat == "Defense":
            Character.defense += self.stat_bonus
            print(f"Defense increased by {self.stat_bonus}. New defense: {Character.defense}")
        elif self.stat == "Damage":
            Character.attack += self.stat_bonus
            print(f"Attack increased by {self.stat_bonus}. New attack: {Character.attack}")

class Potion:
    def __init__(self, name, potion_type, stat_bonus):
        self.name = name
        self.type = potion_type
        self.stat_bonus = stat_bonus

    def use(self):
        print(f"Using potion: {self.name}")
        if self.type == "Health":
            Character.health += self.stat_bonus
            print(f"Health increased by {self.stat_bonus}. New health: {Character.health}")
        elif self.type == "Mana":
            Character.mana += self.stat_bonus
            print(f"Mana increased by {self.stat_bonus}. New mana: {Character.mana}")

class Shield(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, "Defense")
        self.stat_bonus = defense

class Armor(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, "Defense")
        self.stat_bonus = defense

class Weapon(Equipment):
    def __init__(self, name, damage):
        super().__init__(name, "Damage")
        self.stat_bonus = damage

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
