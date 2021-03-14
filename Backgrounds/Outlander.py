
if Background == "Outlander":
    Origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
    Background = "Outlander " + Origin
    SkillProficiencies.extend(["Athletics", "Survival"])
    ToolProficiencies.extend([random.choice(MusicalInstruments)])
    Equipment.extend(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
   