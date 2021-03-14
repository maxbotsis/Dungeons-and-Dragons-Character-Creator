
if Background == "Faction Agent":
    Faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
    Background = "Faction Agent of " + Faction
    SkillProficiencies.extend(["Insight"])
    if Faction == "The Emerald Enclave":
        SkillProficiencies.extend(["Nature"])
    if Faction == "The Harpers":
        SkillProficiencies.extend(["Investigation"])
    if Faction == "The Lord's Alliance":
        SkillProficiencies.extend(["History"])
    if Faction == "The Order of the Gauntlet":
        SkillProficiencies.extend(["Religion"])
    if Faction == "The Zhentarim":
        SkillProficiencies.extend(["Deception"])
    Equipment.extend([random.choice(["Badge of " + Faction, "Emblem of " + Faction]), "Set of Common Clothes", "15 gp"])
    if Faction == "The Harpers" or Faction == "The Zhentarim":
        Equipment.extend(["Copy of a Code-Book from " + Faction])
    else: 
        Equipment.extend(["Copy of a Seminal Text from " + Faction])
    