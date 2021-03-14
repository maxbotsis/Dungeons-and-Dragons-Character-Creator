
if Race == "Halfling":
    Subrace = ["Ghostwise", "Lightfoot", "Stout"]
    Subrace = random.choice(Subrace)
    DEX = StatIncrease(DEX, 2)
    if Subrace == "Ghostwise":
        WIS = StatIncrease(WIS, 1)
    if Subrace == "Lightfoot":
        CHA = StatIncrease(CHA, 1)
    if Subrace == "Stout":
        CON = StatIncrease(CON, 1)
    Age = Normal(20,200)
    SizeMod =  Normal(2,8)
    Height = 2 * 12 + 7 + SizeMod
    Weight = 35 + SizeMod
    Eyes = "Brown"
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin = random.choice(Skin)
    Hair = ["Aubrun", "Black", "Brown", "Gray"]
    Hair = random.choice(Hair)
    Speed = 25
    Traits.extend(["Lucky", "Brave", "Halfling Nimbleness"])
    if Subrace == "Ghostwise":
        Traits.extend(["Silent Speech"])
    if Subrace == "Lightfoot":
        Traits.extend(["Naturally Stealthy"])
    if Subrace == "Stout":
        Resistances.extend(["Poison"])
        Traits.extend(["Stout Resilience"])
    