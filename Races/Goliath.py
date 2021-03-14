
if Race == "Goliath":
    STR = StatIncrease(STR, 2)
    CON = StatIncrease(CON, 1)
    Age = Normal(20,80)
    SizeMod = Normal(2,20)
    Height = 6 * 12 + 8 + SizeMod
    Weight = 270 + SizeMod * Normal(2,12)
    Eyes = ["Blue", "Green"]
    Eyes = random.choice(Eyes)
    Skin = "Grey"
    Hair = ["Black", "Dark Brown", "Dark Grey"]
    Hair = random.choice(Hair)
    Speed = 30
    SkillProficiencies.extend(["Athletics"])
    Traits.extend(["Stone's Endurance", "Powerful Build", "Mountain Born"])
    