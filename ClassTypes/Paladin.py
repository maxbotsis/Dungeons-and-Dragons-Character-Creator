
    
if Class == "Paladin":
    if Level >= 2:
        FightingStyle = ["Defense", "Dueling", "Great Weapon Fighting", "Protection"]
        FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass = ["Oath of the Ancients", "Oath of Conquests", "Oath of the Crown", "Oath of Devotion", "Oath of Redemption", "Oath of Vengeance", "Oathbreaker", "Oath of Treachery"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Heavy Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2))
    EqptExtnd = random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)])
    EqptExtnd.extend([random.choice(["5 Javelins", random.choice(SimpleMelee)])])
    EqptExtnd.extend(["Chain Mail", "Holy Symbol"])
    Equipment.extend(EqptExtnd)
    