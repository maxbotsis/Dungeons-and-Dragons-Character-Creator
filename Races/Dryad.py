if Race == "Dryad": # Extra Race I found https://www.dandwiki.com/wiki/Dryad_(5e_Race)
    Subrace = ["Watcher"]  # Leaving this as a list in case I can find a balanced version of the Guardian subclass
    Subrace = random.choice(Subrace)
    DEX = StatIncrease(DEX, 1)
    WIS = StatIncrease(WIS, 2)
    Age = "N/A"
    SizeMod = Normal(2,6)
    Height = 5 * 12 + 5 + SizeMod
    Weight = 40 + SizeMod * Normal(2,6)
    Eyes = "Changes with the Seasons"
    Skin = ["Orange", "Green", "Yellowish Green"]
    Skin = random.choice(Skin)
    Hair = "Leaves that Change with the Seasons"
    Speed = 30
    Traits.extend(["Barkskin", "Forest Blend", "Photosynthesis", "Tree Stride", "Nature Whisperer"])
    Vulnerabilities.extend(["Fire"])