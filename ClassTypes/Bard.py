
if Class == "Bard":
    if Level >= 3:
        Subclass = ["College of Glamour", "College of Lore", "College of Satire", "College of Swords", "College of Valor", "College of Whispers"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour"])
    WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
    ToolProficiencies.extend(random.sample(MusicalInstruments, 3))
    SavingThrowProficiencies.extend(["DEX", "CHA"])
    SkillProficiencies.extend(random.sample(Skills, 3))
    Equipment.extend([random.choice(["Rapier", "Longsword", random.choice(SimpleWeapons)]), random.choice(["Diplomat's Pack", "Entertainer's Pack"]), random.choice(["Lute", random.choice(MusicalInstruments)]), "Leather Armour", "Dagger"])
    