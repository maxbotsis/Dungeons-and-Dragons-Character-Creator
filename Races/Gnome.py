   
if Race == "Gnome":
    Subrace = ["Deep", "Forest", "Rock"]
    Subrace = random.choice(Subrace)
    INT = StatIncrease(INT, 2)
    if Subrace == "Deep" or Subrace == "Forest":
        DEX = StatIncrease(DEX, 1)
    if Subrace == "Rock":
        CON = StatIncrease(CON, 1)
    Age = Normal(20,400)
    SizeMod = Normal(2,8)
    Height = 2 * 12 + 11 + SizeMod
    Weight = 35 + SizeMod
    Eyes = ["Glittering Opaque Black", "Glittering Opaque Blue"]
    Eyes = random.choice(Eyes)
    Skin = ["Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Rocky Gray"]
    Skin = random.choice(Skin)
    Hair = ["Red", "Black", "Grey", "Dark Brown", "Brown", "Dirty Blonde", "Blonde", "White"]
    Hair = random.choice(Hair)
    Speed = 25
    Traits.extend(["Gnome Cunning"])
    if Subrace == "Deep":
        Traits.extend(["Darkvision (120ft)", "Stone Camoflage"])
    if Subrace == "Forest":
        Traits.extend(["Darkvision (60ft)", "Natural Illusionist", "Speak with Small Beasts"])
    if Subrace == "Rock":
        ToolProficiencies.extend(["Artisan's Tools"])
        Traits.extend(["Artificer's Lore", "Tinker"])