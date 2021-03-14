if Race == "Dwarf":
    Subrace = ["Duergar", "Hill", "Mountain"]
    Subrace = random.choice(Subrace)
    CON = StatIncrease(CON, 2)
    if Subrace == "Hill":
        WIS = StatIncrease(WIS, 1)
    if Subrace == "Mountain":
        STR = StatIncrease(STR, 2)
    if Subrace == "Duergar":
        STR = StatIncrease(STR, 1)
    Age = Normal(20,320)
    SizeMod = Normal(2,8)
    if Subrace == "Hill":
        Height = 3 * 12 + 8 + SizeMod
        Weight = 115 + SizeMod * Normal(2,12)
    if Subrace == "Mountain":
        Height = 4 * 12 + SizeMod
        Weight = 130 + SizeMod * Normal(2,12)
    if Subrace == "Duergar":
        Height = 3 * 12 + 8 + SizeMod
        Weight = 115 + SizeMod * Normal(2,12)
    Eyes = ["Brown", "Hazel", "Green"]
    Eyes = random.choice(Eyes)
    Skin = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin = random.choice(Skin)
    Hair = ["Bald", "Brown", "Black", "Blond", "Red"]
    Hair = random.choice(Hair)
    Speed = 25
    WeaponProficiencies.extend(["Battleaxe", "Handaxe", "Throwing Hammer", "Warhammer"])
    Traits.extend(["Dwarven Resilience"])
    if Subrace == "Hill":
        HP = HP + Level
        Traits.extend(["Darkvision (60ft)"])
    if Subrace == "Mountain":
        ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
        Traits.extend(["Darkvision (60ft)"])
    if Subrace == "Duergar":
        Traits.extend(["Darkvision (120ft)", "Duergar Resilience", "Duergar Magic", "Sunlight Sensitivity"])
    