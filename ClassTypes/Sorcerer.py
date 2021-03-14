
    
if Class == "Sorcerer":
    Subclass = ["Divine Soul", "Draconic Bloodline", "Giant Soul", "Pheonix Sorcery", "Pyromancer", "Sea Sorcery", "Shadow Magic", "Stone Soercery", "Storm Sorcery", "Wild Magic"]
    Subclass = random.choice(Subclass)
    HP = HP + HitPoints(6)
    WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    SavingThrowProficiencies.extend(["CON", "CHA"])
    SkillProficiencies.extend(random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2))
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "Two Daggers"])
    