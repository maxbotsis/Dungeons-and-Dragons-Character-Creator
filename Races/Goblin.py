
if Race == "Goblin":
    DEX = StatIncrease(DEX, 2)
    CON = StatIncrease(CON, 1)
    Age = Normal(10,35)
    SizeMod = Normal(2,8)
    Height = 2 * 12 + 11 + SizeMod
    Weight = 40 + SizeMod
    Eyes = "Beady Black"
    Skin = ["Brownish Orange", "Greenish Orange", "Brownish Green", "Green"]
    Skin = random.choice(Skin)
    Hair = ["Black", "Deep Grey", "Silver"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Fury of the Small", "Nimble Escape"])
