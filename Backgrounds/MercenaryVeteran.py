
if Background == "Mercenary Veteran":
    Company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
    Background = "Mercenary Veteran from " + Company
    SkillProficiencies.extend(["Athletics", "Persuasion"])
    MercenaryVeteranGamingSet = random.choice(GamingSets)
    ToolProficiencies.extend([MercenaryVeteranGamingSet, "Land Vehicles"])
    Equipment.extend(["Uniform from " + Company, "Insignia of Your Rank from " + Company, MercenaryVeteranGamingSet, "10 gp"])
    