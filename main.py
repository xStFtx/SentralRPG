from imports.Character_creation import Character
from imports.Enemy import Enemy
from imports.Exploring import Exploring
from imports.Quests import quests

import random

def main():
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

    print("Welcome to the Text-Based RPG!")
    while True:
        print("1. Explore Location")
        print("2. Check Inventory")
        print("3. View Quests")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            exploration.explore_location()
        elif choice == "2":
            player.display_character_info()
        elif choice == "3":
            display_active_quests()
        elif choice == "4":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_active_quests():
    print("Active Quests:")
    print()  # Add an empty line for spacing
    
    for quest in quests:
        if not quest.completed:
            quest.display_quest_info()
            print()  # Add an empty line between quests


if __name__ == "__main__":
    main()
