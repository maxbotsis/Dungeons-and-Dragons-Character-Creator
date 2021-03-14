
   
if Race == "Tabaxi":
    DEX = StatIncrease(DEX, 2)
    CHA = StatIncrease(CHA, 1)
    Age = Normal(20,60)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 10 + SizeMod
    Weight = 90 + SizeMod * Normal(2,8)
    Eyes = ["Green", "Yellow"]
    Eyes = random.choice(Eyes)
    Skin = "Pink"
    Hair = ["Yelow", "Spotted Yellow", "Orange", "Spotted Orange", "Red", "Spotted Red"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Darkvision (60ft)", "Feline Agility", "Cat Claws"])
    SkillProficiencies.extend(["Perception", "Stealth"])