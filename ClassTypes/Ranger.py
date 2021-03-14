
    
if Class == "Ranger":
    if Level >= 2:
        FightingStyle = ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]
        FightingStyle = random.choice(FightingStyle)
    if Level >= 3:
        Subclass = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Primeval Guardian"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(10)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
    SavingThrowProficiencies.extend(["STR", "DEX"])
    SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3))
    EqptExtnd =[random.choice(["Scale Mail", "Leather Armour"])]
    EqptExtnd.extend(random.choice([["Two Shortswords"], random.sample(SimpleMelee, 2)]))
    EqptExtnd.extend([random.choice(["Dungeoneer's Pack", "Explorer's Pack"])])
    EqptExtnd.extend(["Longbow with 20 Arrows"])
    Equipment.extend(EqptExtnd)