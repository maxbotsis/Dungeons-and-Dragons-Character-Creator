
if Class == "Fighter":
    FightingStyle = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
    FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass = ["Arcane Archer", "Battle Master", "Brute", "Cavalier", "Champion", "Eldritch Knight", "Purple Dragon Knight", "Samurai", "Scout", "Sharpshooter"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour, Medium Armour, Heavy Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "CON"])
    SkillProficiencies.extend(random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2))
# =============================================================================
#   This whole equipment section got messed up because one choice of equipment gives multiple items, which gives my code lists within lists. My print functions don't work with lists within lists. I'm looking for a way to simplify this. Similar issue encountered with Paladin and Ranger
# =============================================================================
    EqptExtnd = [random.choice(["Light Crossbow with 20 Bolts", "Two Handaxes"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"])]
    EqptExtnd.extend(random.choice([["Chain Mail"], ["Leather Armour", "Longbow with 20 Arrows"]]))
    EqptExtnd.extend(random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)]))
    Equipment.extend(EqptExtnd)