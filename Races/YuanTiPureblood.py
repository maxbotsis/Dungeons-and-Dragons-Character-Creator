
    
if Race == "Yuan-Ti-Pureblood":
    CHA = StatIncrease(CHA, 2)
    INT = StatIncrease(INT, 1)
    Age = Normal(20,60)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 8 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Red", "Orange", "Silver", "Copper", "Green", "Yellow"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin = random.choice(Skin)
    Hair = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair = random.choice(Hair)
    Speed = 30
    Immunities.extend(["Poison", "Poisoned"])
    Traits.extend(["Darkvision (60ft)", "Innate Spellcasting", "Magic Resistance"])