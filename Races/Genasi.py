
if Race == "Genasi":
    Subrace = ["Air", "Earth", "Fire", "Water"]
    Subrace = random.choice(Subrace)
    CON = StatIncrease(CON, 2)
    if Subrace == "Air":
        DEX = StatIncrease(DEX, 1)
    if Subrace == "Earth":
        STR = StatIncrease(STR, 1)
    if Subrace == "Fire":
        INT = StatIncrease(INT, 1)
    if Subrace == "Water":
        WIS = StatIncrease(WIS, 1)
    Age = Normal(20,100)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 8 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    if Subrace == "Air":
        Eyes = "Pale Blue"
        Skin = "Blueish Silver"
        Hair = "Blue and Gray Crystalline Hair"
    if Subrace == "Earth":
        Eyes = "Golden"
        Skin = "Brownish Gray"
        Hair = "Black"
    if Subrace == "Fire":
        Eyes = "Reddish Orange"
        Skin = "Bronze"
        Hair = "Orange"
    if Subrace == "Water":
        Eyes = "Deep Blue"
        Skin = "Green"
        Hair = "Dark Green"
    Speed = 30
    if Subrace == "Air":
        Traits.extend(["Unending Breath", "Mingle with the Wind"])
    if Subrace == "Earth":
        Traits.extend(["Earth Walk", "Merge with Stone"])
    if Subrace == "Fire":
        Resistances.extend(["Fire"])
        Traits.extend(["Darkvision(60ft)", "Reach to the Blaze"])
    if Subrace == "Water":
        Resistances.extend(["Acid"])
        Traits.extend(["Amphibious", "Swim (30ft)", "Call to the Wave"])
