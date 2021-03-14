
if Race == "Hobgoblin":
    CON = StatIncrease(CON, 2)
    INT = StatIncrease(INT, 1)
    Age = Normal(20,80)
    SizeMod = Normal(2,16)
    Height = 5 * 12 + 6 + SizeMod
    Weight = 175 + SizeMod * Normal(2,12)
    Eyes = ["Black", "Red"]
    Eyes = random.choice(Eyes)
    Skin = ["Orange", "Dirty Orange", "Red", "Dull Red", "Reddish Brown"]
    Skin = random.choice(Skin)
    Hair = ["Dark Brown", "Dark Grey", "Orange", "Red"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Martial Training", "Saving Face"])