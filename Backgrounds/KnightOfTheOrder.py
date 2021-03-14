
if Background == "Knight of the Order":
    Order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
    Background = "Knight of the Order of " + Order
    SkillProficiencies.extend(["Persuasion"])
    if Order == "the Unicorn":
        SkillProficiencies.extend([random.choice(["Arcana", "Religion"])])
    if Order == "Myth Drannor":
        SkillProficiencies.extend([random.choice(["Nature", "History"])])
    if Order == "the Silver Chalice":
        SkillProficiencies.extend([random.choice(["History", "Religion"])])
    ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
    Equipment.extend(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + Order, "10 gp"])
    