
if Background == "Entertainer":
    Routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
    Background = "Entertainer who is " + ", and ".join(Routine)
    SkillProficiencies.extend(["Acrobatics", "Performance"])
    EntertainerMusicalInstrument = random.choice(MusicalInstruments)  # Introducing a temporary variable so the same instrument will be included in the equipment and proficiencies
    ToolProficiencies.extend(["Disguise Kit", EntertainerMusicalInstrument])
    Equipment.extend([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
    if "a Gladiator" in Routine:
        GladiatorWeapon = random.choice(["Trident", "Net"])
        WeaponProficiencies.extend([GladiatorWeapon])
        Equipment.extend([GladiatorWeapon])
    