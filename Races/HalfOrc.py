

if Race == "Half-Orc":
    STR = StatIncrease(STR, 2)
    CON = StatIncrease(CON, 1)
    Age = Normal(14,60)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 10 + SizeMod
    Weight = 140 + SizeMod * Normal(2,12)
    Eyes = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
    Eyes = random.choice(Eyes)
    Skin = "Greyish Green"
    Hair = ["Dark Brown", "Bald", "Red"]
    Hair = random.choice(Hair)
    Speed = 30
    SkillProficiencies.extend(["Intimidation"])
    Traits.extend(["Darkvision (60ft)", "Relentless Endurance", "Savage Attacks"])