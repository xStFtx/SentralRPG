class Character:
    def __init__(self, name, character_class, health, strength, intelligence):
        self.name = name
        self.character_class = character_class
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.inventory = []
        self.equipped_shield = None
        self.equipped_armor = None
        self.equipped_weapon = None

    def display_character_info(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Intelligence: {self.intelligence}")

        inventory_counts = {}  # Dictionary to store item counts
        for item in self.inventory:
            if item.name in inventory_counts:
                inventory_counts[item.name] += 1  # Increment count for duplicate item
            else:
                inventory_counts[item.name] = 1  # Initialize count for new item

        inventory_display = []
        for item_name, count in inventory_counts.items():
            if count > 1:
                item_display = f"{item_name} ({count})"  # Display item with count in brackets
            else:
                item_display = item_name  # Display item without count
            inventory_display.append(item_display)

        print("Inventory: ", ", ".join(inventory_display))  # Join the inventory items for display



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
