
if Class == "Warlock":
    Subclass = ["The Archfey", "The Celestial", "The Fiend", "The Ghost in the Machine", "The Great Old One", "The Hexblade", "The Raven Queen", "The Seeker", "The Undying"]
    Subclass = random.choice(Subclass)
    if Level >= 3:
        FightingStyle = ["Pact of the Chain", "Pact of the Blade", "Pact of the Tome"]
        FightingStyle = random.choice(FightingStyle)
    HP = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2))
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Dungeoneer's Pack"]), "Leather Armour", random.choice(SimpleWeapons), "Two Daggers"])
    