import random
from .Enemy import Goblin, Skeleton, Orc, Dragon, SkeletonBoss, OrcBoss
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
        enemy = random.choice([Goblin(), Skeleton(), Orc(), Dragon(), SkeletonBoss(), OrcBoss()])
        print("You encountered an enemy:", enemy.name)
        while self.player.is_alive() and enemy.is_alive():
            self.player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(self.player)

        if self.player.is_alive():
            print(f"You defeated {enemy.name}!")
            potion = Potion("Health Potion", "Health", 20)  # Create a Health Potion item
            self.player.add_item_to_inventory(potion)
            self.player.gain_experience(enemy.xp)  # Gain XP from defeated enemy
        else:
            print("You were defeated by the enemy.")
            self.player.reset()  # Reset the player if defeated

    def find_treasure_chest(self):
        print("You found a treasure chest!")
        potion = random.choice([Potion("Health Potion", "Health", 20), Potion("Mana Potion", "Mana", 20)])
        self.player.add_item_to_inventory(potion)
