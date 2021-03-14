
if Race == "Firbolg":
    WIS = StatIncrease(WIS, 2)
    STR = StatIncrease(STR, 1)
    Age = Normal(30,450)
    SizeMod = Normal(2,24)
    Height = 6 * 12 + 4 + SizeMod
    Weight = 210 + SizeMod * Normal(1,4)
    Eyes = ["Blue", "Violet", "Green"]
    Eyes = random.choice(Eyes) 
    Skin = ["Light Pink", "Grayish Blue"]
    Skin = random.choice(Skin)
    Hair = ["Red", "Blonde", "Dark Brown"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf"])