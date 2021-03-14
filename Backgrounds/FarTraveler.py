
if Background == "Far Traveler":
    Reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
    Origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
    Background = "Far Traveler " + Reason + " from " + Origin
    SkillProficiencies.extend(["Insight", "Perception"])
    FarTravelerTool = random.choice([random.choice(MusicalInstruments), random.choice(GamingSets)])
    ToolProficiencies.extend([FarTravelerTool])
    Equipment.extend([FarTravelerTool, "Poorly Wrought Maps from " + Origin, "Small Piece of Jewelry Worth 10 gp from " + Origin, "5 gp"])
    