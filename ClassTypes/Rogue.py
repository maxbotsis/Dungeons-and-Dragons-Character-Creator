
if Class == "Rogue":
    if Level >= 3:
        Subclass = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    ToolProficiencies.extend(["Thieves' Tools"])
    SavingThrowProficiencies.extend(["DEX", "INT"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4))
    Equipment.extend([random.choice(["Rapier", "Shortsword"]), random.choice(["Shortbow with 20 Arrows", "Shortsword"]), random.choice(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]), "Leather Armour", "Two Daggers", "Thieves's Tools"])
    