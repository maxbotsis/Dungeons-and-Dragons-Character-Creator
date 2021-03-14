
    
if Class == "Druid":
    if Level >= 2:
        Subclass = ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of Spores", "Circle of Twilight"]
        Subclass = random.choice(Subclass)
        if Subclass == "Circle of the Land":
            Land = random.choice(["(Arctic)", "(Coast)", "(Desert)", "(Forest)", "(Grassland)", "(Mountain)", "(Swamp)", "(Underdark)"])
            Subclass = "Circle of the Land " + Land
    HP = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"])
    ToolProficiencies.extend(["Herbalism Kit"])
    SavingThrowProficiencies.extend(["INT", "WIS"])
    SkillProficiencies.extend(random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2))
    Equipment.extend([random.choice(["Wooden Shield", random.choice(SimpleWeapons)]), random.choice(["Scimitar", random.choice(SimpleMelee)]), "Leather Armour", "Explorer's Pack", "Druidic Focus"])
   