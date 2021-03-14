
if Race == "Gith":
    Subrace = ["Githyanki", "Githzerai"]
    Subrace = random.choice(Subrace)
    INT = StatIncrease(INT, 1)
    if Subrace == "Githyanki":
        STR = StatIncrease(STR, 2)
    if Subrace == "Githzerai":
        WIS = StatIncrease(WIS, 2)
    Age = Normal(20,80)
    SizeMod = Normal(2,24)
    if Subrace == "Githyanki":
        Height = 5 * 12 + SizeMod
        Weight = 100 + SizeMod * Normal(2,8)
    if Subrace == "Githzerai":
        Height = 4 * 12 + 11 + SizeMod
        Weight = 90 + SizeMod * Normal(2,8)
    Eyes = "Yellow"
    Skin = ["Fair", "Pale Yellow with Green Tones", "Pale Yellow with Brown Tones"]
    Skin = random.choice(Skin)
    Hair = ["Russet", "Black", "Gray"]
    Hair = random.choice(Hair)
    Speed = 30
    if Subrace == "Githyanki":
        ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
        WeaponProficiencies.extend(["Shortswords", "Longswords", "Greatswords"])
        Traits.extend(["Decadent Mastery", "Githyanki Psionics"])
    if Subrace == "Githzerai":
        Traits.extend(["Mental Discipline", "Githzerai Psionics"])