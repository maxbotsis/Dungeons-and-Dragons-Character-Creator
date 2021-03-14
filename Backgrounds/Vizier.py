
if Background == "Vizier":
    SkillProficiencies.extend(["History", "Religion"])
    VizierArtisanTool = random.choice(ArtisanTools)
    VizierMusicalInstrument = random.choice(MusicalInstruments)
    ToolProficiencies.extend([VizierArtisanTool, VizierMusicalInstrument])
    Equipment.extend([random.choice([VizierArtisanTool, VizierMusicalInstrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    