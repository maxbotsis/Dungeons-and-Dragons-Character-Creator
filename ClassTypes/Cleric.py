
    
if Class == "Cleric":
    Subclass = ["Arcana Domain", "Ambition Domain", "City Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Protection Domain", "Solidarity Domain", "Strength Domain", "Tempest Domain", "Trickery Domain", "War Domain", "Zeal Domain"]
    Subclass = random.choice(Subclass)
    HP = HP + HitPoints(8)
    ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
    WeaponProficiencies.extend(["Simple Weapons"])
    SavingThrowProficiencies.extend(["WIS", "CHA"])
    SkillProficiencies.extend(random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2))
    if "Warhammer" in WeaponProficiencies or "Martial Weapons" in WeaponProficiencies:
        Equipment.extend([random.choice(["Mace", "Warhammer"])])
    else:
        Equipment.extend(["Mace"])
    if "Chain Mail" in ArmourProficiencies or "Heavy Armour" in ArmourProficiencies:
        Equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
    else:
        Equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
    Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Priest's Pack", "Explorer's Pack"]), "Shield", "Holy Symbol"])
    