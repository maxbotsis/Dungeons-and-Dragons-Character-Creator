if Race == "Bugbear":
    STR = StatIncrease(STR, 2)
    DEX = StatIncrease(DEX, 1)
    Age = Normal(16,60)
    SizeMod = Normal(2,16)
    Height = 6 * 12 + 4 + SizeMod
    Weight = 230 + SizeMod * Normal(2,12)
    Eyes = ["Yellow", "Orange", "Red", "Brown", "Greenish White"]
    Eyes = random.choice(Eyes)
    Skin = ["Yellow", "Muddy Yellow", "Reddish Orange", "Reddish Brown"]
    Skin = random.choice(Skin)
    Hair = ["Brown", "Red"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Long-Limbed", "Powerful Build", "Surprise Attack"])
    SkillProficiencies.extend(["Stealth"])