
if Background == "Criminal":
    Specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
    Background = "Criminal " + random.choice(Specialty)
    SkillProficiencies.extend(["Deception", "Stealth"])
    ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])
