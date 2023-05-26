import random
from .Items import Potion


class Character:
    def __init__(self, name, character_class, health, strength, intelligence, sneak):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.sneak = sneak
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
        print("Sneak:", self.sneak)
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
        base_value = 25  # Base value for calculating xp_needed
        exponent = 1.5  # Exponent determines the rate of increase in xp_needed
        return int(base_value * (level ** exponent))

    def level_up(self):
        self.level += 1
        print(f"Congratulations! {self.name} leveled up to level {self.level}.")
        self.health = self.max_health  # Restore health upon leveling up

        # Choose a stat to increase
        print(f"Choose a stat to increase:")
        print("1. Strength")
        print("2. Intelligence")
        print("3. Sneak")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.strength += 1
            print(f"{self.name}'s Strength increased by 1.")
        elif choice == "2":
            self.intelligence += 1
            print(f"{self.name}'s Intelligence increased by 1.")
        elif choice == "3":
            self.sneak += 1
            print(f"{self.name}'s Sneak increased by 1.")
        else:
            print("Invalid choice. No stat increase.")

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
        damage = self.strength
        print(f"{self.name} attacks {enemy.name} with strength {damage}!")
        enemy.take_damage(damage)

    def attack_with_intelligence(self, enemy):
        if self.intelligence < 5:
            print("Your Intelligence is too low to perform this action.")
            return

        damage = self.intelligence
        print(f"{self.name} attacks {enemy.name} with intelligence {damage}!")
        enemy.take_damage(damage)

    def sneak_attack(self, enemy):
        if self.sneak < 5:
            print("Your Sneak is too low to perform this action.")
            return

        damage = self.sneak
        print(f"{self.name} performs a sneak attack on {enemy.name} with damage {damage}!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
            self.reset()
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")
            if self.health < self.max_health * 0.25:
                self.use_health_potion()

    def is_alive(self):
        return self.health > 0

    def use_health_potion(self):
        health_potions = [item for item in self.inventory if isinstance(item, Potion) and item.type == "Health"]
        if health_potions:
            potion = random.choice(health_potions)
            self.health += potion.healing_points
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} used a {potion.name} and restored {potion.healing_points} health.")

    def reset(self):
        self.health = self.max_health
        self.experience = 0
        print("You have been defeated. Your character has been reset.")
