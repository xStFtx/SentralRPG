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
            if self.player.level < 3:
                self.encounter_enemy(Goblin())
            elif self.player.level < 5:
                self.encounter_enemy(Skeleton())
            elif self.player.level < 10:
                self.encounter_enemy(Orc())
            elif self.player.level < 20:
                self.encounter_enemy(Dragon())
            else:
                self.encounter_enemy(random.choice([SkeletonBoss(), OrcBoss()]))
        elif event == 2:
            self.find_treasure_chest()
        else:
            print("You didn't find anything interesting.")

    def encounter_enemy(self, enemy):
        print(f"You encountered a {enemy.name}!")

        while enemy.is_alive() and self.player.is_alive():
            print("\nChoose your action:")
            print("1. Attack (S)")
            print("2. Attack with Intelligence (I)")
            print("3. Sneak Attack (A)")
            print("4. Run Away (R)")

            choice = input("Enter your choice: ")

            if choice.lower() == "s" or choice == "1":
                self.player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif choice.lower() == "i" or choice == "2":
                if self.player.intelligence < 5:
                    print("Your Intelligence is too low to perform this action.")
                    continue
                self.player.attack_with_intelligence(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif choice.lower() == "a" or choice == "3":
                if self.player.sneak < 5:
                    print("Your Sneak is too low to perform this action.")
                    continue
                self.player.sneak_attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            elif choice.lower() == "r" or choice == "4":
                print("You ran away from the enemy.")
                break
            else:
                print("Invalid choice. Please try again.")

            if not enemy.is_alive():
                self.player.gain_experience(enemy.experience_points)
                self.player.add_item_to_inventory(enemy.loot())
                break

        if not self.player.is_alive():
            self.player.rest()

    def find_treasure_chest(self):
        print("You found a treasure chest!")
        item = self.generate_random_potion()
        self.player.add_item_to_inventory(item)

    def generate_random_potion(self):
        potion_types = ["Health", "Mana", "Stamina"]
        potion_type = random.choice(potion_types)
        potion_name = f"{potion_type} Potion"
        potion_stat_bonus = random.randint(5, 15)  # Adjust the stat bonus range as desired
        return Potion(potion_name, potion_type, potion_stat_bonus)
