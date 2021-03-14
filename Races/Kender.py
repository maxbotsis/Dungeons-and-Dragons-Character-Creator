

if Race == "Kender": # Extra Race I found https://www.dndbeyond.com/races/670-kender
    DEX = StatIncrease(DEX, 2)
    CHA = StatIncrease(CHA, 1)
    Age = Normal(15,80)
    SizeMod = Normal(2,8)
    Height = 3 * 12 + 4 + SizeMod
    Weight = 50 + SizeMod * random.randint(1,4)
    Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
    Skin = random.choice(Skin)
    Hair = ["Black", "Brown", "Blonde", "Red", "White"]
    Hair = random.choice(Hair)
    Speed = 25
    Immunities.extend(["Frightened"])
    ToolProficiencies.extend(["Thieves' Tools"])
    Traits.extend(["Kender Pockets", "Nimbleness", "Taunt"])