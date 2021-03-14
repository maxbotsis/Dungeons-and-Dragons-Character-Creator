
    
if Race == "Triton":
    STR = StatIncrease(STR, 1)
    CON = StatIncrease(CON, 1)
    CHA = StatIncrease(CHA, 1)
    Age = Normal(15,170)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 6 + SizeMod
    Weight = 90 + SizeMod * Normal(2,8)
    Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
    Eyes = random.choice(Eyes)
    Skin = ["Silver", "Blueish Silver"]
    Skin = random.choice(Skin)
    Hair = ["Deep Blue", "Greenish Blue", "Green"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths"])