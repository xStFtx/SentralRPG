class Quest:
    def __init__(self, name, description, objectives, rewards):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.rewards = rewards
        self.completed = False

    def check_completion(self):
        # Implement logic to check if all objectives are completed
        pass

    def complete(self):
        if self.check_completion():
            # Grant rewards to the player
            self.completed = True
            print(f"Quest '{self.name}' completed!")
        else:
            print(f"Quest '{self.name}' is not yet completed.")

    def display_quest_info(self):
        print(f"Quest: {self.name}")
        print(f"Description: {self.description}")
        print("Objectives:")
        for objective in self.objectives:
            print(f"- {objective}")
        print("Rewards:")
        for reward in self.rewards:
            print(f"- {reward}")


# Quests
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

# List of all quests
quests = [quest1, quest2, quest3]
