from imports.Character_creation import Character

class SkillBook:
    def __init__(self, name, skill, skill_type):
        self.name = name
        self.skill = skill
        self.skill_type = skill_type

    def use(self):
        print(f"Using skill book: {self.name}")
        if self.skill_type == "Health":
            Character.health += 5
        elif self.skill_type == "Attack":
            Character.attack += 5
        elif self.skill_type == "Defense":
            Character.defense += 5

class Equipment:
    def __init__(self, name, stat):
        self.name = name
        self.stat = stat

    def equip(self):
        print(f"Equipping {self.name}: {self.stat}")
        # Implement logic for equipping the equipment

class Potion:
    def __init__(self, name, potion_type):
        self.name = name
        self.type = potion_type

    def use(self):
        print(f"Using potion: {self.name}")
        # Implement logic for using the potion

class Shield(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, defense)

class Armor(Equipment):
    def __init__(self, name, defense):
        super().__init__(name, defense)

class Weapon(Equipment):
    def __init__(self, name, damage):
        super().__init__(name, damage)

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
