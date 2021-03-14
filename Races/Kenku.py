
    
if Race == "Kenku":
    DEX = StatIncrease(DEX, 2)
    WIS = StatIncrease(WIS, 1)
    Age = Normal(12,45)
    SizeMod = Normal(2,16)
    Height = 4 * 12 + 4 + SizeMod
    Weight = 50 + SizeMod * random.randint(1,6)
    Eyes = "Beady Black"
    Skin = "Black"
    Hair = "Black Feathers"
    Speed = 30
    Traits.extend(["Expert Forgery", "Mimicry"])
    KenkuSkills = ["Acrobatics", "Deception", "Stealth", "Sleight of Hand"]
    SkillProficiencies.extend(random.sample(KenkuSkills, 2))