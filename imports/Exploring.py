import random
from .Enemy import Enemy
from .Items import Potion

class Exploring:
    def __init__(self, player):
        self.player = player

    def explore_location(self):
        print("You are exploring the location...")
        event = random.randint(1, 3)

        if event == 1:
            self.encounter_enemy()
        elif event == 2:
            self.find_treasure_chest()
        else:
            print("You didn't find anything interesting.")

    def encounter_enemy(self):
        enemy = Enemy("Goblin", 50, 8)
        print("You encountered an enemy:", enemy.name)
        while self.player.is_alive() and enemy.is_alive():
            self.player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(self.player)

        if self.player.is_alive():
            print(f"You defeated {enemy.name}!")
            self.player.add_item_to_inventory(Potion("Health Potion", "Health"))
        else:
            print("You were defeated by the enemy.")

    def find_treasure_chest(self):
        print("You found a treasure chest!")
        item = random.choice([Potion("Health Potion", "Health"), Potion("Mana Potion", "Mana")])
        self.player.add_item_to_inventory(item)
