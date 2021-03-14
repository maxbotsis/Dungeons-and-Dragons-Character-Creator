if Race == "Elf":
    Subrace = ["Eladrin", "Drow", "High", "Sea", "Shadar-Kai", "Wood"]
    Subrace = random.choice(Subrace)
    DEX = StatIncrease(DEX, 2)
    if Subrace == "Eladrin" or Subrace == "Drow":
        CHA = StatIncrease(CHA, 1)
    if Subrace == "High":
        INT = StatIncrease(INT, 1)
    if Subrace == "Sea" or Subrace == "Shadar-Kai":
        CON = StatIncrease(CON, 1)
    if Subrace == "Wood":
        WIS = StatIncrease(WIS, 1)
    Age = Normal(20,700)
    if Subrace == "Eladrin":
        SizeMod = Normal(2,24)
    if Subrace == "Drow":
        SizeMod = Normal(2,12)
    if Subrace == "High" or Subrace == "Wood":
        SizeMod = Normal(2,20)
    if Subrace == "Sea" or Subrace == "Shadar-Kai":
        SizeMod = Normal(2,16)
    if Subrace == "Eladrin":
        Height = 4 * 12 + 6 + SizeMod
        Weight = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Drow":
        Height = 4 * 12 + 5 + SizeMod
        Weight = 75 + SizeMod * random.randint(1,6)
    if Subrace == "High":
        Height = 4 * 12 + 6 + SizeMod
        Weight = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Sea":
        Height = 4 * 12 + 6 + SizeMod
        Weight = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Shadar-Kai":
        Height = 4 * 12 + 8 + SizeMod
        Weight = 90 + SizeMod * random.randint(1,4)
    if Subrace == "Wood":
        Height = 4 * 12 + 6 + SizeMod
        Weight = 100 + SizeMod * random.randint(1,4)
    Eyes = ["Blue", "Violet", "Green"]
    Eyes = random.choice(Eyes)
    Skin = ["Lightly Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    Skin = random.choice(Skin)
    Hair = ["Dark Brown", "Autumn Orange", "Mossy Green", "Deep Gold"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Keen Senses", "Fey Ancestry", "Trance"])
    if Subrace == "Eladrin":
        Subrace = ["Eladrin of Autumn", "Eladrin of Winter", "Eladrin of Spring", "Eladrin of Summer"]
        Subrace = random.choice(Subrace)
        Traits.extend(["Darkvision (60ft)", "Fey Step"])
    if Subrace == "Drow":
        WeaponProficiencies.extend(["Rapiers", "Shortswords", "Hand Crossbows"])
        Traits.extend(["Darkvision (120ft)", "Sunlight Sensitivity", "Drow Magic"])
    if Subrace == "High":
        WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        Traits.extend(["Wizard Cantrip"])
    if Subrace == "Sea":
        WeaponProficiencies.extend(["Spears", "Tridents", "Light Crossbows", "Nets"])
        Traits.extend(["Swim (30ft)", "Child of the Sea", "Friend of the Sea"])
    if Subrace == "Shadar-Kai":
        Resistances.extend(["Necrotic"])
        Traits.extend(["Blessing of the Raven Queen"])
    if Subrace == "Wood":
        Speed = 35
        WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
        Traits.extend(["Mask of the Wild"])
