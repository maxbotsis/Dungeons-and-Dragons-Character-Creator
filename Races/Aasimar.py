class Aasimar:

    # Subrace = ["Fallen", "Protector", "Scourge"]
    Subrace = {
        "Fallen": 
        "Protector":
        "Scourge":
        }


    def __init__(): 
         Subrace = random.choice(Subrace)
         CHA = StatIncrease(CHA, 2)

         


    
    
    if Subrace == "Fallen":
        STR = StatIncrease(STR, 1)
    if Subrace == "Protector":
        WIS = StatIncrease(WIS, 1)
    if Subrace == "Scourge":
        CON = StatIncrease(CON, 1)
    Age = Normal(20,140)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 10 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Pupil-less Pale White", "Pupil-less Gold", "Pupil-less Gray", "Pupil-less Topaz"]
    Eyes = random.choice(Eyes)
    Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Emerald", "Gold", "Silver"]
    Skin = random.choice(Skin)
    Hair = ["Red", "Blond", "Brown", "Black", "Silver"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Healing Hands", "Light Bearer"])
    Resistances.extend(["Necrotic", "Radiant"])

    # if Level >= 3:
    #     if Subrace == "Fallen":
    #         Traits.extend(["Necrotic Shroud"])
    #     if Subrace == "Protector":
    #         Traits.extend(["Radiant Soul"])
    #     if Subrace == "Scourge":
    #         Traits.extend(["Radiant Consumption"])