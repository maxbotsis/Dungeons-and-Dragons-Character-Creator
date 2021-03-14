

    
if Race == "Tortle":
    STR = StatIncrease(STR, 2)
    WIS = StatIncrease(WIS, 1)
    Age = Normal(30,320)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 8 + SizeMod
    Weight = 350 + SizeMod * Normal(2,12)
    Eyes = ["Yellow", "Green", "Red", "Orange", "Brown", "Brownish Yellow"]
    Eyes = random.choice(Eyes)
    Skin = ["Olive Green", "Blueish Green"]
    Skin = random.choice(Skin)
    Hair = "N/A"
    Speed = 25
    SkillProficiencies.extend(["Survival"])
    Traits.extend(["Claws", "Hold Breath", "Natural Armour", "Shell Defense"])