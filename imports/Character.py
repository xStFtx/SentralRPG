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

        if self.character_class == "Mage":
            self.mana = 100
            self.max_mana = 100
        else:
            self.mana = 0
            self.max_mana = 0

        if self.character_class in ["Warrior", "Rogue"]:
            self.stamina = 100
            self.max_stamina = 100
        else:
            self.stamina = 0
            self.max_stamina = 0

    def display_character_info(self):
        print("Name:", self.name)
        print("Class:", self.character_class)
        print("Health:", self.health)
        if self.character_class == "Mage":
            print("Mana:", self.mana)

        if self.character_class in ["Warrior", "Rogue"]:
            print("Stamina:", self.stamina)
        print("Strength:", self.strength)
        print("Intelligence:", self.intelligence)
        print("Sneak:", self.sneak)
        print("Level:", self.level)

  
        print()
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

        xp_needed = self.calculate_xp_needed(self.level)
        if self.experience >= xp_needed:
            self.level_up()

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def use_health_potion(self):
        health_potions = [item for item in self.inventory if isinstance(item, Potion) and item.type == "Health"]
        if health_potions:
            potion = health_potions[0]
            self.health += potion.healing_amount
            if self.health > self.max_health:
                self.health = self.max_health
            self.inventory.remove(potion)
            print(f"{self.name} used {potion.name} and restored {potion.healing_amount} health.")
        else:
            print(f"{self.name} does not have any health potions.")

    def use_mana_potion(self):
        if self.character_class != "Mage":
            print(f"{self.name} cannot use mana potions.")
            return

        mana_potions = [item for item in self.inventory if isinstance(item, Potion) and item.type == "Mana"]
        if mana_potions:
            potion = mana_potions[0]
            self.mana += potion.healing_amount
            if self.mana > self.max_mana:
                self.mana = self.max_mana
            self.inventory.remove(potion)
            print(f"{self.name} used {potion.name} and restored {potion.healing_amount} mana.")
        else:
            print(f"{self.name} does not have any mana potions.")

    def use_stamina_potion(self):
        if self.character_class not in ["Warrior", "Rogue"]:
            print(f"{self.name} cannot use stamina potions.")
            return

        stamina_potions = [item for item in self.inventory if isinstance(item, Potion) and item.type == "Stamina"]
        if stamina_potions:
            potion = stamina_potions[0]
            self.stamina += potion.healing_amount
            if self.stamina > self.max_stamina:
                self.stamina = self.max_stamina
            self.inventory.remove(potion)
            print(f"{self.name} used {potion.name} and restored {potion.healing_amount} stamina.")
        else:
            print(f"{self.name} does not have any stamina potions.")

    def add_item_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Added {item.name} to inventory.")

    def attack(self, enemy):
        if self.character_class == "Mage":
            if self.mana < 5:
                print(f"{self.name} does not have enough mana to attack.")
                return
            self.mana -= 5
            print(f"{self.name} attacks {enemy.name} with intelligence {self.intelligence}!")
            damage = random.randint(1, self.intelligence)
        else:
            if self.stamina < 5:
                print(f"{self.name} does not have enough stamina to attack.")
                return
            self.stamina -= 5
            print(f"{self.name} attacks {enemy.name} with strength {self.strength}!")
            damage = random.randint(1, self.strength)

        enemy.take_damage(damage)

    def attack_with_intelligence(self, enemy):
        if self.character_class == "Mage":
            if self.mana < 10:
                print(f"{self.name} does not have enough mana to attack with intelligence.")
                return
            self.mana -= 10
            print(f"{self.name} attacks {enemy.name} with intelligence {self.intelligence}!")
            damage = random.randint(self.intelligence, self.intelligence * 2)

            enemy.take_damage(damage)
        else:
            print(f"{self.name} cannot attack with intelligence.")

    def sneak_attack(self, enemy):
        if self.character_class not in ["Rogue"]:
            print(f"{self.name} cannot perform sneak attacks.")
            return

        if self.sneak < 5:
            print(f"{self.name}'s Sneak is too low to perform a sneak attack.")
            return

        if self.stamina < 10:
            print(f"{self.name} does not have enough stamina to perform a sneak attack.")
            return

        self.stamina -= 10

        print(f"{self.name} performs a sneak attack on {enemy.name}!")
        damage = random.randint(1, self.sneak * 2)

        enemy.take_damage(damage)

    def run_away(self, enemy):
        if self.stamina < 10:
            print(f"{self.name} does not have enough stamina to run away.")
            return

        self.stamina -= 10

        print(f"{self.name} runs away from {enemy.name}.")

    def regenerate(self):
        if self.character_class == "Mage":
            self.mana = self.max_mana
        elif self.character_class in ["Warrior", "Rogue"]:
            self.stamina = self.max_stamina

        print(f"{self.name} has regenerated mana and stamina.")

    def rest(self):
        self.health = self.max_health
        self.regenerate()
        print(f"{self.name} has rested and fully recovered.")


    def is_alive(self):
        return self.health > 0
