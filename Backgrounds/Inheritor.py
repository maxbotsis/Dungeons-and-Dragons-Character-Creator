
if Background == "Inheritor":
    SkillProficiencies.extend(["Survival", random.choice(["Arcana", "History", "Religion"])])
    InheritorTool = random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])
    ToolProficiencies.extend([InheritorTool])
    Equipment.extend(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", InheritorTool, "15 gp"])
    