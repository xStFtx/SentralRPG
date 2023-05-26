class Quest:
    def __init__(self, name, description, objectives, rewards):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.rewards = rewards
        self.completed = False

    def display_quest_info(self):
        print("Quest:", self.name)
        print("Description:", self.description)
        print("Objectives:", ", ".join(self.objectives))
        print("Rewards:", ", ".join(self.rewards))
        if self.completed:
            print("Status: Completed")
        else:
            print("Status: In Progress")

    def complete_quest(self):
        if not self.completed:
            print(f"Congratulations! You have completed the quest: {self.name}")
            print("You receive the following rewards:", ", ".join(self.rewards))
            self.completed = True
        else:
            print("This quest has already been completed.")


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest):
        if quest in self.quests:
            self.quests.remove(quest)

    def display_all_quests(self):
        if not self.quests:
            print("No quests available.")
        else:
            print("Quests:")
            for quest in self.quests:
                quest.display_quest_info()
                print()


quest1 = Quest(
    name="Save the Village",
    description="The village is under attack by monsters. Defeat all the monsters and save the village.",
    objectives=["Defeat 5 monsters", "Talk to the village elder"],
    rewards=["Gold", "Experience points"]
)

quest2 = Quest(
    name="Gather Rare Ingredients",
    description="Collect rare ingredients for a powerful potion.",
    objectives=["Find the hidden forest", "Defeat the guardian of the forest", "Collect rare plants"],
    rewards=["Rare potion recipe", "Boosted stats"]
)

quest3 = Quest(
    name="Uncover the Ancient Artifact",
    description="Embark on a journey to uncover an ancient artifact hidden in the ruins.",
    objectives=["Solve the puzzles in the ruins", "Defeat the guardian of the artifact"],
    rewards=["Legendary weapon", "Unlock new abilities"]
)

quests = [quest1, quest2, quest3]

def QuestLoader(quest_manager):
    for quest in quests:
        quest_manager.add_quest(quest)
