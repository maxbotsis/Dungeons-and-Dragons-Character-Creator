


if Race == "Lizardfolk":
    CON = StatIncrease(CON, 2)
    WIS = StatIncrease(WIS, 1)
    Age = Normal(14,45)
    SizeMod = Normal(2,20)
    Height = 4 * 12 + 9 + SizeMod
    Weight = 120 + SizeMod * Normal(2,12)
    Eyes = ["Red", "Green", "Gold", "Orange", "Blue"]
    Eyes = random.choice(Eyes)
    Skin = ["Green Scales", "Greenish Brown", "Brown Scales", "Black Scales", "Tan Scales", "Albino Scales"]
    Skin = random.choice(Skin)
    Hair = ["Pair of Spikes", "Lots of Spikes", "N/A"]
    Hair = random.choice(Hair)
    Speed = 30
    Traits.extend(["Bite", "Cunning Artisan", "Hold Breath", "Natural Armour", "Hungry Jaws"])
    LizardfolkSkills = ["Animal Handling", "Nature", "Perception", "Stealth", "Survival"]
    SkillProficiencies.extend(random.sample(LizardfolkSkills, 2))
    