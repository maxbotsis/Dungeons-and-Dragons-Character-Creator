
if Background == "Soldier":
    Specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
    Background = "Soldier " + Specialty
    SkillProficiencies.extend(["Athletics", "Intimidation"])
    ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
    Equipment.extend(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    