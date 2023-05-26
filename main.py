from imports.Character import Character
from imports.Enemy import Enemy, Goblin, Skeleton, Orc, Dragon, SkeletonBoss, OrcBoss
from imports.Exploring import Exploring
from imports.Quests import QuestManager, Quest, QuestLoader

def main():
    while True:
        name = input("Enter your character's name: ")
        print("Choose your character's class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        class_choice = input("Enter your choice: ")

        character_class = ""
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Mage"
        elif class_choice == "3":
            character_class = "Rogue"

        player = Character(name, character_class, 100, 10, 5)
        exploration = Exploring(player)

        quest_manager = QuestManager()
        QuestLoader(quest_manager)

        print("Welcome to Sentral RPG!")
        while True:
            print("\n1. Explore Location")
            print("2. Check Inventory")
            print("3. View Quests")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                exploration.explore_location()
                if not player.is_alive():
                    print("You were defeated by an enemy.")
                    break
            elif choice == "2":
                player.display_character_info()
            elif choice == "3":
                quest_manager.display_all_quests()
            elif choice == "4":
                print("Thank you for playing!")
                return
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
