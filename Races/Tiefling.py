
    
if Race == "Tiefling":
    Subrace = ["Asmodeus", "Baalzebul", "Devil's Tongue", "Dispater", "Feral", "Fierna", "Glasya", "Hellfire", "Levistus", "Mammon", "Mephistopheles", "Zariel"]
    Subrace = random.choice(Subrace)
    if Subrace == "Asmodeus" or Subrace == "Baalzebul" or Subrace == "Devil's Tongue" or Subrace == "Hellfire" or Subrace == "Mammon" or Subrace == "Mephistopheles":
        CHA = StatIncrease(CHA, 2)
        INT = StatIncrease(INT, 1)
    if Subrace == "Dispater" or Subrace == "Glasya":
        CHA = StatIncrease(CHA, 2)
        DEX = StatIncrease(DEX, 1)
    if Subrace == "Feral":
        DEX = StatIncrease(DEX, 2)
        INT = StatIncrease(INT, 1)
    if Subrace == "Fierna":
        CHA = StatIncrease(CHA, 2)
        WIS = StatIncrease(WIS, 1)
    if Subrace == "Livistus":
        CHA = StatIncrease(CHA, 2)
        CON = StatIncrease(CON, 1)
    if Subrace == "Zariel":
        CHA = StatIncrease(CHA, 2)
        STR = StatIncrease(STR, 1)
    Age = Normal(20,60)
    SizeMod = Normal(2,16)
    Height = 4 * 12 + 9 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Solid Orb of Red", "Solid Orb of Black", "Solid Orb of White", "Solid Orb of Silver", "Solid Orb of Gold"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
    Skin = random.choice(Skin)
    Hair = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)"])
    Resistances.extend(["Fire"])
    if Subrace == "Asmodeus" or Subrace == "Feral":
        Traits.extend(["Infernal Legacy"])
    if Subrace == "Baalzebul":
        Traits.extend(["Legacy of Maladomini"])
    if Subrace == "Devil's Tongue":
        Traits.extend(["Devil's Tongue"])
    if Subrace == "Dispater":
        Traits.extend(["Legacy of Dis"])
    if Subrace == "Fierna":
        Traits.extend(["Legacy of Phlegethos"])
    if Subrace == "Glasya":
        Traits.extend(["Legacy of Malbolge"])
    if Subrace == "Hellfire":
        Traits.extend(["Hellfire"])
    if Subrace == "Levistus":
        Traits.extend(["Legacy of Stygia"])
    if Subrace == "Mammon":
        Traits.extend(["Legacy of Minauros"])
    if Subrace == "Mephistopheles":
        Traits.extend(["Legacy of Cania"])
    if Subrace == "Zariel":
        Traits.extend(["Legacy of Avernus"])