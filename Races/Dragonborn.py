if Race == "Dragonborn":
    Subrace = ["Red", "Green", "Blue", "White", "Black", "Gold", "Silver", "Brass", "Copper", "Bronze"]
    Subrace = random.choice(Subrace)
    STR = StatIncrease(STR, 2)
    CHA = StatIncrease(CHA, 1)
    Age = Normal(15,60)
    SizeMod = Normal(2,16)
    Height = 5 * 12 + 6 + SizeMod
    Weight = 175 + SizeMod * Normal(2,12)
    Eyes = ["Red", "Gold"]
    Eyes = random.choice(Eyes)
    Skin = Subrace + " Scales"
    Speed = 30
    if Subrace == "Black":
        Resistances.extend(["Acid"])
        Traits.extend(["Acid Breath"])
    if Subrace == "Blue":
        Resistances.extend(["Lightning"])
        Traits.extend(["Lightning Breath"])
    if Subrace == "Brass":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Bronze":
        Resistances.extend(["Lightning"])
        Traits.extend(["Lightning Breath"])
    if Subrace == "Copper":
        Resistances.extend(["Acid"])
        Traits.extend(["Acid Breath"])
    if Subrace == "Gold":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Green":
        Resistances.extend(["Poison"])
        Traits.extend(["Poison Breath"])
    if Subrace == "Red":
        Resistances.extend(["Fire"])
        Traits.extend(["Fire Breath"])
    if Subrace == "Silver":
        Resistances.extend(["Cold"])
        Traits.extend(["Cold Breath"])
    if Subrace == "White":
        Resistances.extend(["Cold"])
        Traits.extend(["Cold Breath"])