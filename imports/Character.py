from .Quests import QuestManager

class Character:
    def __init__(self, name, character_class, health, strength, intelligence):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.max_health = health

    def display_character_info(self):
        print("Name:", self.name)
        print("Class:", self.character_class)
        print("Health:", self.health)
        print("Strength:", self.strength)
        print("Intelligence:", self.intelligence)
        print("Level:", self.level)

        xp_needed = self.calculate_xp_needed(self.level + 1)
        print("Experience:", f"{self.experience}/{xp_needed}")

        inventory_counts = {}
        for item in self.inventory:
            if item.name in inventory_counts:
                inventory_counts[item.name] += 1
            else:
                inventory_counts[item.name] = 1

        inventory_display = []
        for item_name, count in inventory_counts.items():
            if count > 1:
                item_display = f"{item_name} ({count})"
            else:
                item_display = item_name
            inventory_display.append(item_display)

        print("Inventory: ", ", ".join(inventory_display))

    def calculate_xp_needed(self, level):
        # Exponential leveling system: xp_needed = base_value * level^exponent
        base_value = 100  # Base value for calculating xp_needed
        exponent = 1.5  # Exponent determines the rate of increase in xp_needed
        return int(base_value * (level ** exponent))

    def level_up(self):
        self.level += 1
        print(f"Congratulations! {self.name} leveled up to level {self.level}.")

    def gain_experience(self, experience_points):
        self.experience += experience_points
        print(f"{self.name} gained {experience_points} experience points.")

        xp_needed = self.calculate_xp_needed(self.level + 1)
        if self.experience >= xp_needed:
            self.level_up()

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Added {item.name} to inventory.")

    def remove_item_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"Removed {item} from inventory.")
        else:
            print(f"{item} is not in the inventory.")

    def equip_shield(self, shield):
        print(f"Equipping shield: {shield.name}")
        self.equipped_shield = shield

    def equip_armor(self, armor):
        print(f"Equipping armor: {armor.name}")
        self.equipped_armor = armor

    def equip_weapon(self, weapon):
        print(f"Equipping weapon: {weapon.name}")
        self.equipped_weapon = weapon

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}!")
        enemy.take_damage(self.strength)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0
    
    def gain_experience(self, experience_points):
        self.experience += experience_points
        print(f"{self.name} gained {experience_points} experience points.")

        xp_needed = self.calculate_xp_needed(self.level + 1)
        if self.experience >= xp_needed:
            self.level_up()


    def reset(self):
        self.health = self.max_health
        self.experience = 0
        print("You have been defeated. Your character has been reset.")