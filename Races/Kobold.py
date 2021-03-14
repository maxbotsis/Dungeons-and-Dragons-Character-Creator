

    
if Race == "Kobold":
    DEX = StatIncrease(DEX, 2)
    STR = StatDecrease(STR, 2)
    Age = Normal(8,80)
    SizeMod = Normal(2,8)
    Height = 2 * 12 + 1 + SizeMod
    Weight = 25 + SizeMod
    Eyes = ["Burnt Orange", "Red"]
    Eyes = random.choice(Eyes)
    Skin = ["Reddish Brown", "Green", "Blue"]
    Skin = random.choice(Skin)
    Hair = "N/A"
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Grovel, Cower and Beg", "Pack Tactics", "Sunlight Sensitivity"])