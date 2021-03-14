
        
if Race == "Juiblexian":
    Subrace = ["Corrosive", "Blasphemy", "Mnemonic"]
    Subrace = random.choice(Subrace)
    CON = StatIncrease(CON, 2)
    if Subrace == "Corrosive":
        DEX = StatIncrease(DEX, 1)
    if Subrace == "Blasphemy":
        CHA = StatIncrease(CHA, 1)
    if Subrace == "Mnemonic":
        INT = StatIncrease(INT, 1)
    Age = Normal(100,200)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 10 + SizeMod
    Weight = 80 + SizeMod * Normal(2,8)
    Eyes = "N/A"
    Skin = "Transparent " + random.choice(["Green", "Blueish White", "Yellow", "Orange", "Blue", "Red"])
    Hair = "N/A"
    Speed = 30
    Immunities.extend(["Poison", "Poisoned"])
    Traits.extend(["Amorphous Ooze", "Blind Vision", "Gelatinous Trance"])
    if Subrace == "Corrosive":
        Traits.extend(["Caustic Touch", "Corrosive Body"])
        Resistances.extend(["Acid"])
    if Subrace == "Blasphemy":
        Traits.extend(["Elemental Chaos", "Innate Spellcasting"])
    if Subrace == "Mnemonic":
        Traits.extend(["False Appearance", "Mnemonic Echoes"])