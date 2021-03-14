
if Race == "Half-Elf":
    Subrace = ["N/A", "Drow", "Sun", "Moon", "Wood"] # Keen Senses subrace removed because it is obsolete
    Subrace = random.choice(Subrace)
    CHA = StatIncrease(CHA, 2)
    Age = Normal(20,160)
    SizeMod = Normal(2,16)
    Height = 4 * 12 + 9 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Blue", "Violet", "Green"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
    Skin = random.choice(Skin)
    Hair = ["Red", "Blond", "Brown", "Black"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Fey Ancestry"])
    if Subrace == "N/A":
        Traits.extend(["Skill Versatility"])
    if Subrace == "Drow":
        Traits.extend(["Drow Magic"])
    if Subrace == "Sun" or Subrace == "Moon":
        Choice = random.choice(["Elf Weapon Training", "Wizard Cantrip"])
        Traits.extend([Choice])
    if Subrace == "Wood":
        Choice = random.choice(["Elf Weapon Training", "Fleet of Foot", "Mask of the Wild"])
        Traits.extend([Choice])