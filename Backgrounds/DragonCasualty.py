
if Background == "Dragon Casualty": # Tool proficiency is based on origin
    Origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
    Background = "Dragon Casualty who used to be a " + Origin
    if Origin == "Dockworker/Fisherman":
        ToolProficiencies.extend(["Water Vehicles"])
    if Origin == "Tradesperson/Merchant":
        ToolProficiencies.extend([random.choice(ArtisanTools)])
    if Origin == "Black Fist Soldier":
        ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), "Land Vehicles"])])
    if Origin == "Adventurer":
        ToolProficiencies.extend(["Land Vehicles"])
    if Origin == "Entertainer":
        ToolProficiencies.extend([random.choice(MusicalInstruments)])
    if Origin == "Scholar/Healer":
        ToolProficiencies.extend([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
    if Origin == "Criminal":
        ToolProficiencies.extend([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
    if Origin == "Unskilled Labourer":
        ToolProficiencies.extend([random.choice(GamingSets)])
    SkillProficiencies.extend(["Intimidation", "Survival"])
    Equipment.extend(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])
