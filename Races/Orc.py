 

if Race == "Orc":
    STR = StatIncrease(STR, 2)
    CON = StatIncrease(CON, 1)
    INT = StatDecrease(INT, 2)
    Age = Normal(12,30)
    SizeMod = Normal(2,16)
    Height = 5 * 12 + 4 + SizeMod
    Weight = 175 + SizeMod * Normal(2,12)
    Eyes = "Red"
    Skin = ["Greenish Grey", "Light Grey", "Dark Grey"]
    Skin = random.choice(Skin)
    Hair = "Black"
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Aggressive", "Powerful Build"])
    SkillProficiencies.extend(["Intimidation"])