

if Race == "Human": # I have not accounted for the different Human ethnicities
    Subrace = ["Stat Increase", "Variant", "Variant"] # Two chances for variant, just to spice things up
    Subrace = random.choice(Subrace)
    if Subrace == "Stat Increase":
        STR = StatIncrease(STR, 1)
        DEX = StatIncrease(DEX, 1)
        CON = StatIncrease(CON, 1)
        INT = StatIncrease(INT, 1)
        WIS = StatIncrease(WIS, 1)
        CHA = StatIncrease(CHA, 1)
    if Subrace == "Variant":
        Choices = random.sample(Stats, 2)  # Stats list is found on line 101 above the STR/DEX/CON/INT/WIS/CHA = 0
        if "STR" in Choices:
            STR = StatIncrease(STR, 1)
        if "DEX" in Choices:
            DEX = StatIncrease(DEX, 1)
        if "CON" in Choices:
            CON = StatIncrease(CON, 1)
        if "INT" in Choices:
            INT = StatIncrease(INT, 1)
        if "WIS" in Choices:
            WIS = StatIncrease(WIS, 1)
        if "CHA" in Choices:
            CHA = StatIncrease(CHA, 1)        
    Age = Normal(20,60)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 8 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin = random.choice(Skin)
    Hair = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair = random.choice(Hair)
    Speed = 30
    if Subrace == "Variant":
        Traits.extend(["Choice of Feat"])
        SkillProficiencies.extend([random.choice(Skills)])