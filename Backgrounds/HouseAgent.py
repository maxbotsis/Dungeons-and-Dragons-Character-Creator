
if Background == "House Agent":
    House = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
    Background = "House Agent of the " + House + " House"
    SkillProficiencies.extend(["Investigation", "Persuasion"])
    if House == "Cannith":
        ToolProficiencies.extend(["Alchemist's Supplies", "Tinker's Tools"])
    if House == "Deneith":
        ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
    if House == "Ghallanda":
        ToolProficiencies.extend(["Brewer's Supplies", "Cook's Utensils"])
    if House == "Jorasco":
        ToolProficiencies.extend(["Alchemist's Supplies", "Herbalism Kit"])
    if House == "Kundarak":
        ToolProficiencies.extend(["Tinker's Tools", "Thieves' Tools"])
    if House == "Lyrandar":
        ToolProficiencies.extend(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
    if House == "Medani":
        ToolProficiencies.extend(["Thieves' Tools", "Disguise Kit"])
    if House == "Orien":
        ToolProficiencies.extend(["Land Vehicles", random.choice(GamingSets)])
    if House == "Phiarlan":
        ToolProficiencies.extend(["Disguise Kit", random.choice(MusicalInstruments)])
    if House == "Sivis":
        ToolProficiencies.extend(["Calligrapher's Tools", "Forgery Kit"])
    if House == "Tharashk":
        ToolProficiencies.extend(["Thieve's Tools", random.choice(GamingSets)])
    if House == "Thuranni":
        ToolProficiencies.extend(["Poisoner's Kit", random.choice(GamingSets)])
    if House == "Vadalis":
        ToolProficiencies.extend(["Land Vehicles", "Herbalism Kit"])
    Equipment.extend(["Set of Fine Clothes", House + " Signet Ring", "ID Papers", "20 gp"])
    