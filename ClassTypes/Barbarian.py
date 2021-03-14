
if Class == "Barbarian":
    if Level >= 3:
        Subclass = ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Berserker", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of the Zealot"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(12)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "CON"])
    SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2))
    Equipment.extend([random.choice(["Greataxe", random.choice(MartialMelee)]), random.choice(["Two Handaxes", random.choice(SimpleWeapons)]), "Explorer's Pack", "Four Javelins"])
    