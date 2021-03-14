
if Background == "Cormanthor Refugee":
    SkillProficiencies.extend(["Nature", "Survival"])
    CormanthorRefugeeArtisanTools = random.choice(ArtisanTools) # Introducing a temporary variable so the same artisan's tools will be included in the equipment and proficiencies
    ToolProficiencies.extend([CormanthorRefugeeArtisanTools])
    Equipment.extend(["Two-Person Tent", CormanthorRefugeeArtisanTools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    