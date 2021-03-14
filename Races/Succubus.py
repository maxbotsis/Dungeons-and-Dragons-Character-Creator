
    
if Race == "Succubus": # Extra class I found https://www.dndbeyond.com/races/1524-succubus
    CHA = StatIncrease(CHA, 1)
    Age = Normal(20,1000)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 8 + SizeMod
    Weight = 110 + SizeMod * Normal(2,8)
    Eyes = ["Glowing Red", "Glowing Blue", "Glowing Brown", "Glowing Green"]
    Eyes = random.choice(Eyes)
    Skin = ["Tan", "Olive", "White"]
    Skin = random.choice(Skin)
    Hair = ["Black", "Red"]
    Hair = random.choice(Hair)
    Speed = 30
    SkillProficiencies.extend(["Persuasion"])
    Traits.extend(["Charm", "Darkvision (60ft)", "Fiendish Nature", "Shapechanger", "Small Wings"]) # I might switch some of these around with playtesting
    Vulnerabilities.extend(["Radiant"])
