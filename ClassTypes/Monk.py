
    
if Class == "Monk":
    if Level >= 3:
        Subclass = ["Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul", "Way of Tranquility"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(8)
    WeaponProficiencies.extend(["Simple Weapons", "Shortswords"])
    ToolProficiencies.extend([random.choice([random.choice(MusicalInstruments), random.choice(ArtisanTools)])])
    SavingThrowProficiencies.extend(["STR", "DEX"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2))
    Equipment.extend([random.choice(["Shortsword", random.choice(SimpleWeapons)]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "10 Darts"])
    