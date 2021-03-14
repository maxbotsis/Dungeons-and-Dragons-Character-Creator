# import Main

# class Aasimar:

#     Subrace = ["Fallen", "Protector", "Scourge"]
#     Subrace = random.choice(Subrace)


#     CHA = StatIncrease(CHA, 2)
#     if Subrace == "Fallen":
#         STR = StatIncrease(STR, 1)
#     if Subrace == "Protector":
#         WIS = StatIncrease(WIS, 1)
#     if Subrace == "Scourge":
#         CON = StatIncrease(CON, 1)

#     Age = Normal(20,140)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 10 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Pupil-less Pale White", "Pupil-less Gold", "Pupil-less Gray", "Pupil-less Topaz"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Emerald", "Gold", "Silver"]
#     Skin = random.choice(Skin)
#     Hair = ["Red", "Blond", "Brown", "Black", "Silver"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Healing Hands", "Light Bearer"])
#     Resistances.extend(["Necrotic", "Radiant"])
    
    
# if Race == "Bugbear":
#     STR = StatIncrease(STR, 2)
#     DEX = StatIncrease(DEX, 1)
#     Age = Normal(16,60)
#     SizeMod = Normal(2,16)
#     Height = 6 * 12 + 4 + SizeMod
#     Weight = 230 + SizeMod * Normal(2,12)
#     Eyes = ["Yellow", "Orange", "Red", "Brown", "Greenish White"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Yellow", "Muddy Yellow", "Reddish Orange", "Reddish Brown"]
#     Skin = random.choice(Skin)
#     Hair = ["Brown", "Red"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Long-Limbed", "Powerful Build", "Surprise Attack"])
#     SkillProficiencies.extend(["Stealth"])
    
# if Race == "Dragonborn":
#     Subrace = ["Red", "Green", "Blue", "White", "Black", "Gold", "Silver", "Brass", "Copper", "Bronze"]
#     Subrace = random.choice(Subrace)
#     STR = StatIncrease(STR, 2)
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(15,60)
#     SizeMod = Normal(2,16)
#     Height = 5 * 12 + 6 + SizeMod
#     Weight = 175 + SizeMod * Normal(2,12)
#     Eyes = ["Red", "Gold"]
#     Eyes = random.choice(Eyes)
#     Skin = Subrace + " Scales"
#     Speed = 30
#     if Subrace == "Black":
#         Resistances.extend(["Acid"])
#         Traits.extend(["Acid Breath"])
#     if Subrace == "Blue":
#         Resistances.extend(["Lightning"])
#         Traits.extend(["Lightning Breath"])
#     if Subrace == "Brass":
#         Resistances.extend(["Fire"])
#         Traits.extend(["Fire Breath"])
#     if Subrace == "Bronze":
#         Resistances.extend(["Lightning"])
#         Traits.extend(["Lightning Breath"])
#     if Subrace == "Copper":
#         Resistances.extend(["Acid"])
#         Traits.extend(["Acid Breath"])
#     if Subrace == "Gold":
#         Resistances.extend(["Fire"])
#         Traits.extend(["Fire Breath"])
#     if Subrace == "Green":
#         Resistances.extend(["Poison"])
#         Traits.extend(["Poison Breath"])
#     if Subrace == "Red":
#         Resistances.extend(["Fire"])
#         Traits.extend(["Fire Breath"])
#     if Subrace == "Silver":
#         Resistances.extend(["Cold"])
#         Traits.extend(["Cold Breath"])
#     if Subrace == "White":
#         Resistances.extend(["Cold"])
#         Traits.extend(["Cold Breath"])

# if Race == "Dryad": # Extra Race I found https://www.dandwiki.com/wiki/Dryad_(5e_Race)
#     Subrace = ["Watcher"]  # Leaving this as a list in case I can find a balanced version of the Guardian subclass
#     Subrace = random.choice(Subrace)
#     DEX = StatIncrease(DEX, 1)
#     WIS = StatIncrease(WIS, 2)
#     Age = "N/A"
#     SizeMod = Normal(2,6)
#     Height = 5 * 12 + 5 + SizeMod
#     Weight = 40 + SizeMod * Normal(2,6)
#     Eyes = "Changes with the Seasons"
#     Skin = ["Orange", "Green", "Yellowish Green"]
#     Skin = random.choice(Skin)
#     Hair = "Leaves that Change with the Seasons"
#     Speed = 30
#     Traits.extend(["Barkskin", "Forest Blend", "Photosynthesis", "Tree Stride", "Nature Whisperer"])
#     Vulnerabilities.extend(["Fire"])
    
# if Race == "Dwarf":
#     Subrace = ["Duergar", "Hill", "Mountain"]
#     Subrace = random.choice(Subrace)
#     CON = StatIncrease(CON, 2)
#     if Subrace == "Hill":
#         WIS = StatIncrease(WIS, 1)
#     if Subrace == "Mountain":
#         STR = StatIncrease(STR, 2)
#     if Subrace == "Duergar":
#         STR = StatIncrease(STR, 1)
#     Age = Normal(20,320)
#     SizeMod = Normal(2,8)
#     if Subrace == "Hill":
#         Height = 3 * 12 + 8 + SizeMod
#         Weight = 115 + SizeMod * Normal(2,12)
#     if Subrace == "Mountain":
#         Height = 4 * 12 + SizeMod
#         Weight = 130 + SizeMod * Normal(2,12)
#     if Subrace == "Duergar":
#         Height = 3 * 12 + 8 + SizeMod
#         Weight = 115 + SizeMod * Normal(2,12)
#     Eyes = ["Brown", "Hazel", "Green"]
#     Eyes = random.choice(Eyes)
#     Skin = ["White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
#     Skin = random.choice(Skin)
#     Hair = ["Bald", "Brown", "Black", "Blond", "Red"]
#     Hair = random.choice(Hair)
#     Speed = 25
#     WeaponProficiencies.extend(["Battleaxe", "Handaxe", "Throwing Hammer", "Warhammer"])
#     Traits.extend(["Dwarven Resilience"])
#     if Subrace == "Hill":
#         HP = HP + Level
#         Traits.extend(["Darkvision (60ft)"])
#     if Subrace == "Mountain":
#         ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
#         Traits.extend(["Darkvision (60ft)"])
#     if Subrace == "Duergar":
#         Traits.extend(["Darkvision (120ft)", "Duergar Resilience", "Duergar Magic", "Sunlight Sensitivity"])
    
# if Race == "Elf":
#     Subrace = ["Eladrin", "Drow", "High", "Sea", "Shadar-Kai", "Wood"]
#     Subrace = random.choice(Subrace)
#     DEX = StatIncrease(DEX, 2)
#     if Subrace == "Eladrin" or Subrace == "Drow":
#         CHA = StatIncrease(CHA, 1)
#     if Subrace == "High":
#         INT = StatIncrease(INT, 1)
#     if Subrace == "Sea" or Subrace == "Shadar-Kai":
#         CON = StatIncrease(CON, 1)
#     if Subrace == "Wood":
#         WIS = StatIncrease(WIS, 1)
#     Age = Normal(20,700)
#     if Subrace == "Eladrin":
#         SizeMod = Normal(2,24)
#     if Subrace == "Drow":
#         SizeMod = Normal(2,12)
#     if Subrace == "High" or Subrace == "Wood":
#         SizeMod = Normal(2,20)
#     if Subrace == "Sea" or Subrace == "Shadar-Kai":
#         SizeMod = Normal(2,16)
#     if Subrace == "Eladrin":
#         Height = 4 * 12 + 6 + SizeMod
#         Weight = 90 + SizeMod * random.randint(1,4)
#     if Subrace == "Drow":
#         Height = 4 * 12 + 5 + SizeMod
#         Weight = 75 + SizeMod * random.randint(1,6)
#     if Subrace == "High":
#         Height = 4 * 12 + 6 + SizeMod
#         Weight = 90 + SizeMod * random.randint(1,4)
#     if Subrace == "Sea":
#         Height = 4 * 12 + 6 + SizeMod
#         Weight = 90 + SizeMod * random.randint(1,4)
#     if Subrace == "Shadar-Kai":
#         Height = 4 * 12 + 8 + SizeMod
#         Weight = 90 + SizeMod * random.randint(1,4)
#     if Subrace == "Wood":
#         Height = 4 * 12 + 6 + SizeMod
#         Weight = 100 + SizeMod * random.randint(1,4)
#     Eyes = ["Blue", "Violet", "Green"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Lightly Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
#     Skin = random.choice(Skin)
#     Hair = ["Dark Brown", "Autumn Orange", "Mossy Green", "Deep Gold"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Keen Senses", "Fey Ancestry", "Trance"])
#     if Subrace == "Eladrin":
#         Subrace = ["Eladrin of Autumn", "Eladrin of Winter", "Eladrin of Spring", "Eladrin of Summer"]
#         Subrace = random.choice(Subrace)
#         Traits.extend(["Darkvision (60ft)", "Fey Step"])
#     if Subrace == "Drow":
#         WeaponProficiencies.extend(["Rapiers", "Shortswords", "Hand Crossbows"])
#         Traits.extend(["Darkvision (120ft)", "Sunlight Sensitivity", "Drow Magic"])
#     if Subrace == "High":
#         WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
#         Traits.extend(["Wizard Cantrip"])
#     if Subrace == "Sea":
#         WeaponProficiencies.extend(["Spears", "Tridents", "Light Crossbows", "Nets"])
#         Traits.extend(["Swim (30ft)", "Child of the Sea", "Friend of the Sea"])
#     if Subrace == "Shadar-Kai":
#         Resistances.extend(["Necrotic"])
#         Traits.extend(["Blessing of the Raven Queen"])
#     if Subrace == "Wood":
#         Speed = 35
#         WeaponProficiencies.extend(["Longswords", "Shortswords", "Shortbows", "Longbows"])
#         Traits.extend(["Mask of the Wild"])

# if Race == "Firbolg":
#     WIS = StatIncrease(WIS, 2)
#     STR = StatIncrease(STR, 1)
#     Age = Normal(30,450)
#     SizeMod = Normal(2,24)
#     Height = 6 * 12 + 4 + SizeMod
#     Weight = 210 + SizeMod * Normal(1,4)
#     Eyes = ["Blue", "Violet", "Green"]
#     Eyes = random.choice(Eyes) 
#     Skin = ["Light Pink", "Grayish Blue"]
#     Skin = random.choice(Skin)
#     Hair = ["Red", "Blonde", "Dark Brown"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf"])

# if Race == "Genasi":
#     Subrace = ["Air", "Earth", "Fire", "Water"]
#     Subrace = random.choice(Subrace)
#     CON = StatIncrease(CON, 2)
#     if Subrace == "Air":
#         DEX = StatIncrease(DEX, 1)
#     if Subrace == "Earth":
#         STR = StatIncrease(STR, 1)
#     if Subrace == "Fire":
#         INT = StatIncrease(INT, 1)
#     if Subrace == "Water":
#         WIS = StatIncrease(WIS, 1)
#     Age = Normal(20,100)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 8 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     if Subrace == "Air":
#         Eyes = "Pale Blue"
#         Skin = "Blueish Silver"
#         Hair = "Blue and Gray Crystalline Hair"
#     if Subrace == "Earth":
#         Eyes = "Golden"
#         Skin = "Brownish Gray"
#         Hair = "Black"
#     if Subrace == "Fire":
#         Eyes = "Reddish Orange"
#         Skin = "Bronze"
#         Hair = "Orange"
#     if Subrace == "Water":
#         Eyes = "Deep Blue"
#         Skin = "Green"
#         Hair = "Dark Green"
#     Speed = 30
#     if Subrace == "Air":
#         Traits.extend(["Unending Breath", "Mingle with the Wind"])
#     if Subrace == "Earth":
#         Traits.extend(["Earth Walk", "Merge with Stone"])
#     if Subrace == "Fire":
#         Resistances.extend(["Fire"])
#         Traits.extend(["Darkvision(60ft)", "Reach to the Blaze"])
#     if Subrace == "Water":
#         Resistances.extend(["Acid"])
#         Traits.extend(["Amphibious", "Swim (30ft)", "Call to the Wave"])

# if Race == "Gith":
#     Subrace = ["Githyanki", "Githzerai"]
#     Subrace = random.choice(Subrace)
#     INT = StatIncrease(INT, 1)
#     if Subrace == "Githyanki":
#         STR = StatIncrease(STR, 2)
#     if Subrace == "Githzerai":
#         WIS = StatIncrease(WIS, 2)
#     Age = Normal(20,80)
#     SizeMod = Normal(2,24)
#     if Subrace == "Githyanki":
#         Height = 5 * 12 + SizeMod
#         Weight = 100 + SizeMod * Normal(2,8)
#     if Subrace == "Githzerai":
#         Height = 4 * 12 + 11 + SizeMod
#         Weight = 90 + SizeMod * Normal(2,8)
#     Eyes = "Yellow"
#     Skin = ["Fair", "Pale Yellow with Green Tones", "Pale Yellow with Brown Tones"]
#     Skin = random.choice(Skin)
#     Hair = ["Russet", "Black", "Gray"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     if Subrace == "Githyanki":
#         ArmourProficiencies.extend(["Light Armour", "Medium Armour"])
#         WeaponProficiencies.extend(["Shortswords", "Longswords", "Greatswords"])
#         Traits.extend(["Decadent Mastery", "Githyanki Psionics"])
#     if Subrace == "Githzerai":
#         Traits.extend(["Mental Discipline", "Githzerai Psionics"])
    
# if Race == "Gnome":
#     Subrace = ["Deep", "Forest", "Rock"]
#     Subrace = random.choice(Subrace)
#     INT = StatIncrease(INT, 2)
#     if Subrace == "Deep" or Subrace == "Forest":
#         DEX = StatIncrease(DEX, 1)
#     if Subrace == "Rock":
#         CON = StatIncrease(CON, 1)
#     Age = Normal(20,400)
#     SizeMod = Normal(2,8)
#     Height = 2 * 12 + 11 + SizeMod
#     Weight = 35 + SizeMod
#     Eyes = ["Glittering Opaque Black", "Glittering Opaque Blue"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Rocky Gray"]
#     Skin = random.choice(Skin)
#     Hair = ["Red", "Black", "Grey", "Dark Brown", "Brown", "Dirty Blonde", "Blonde", "White"]
#     Hair = random.choice(Hair)
#     Speed = 25
#     Traits.extend(["Gnome Cunning"])
#     if Subrace == "Deep":
#         Traits.extend(["Darkvision (120ft)", "Stone Camoflage"])
#     if Subrace == "Forest":
#         Traits.extend(["Darkvision (60ft)", "Natural Illusionist", "Speak with Small Beasts"])
#     if Subrace == "Rock":
#         ToolProficiencies.extend(["Artisan's Tools"])
#         Traits.extend(["Artificer's Lore", "Tinker"])

# if Race == "Goblin":
#     DEX = StatIncrease(DEX, 2)
#     CON = StatIncrease(CON, 1)
#     Age = Normal(10,35)
#     SizeMod = Normal(2,8)
#     Height = 2 * 12 + 11 + SizeMod
#     Weight = 40 + SizeMod
#     Eyes = "Beady Black"
#     Skin = ["Brownish Orange", "Greenish Orange", "Brownish Green", "Green"]
#     Skin = random.choice(Skin)
#     Hair = ["Black", "Deep Grey", "Silver"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Fury of the Small", "Nimble Escape"])

# if Race == "Goliath":
#     STR = StatIncrease(STR, 2)
#     CON = StatIncrease(CON, 1)
#     Age = Normal(20,80)
#     SizeMod = Normal(2,20)
#     Height = 6 * 12 + 8 + SizeMod
#     Weight = 270 + SizeMod * Normal(2,12)
#     Eyes = ["Blue", "Green"]
#     Eyes = random.choice(Eyes)
#     Skin = "Grey"
#     Hair = ["Black", "Dark Brown", "Dark Grey"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     SkillProficiencies.extend(["Athletics"])
#     Traits.extend(["Stone's Endurance", "Powerful Build", "Mountain Born"])
    
# if Race == "Hobgoblin":
#     CON = StatIncrease(CON, 2)
#     INT = StatIncrease(INT, 1)
#     Age = Normal(20,80)
#     SizeMod = Normal(2,16)
#     Height = 5 * 12 + 6 + SizeMod
#     Weight = 175 + SizeMod * Normal(2,12)
#     Eyes = ["Black", "Red"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Orange", "Dirty Orange", "Red", "Dull Red", "Reddish Brown"]
#     Skin = random.choice(Skin)
#     Hair = ["Dark Brown", "Dark Grey", "Orange", "Red"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Martial Training", "Saving Face"])

# if Race == "Half-Elf":
#     Subrace = ["N/A", "Drow", "Sun", "Moon", "Wood"] # Keen Senses subrace removed because it is obsolete
#     Subrace = random.choice(Subrace)
#     CHA = StatIncrease(CHA, 2)
#     Age = Normal(20,160)
#     SizeMod = Normal(2,16)
#     Height = 4 * 12 + 9 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Blue", "Violet", "Green"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown"]
#     Skin = random.choice(Skin)
#     Hair = ["Red", "Blond", "Brown", "Black"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Fey Ancestry"])
#     if Subrace == "N/A":
#         Traits.extend(["Skill Versatility"])
#     if Subrace == "Drow":
#         Traits.extend(["Drow Magic"])
#     if Subrace == "Sun" or Subrace == "Moon":
#         Choice = random.choice(["Elf Weapon Training", "Wizard Cantrip"])
#         Traits.extend([Choice])
#     if Subrace == "Wood":
#         Choice = random.choice(["Elf Weapon Training", "Fleet of Foot", "Mask of the Wild"])
#         Traits.extend([Choice])

# if Race == "Halfling":
#     Subrace = ["Ghostwise", "Lightfoot", "Stout"]
#     Subrace = random.choice(Subrace)
#     DEX = StatIncrease(DEX, 2)
#     if Subrace == "Ghostwise":
#         WIS = StatIncrease(WIS, 1)
#     if Subrace == "Lightfoot":
#         CHA = StatIncrease(CHA, 1)
#     if Subrace == "Stout":
#         CON = StatIncrease(CON, 1)
#     Age = Normal(20,200)
#     SizeMod =  Normal(2,8)
#     Height = 2 * 12 + 7 + SizeMod
#     Weight = 35 + SizeMod
#     Eyes = "Brown"
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
#     Skin = random.choice(Skin)
#     Hair = ["Aubrun", "Black", "Brown", "Gray"]
#     Hair = random.choice(Hair)
#     Speed = 25
#     Traits.extend(["Lucky", "Brave", "Halfling Nimbleness"])
#     if Subrace == "Ghostwise":
#         Traits.extend(["Silent Speech"])
#     if Subrace == "Lightfoot":
#         Traits.extend(["Naturally Stealthy"])
#     if Subrace == "Stout":
#         Resistances.extend(["Poison"])
#         Traits.extend(["Stout Resilience"])
    
# if Race == "Half-Orc":
#     STR = StatIncrease(STR, 2)
#     CON = StatIncrease(CON, 1)
#     Age = Normal(14,60)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 10 + SizeMod
#     Weight = 140 + SizeMod * Normal(2,12)
#     Eyes = ["Reddish Brown", "Reddish Blue", "Reddish Green", "Reddish Grey"]
#     Eyes = random.choice(Eyes)
#     Skin = "Greyish Green"
#     Hair = ["Dark Brown", "Bald", "Red"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     SkillProficiencies.extend(["Intimidation"])
#     Traits.extend(["Darkvision (60ft)", "Relentless Endurance", "Savage Attacks"])

# if Race == "Human": # I have not accounted for the different Human ethnicities
#     Subrace = ["Stat Increase", "Variant", "Variant"] # Two chances for variant, just to spice things up
#     Subrace = random.choice(Subrace)
#     if Subrace == "Stat Increase":
#         STR = StatIncrease(STR, 1)
#         DEX = StatIncrease(DEX, 1)
#         CON = StatIncrease(CON, 1)
#         INT = StatIncrease(INT, 1)
#         WIS = StatIncrease(WIS, 1)
#         CHA = StatIncrease(CHA, 1)
#     if Subrace == "Variant":
#         Choices = random.sample(Stats, 2)  # Stats list is found on line 101 above the STR/DEX/CON/INT/WIS/CHA = 0
#         if "STR" in Choices:
#             STR = StatIncrease(STR, 1)
#         if "DEX" in Choices:
#             DEX = StatIncrease(DEX, 1)
#         if "CON" in Choices:
#             CON = StatIncrease(CON, 1)
#         if "INT" in Choices:
#             INT = StatIncrease(INT, 1)
#         if "WIS" in Choices:
#             WIS = StatIncrease(WIS, 1)
#         if "CHA" in Choices:
#             CHA = StatIncrease(CHA, 1)        
#     Age = Normal(20,60)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 8 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
#     Skin = random.choice(Skin)
#     Hair = ["Black", "Brown", "Blonde", "Red", "White"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     if Subrace == "Variant":
#         Traits.extend(["Choice of Feat"])
#         SkillProficiencies.extend([random.choice(Skills)])
        
# if Race == "Juiblexian":
#     Subrace = ["Corrosive", "Blasphemy", "Mnemonic"]
#     Subrace = random.choice(Subrace)
#     CON = StatIncrease(CON, 2)
#     if Subrace == "Corrosive":
#         DEX = StatIncrease(DEX, 1)
#     if Subrace == "Blasphemy":
#         CHA = StatIncrease(CHA, 1)
#     if Subrace == "Mnemonic":
#         INT = StatIncrease(INT, 1)
#     Age = Normal(100,200)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 10 + SizeMod
#     Weight = 80 + SizeMod * Normal(2,8)
#     Eyes = "N/A"
#     Skin = "Transparent " + random.choice(["Green", "Blueish White", "Yellow", "Orange", "Blue", "Red"])
#     Hair = "N/A"
#     Speed = 30
#     Immunities.extend(["Poison", "Poisoned"])
#     Traits.extend(["Amorphous Ooze", "Blind Vision", "Gelatinous Trance"])
#     if Subrace == "Corrosive":
#         Traits.extend(["Caustic Touch", "Corrosive Body"])
#         Resistances.extend(["Acid"])
#     if Subrace == "Blasphemy":
#         Traits.extend(["Elemental Chaos", "Innate Spellcasting"])
#     if Subrace == "Mnemonic":
#         Traits.extend(["False Appearance", "Mnemonic Echoes"])

# if Race == "Kender": # Extra Race I found https://www.dndbeyond.com/races/670-kender
#     DEX = StatIncrease(DEX, 2)
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(15,80)
#     SizeMod = Normal(2,8)
#     Height = 3 * 12 + 4 + SizeMod
#     Weight = 50 + SizeMod * random.randint(1,4)
#     Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
#     Skin = random.choice(Skin)
#     Hair = ["Black", "Brown", "Blonde", "Red", "White"]
#     Hair = random.choice(Hair)
#     Speed = 25
#     Immunities.extend(["Frightened"])
#     ToolProficiencies.extend(["Thieves' Tools"])
#     Traits.extend(["Kender Pockets", "Nimbleness", "Taunt"])
    
# if Race == "Kenku":
#     DEX = StatIncrease(DEX, 2)
#     WIS = StatIncrease(WIS, 1)
#     Age = Normal(12,45)
#     SizeMod = Normal(2,16)
#     Height = 4 * 12 + 4 + SizeMod
#     Weight = 50 + SizeMod * random.randint(1,6)
#     Eyes = "Beady Black"
#     Skin = "Black"
#     Hair = "Black Feathers"
#     Speed = 30
#     Traits.extend(["Expert Forgery", "Mimicry"])
#     KenkuSkills = ["Acrobatics", "Deception", "Stealth", "Sleight of Hand"]
#     SkillProficiencies.extend(random.sample(KenkuSkills, 2))
    
# if Race == "Kobold":
#     DEX = StatIncrease(DEX, 2)
#     STR = StatDecrease(STR, 2)
#     Age = Normal(8,80)
#     SizeMod = Normal(2,8)
#     Height = 2 * 12 + 1 + SizeMod
#     Weight = 25 + SizeMod
#     Eyes = ["Burnt Orange", "Red"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Reddish Brown", "Green", "Blue"]
#     Skin = random.choice(Skin)
#     Hair = "N/A"
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Grovel, Cower and Beg", "Pack Tactics", "Sunlight Sensitivity"])

# if Race == "Lizardfolk":
#     CON = StatIncrease(CON, 2)
#     WIS = StatIncrease(WIS, 1)
#     Age = Normal(14,45)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 9 + SizeMod
#     Weight = 120 + SizeMod * Normal(2,12)
#     Eyes = ["Red", "Green", "Gold", "Orange", "Blue"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Green Scales", "Greenish Brown", "Brown Scales", "Black Scales", "Tan Scales", "Albino Scales"]
#     Skin = random.choice(Skin)
#     Hair = ["Pair of Spikes", "Lots of Spikes", "N/A"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Bite", "Cunning Artisan", "Hold Breath", "Natural Armour", "Hungry Jaws"])
#     LizardfolkSkills = ["Animal Handling", "Nature", "Perception", "Stealth", "Survival"]
#     SkillProficiencies.extend(random.sample(LizardfolkSkills, 2))
    
# if Race == "Mousefolk": # Extra Race I found https://www.dndbeyond.com/races/61879-mousefolk
#     DEX = StatIncrease(DEX, 2)
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(10,45)
#     SizeMod = Normal(2,8)
#     Height = 2 * 12 + 11 + SizeMod
#     Weight = 40 + SizeMod
#     Eyes = ["Pink", "Black"]
#     Eyes = random.choice(Eyes)
#     Skin = "Pink"
#     Hair = ["Beige Fur", "Black Fur", "Chocolate Fur", "Coffee Fur", "Cream Fur", "Ivory Fur", "Lilac Fur", "Silver Fur", "White Fur", "Tan Fur"]
#     Hair = random.choice(Hair)
#     Speed = 25
#     Traits.extend(["Darkvision (60ft)", "Light Sleeper", "Mouse's Agility", "Mousefolk Senses", "Mouse's Survival"]) # I will be ediditing some of these for my campaign as they aren't well balanced
    
# if Race == "Orc":
#     STR = StatIncrease(STR, 2)
#     CON = StatIncrease(CON, 1)
#     INT = StatDecrease(INT, 2)
#     Age = Normal(12,30)
#     SizeMod = Normal(2,16)
#     Height = 5 * 12 + 4 + SizeMod
#     Weight = 175 + SizeMod * Normal(2,12)
#     Eyes = "Red"
#     Skin = ["Greenish Grey", "Light Grey", "Dark Grey"]
#     Skin = random.choice(Skin)
#     Hair = "Black"
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Aggressive", "Powerful Build"])
#     SkillProficiencies.extend(["Intimidation"])
    
# if Race == "Succubus": # Extra class I found https://www.dndbeyond.com/races/1524-succubus
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(20,1000)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 8 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Glowing Red", "Glowing Blue", "Glowing Brown", "Glowing Green"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Tan", "Olive", "White"]
#     Skin = random.choice(Skin)
#     Hair = ["Black", "Red"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     SkillProficiencies.extend(["Persuasion"])
#     Traits.extend(["Charm", "Darkvision (60ft)", "Fiendish Nature", "Shapechanger", "Small Wings"]) # I might switch some of these around with playtesting
#     Vulnerabilities.extend(["Radiant"])

# if Race == "Tabaxi":
#     DEX = StatIncrease(DEX, 2)
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(20,60)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 10 + SizeMod
#     Weight = 90 + SizeMod * Normal(2,8)
#     Eyes = ["Green", "Yellow"]
#     Eyes = random.choice(Eyes)
#     Skin = "Pink"
#     Hair = ["Yelow", "Spotted Yellow", "Orange", "Spotted Orange", "Red", "Spotted Red"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)", "Feline Agility", "Cat Claws"])
#     SkillProficiencies.extend(["Perception", "Stealth"])
    
# if Race == "Tiefling":
#     Subrace = ["Asmodeus", "Baalzebul", "Devil's Tongue", "Dispater", "Feral", "Fierna", "Glasya", "Hellfire", "Levistus", "Mammon", "Mephistopheles", "Zariel"]
#     Subrace = random.choice(Subrace)
#     if Subrace == "Asmodeus" or Subrace == "Baalzebul" or Subrace == "Devil's Tongue" or Subrace == "Hellfire" or Subrace == "Mammon" or Subrace == "Mephistopheles":
#         CHA = StatIncrease(CHA, 2)
#         INT = StatIncrease(INT, 1)
#     if Subrace == "Dispater" or Subrace == "Glasya":
#         CHA = StatIncrease(CHA, 2)
#         DEX = StatIncrease(DEX, 1)
#     if Subrace == "Feral":
#         DEX = StatIncrease(DEX, 2)
#         INT = StatIncrease(INT, 1)
#     if Subrace == "Fierna":
#         CHA = StatIncrease(CHA, 2)
#         WIS = StatIncrease(WIS, 1)
#     if Subrace == "Livistus":
#         CHA = StatIncrease(CHA, 2)
#         CON = StatIncrease(CON, 1)
#     if Subrace == "Zariel":
#         CHA = StatIncrease(CHA, 2)
#         STR = StatIncrease(STR, 1)
#     Age = Normal(20,60)
#     SizeMod = Normal(2,16)
#     Height = 4 * 12 + 9 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Solid Orb of Red", "Solid Orb of Black", "Solid Orb of White", "Solid Orb of Silver", "Solid Orb of Gold"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black", "Light Red", "Maroon", "Burgundy", "Dark Red", "Red"]
#     Skin = random.choice(Skin)
#     Hair = ["Red", "Brown", "Black", "Dark Blue", "Purple"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Darkvision (60ft)"])
#     Resistances.extend(["Fire"])
#     if Subrace == "Asmodeus" or Subrace == "Feral":
#         Traits.extend(["Infernal Legacy"])
#     if Subrace == "Baalzebul":
#         Traits.extend(["Legacy of Maladomini"])
#     if Subrace == "Devil's Tongue":
#         Traits.extend(["Devil's Tongue"])
#     if Subrace == "Dispater":
#         Traits.extend(["Legacy of Dis"])
#     if Subrace == "Fierna":
#         Traits.extend(["Legacy of Phlegethos"])
#     if Subrace == "Glasya":
#         Traits.extend(["Legacy of Malbolge"])
#     if Subrace == "Hellfire":
#         Traits.extend(["Hellfire"])
#     if Subrace == "Levistus":
#         Traits.extend(["Legacy of Stygia"])
#     if Subrace == "Mammon":
#         Traits.extend(["Legacy of Minauros"])
#     if Subrace == "Mephistopheles":
#         Traits.extend(["Legacy of Cania"])
#     if Subrace == "Zariel":
#         Traits.extend(["Legacy of Avernus"])
    
# if Race == "Tortle":
#     STR = StatIncrease(STR, 2)
#     WIS = StatIncrease(WIS, 1)
#     Age = Normal(30,320)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 8 + SizeMod
#     Weight = 350 + SizeMod * Normal(2,12)
#     Eyes = ["Yellow", "Green", "Red", "Orange", "Brown", "Brownish Yellow"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Olive Green", "Blueish Green"]
#     Skin = random.choice(Skin)
#     Hair = "N/A"
#     Speed = 25
#     SkillProficiencies.extend(["Survival"])
#     Traits.extend(["Claws", "Hold Breath", "Natural Armour", "Shell Defense"])
    
# if Race == "Triton":
#     STR = StatIncrease(STR, 1)
#     CON = StatIncrease(CON, 1)
#     CHA = StatIncrease(CHA, 1)
#     Age = Normal(15,170)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 6 + SizeMod
#     Weight = 90 + SizeMod * Normal(2,8)
#     Eyes = ["Brown", "Hazel", "Blue", "Green", "Grey", "Amber"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Silver", "Blueish Silver"]
#     Skin = random.choice(Skin)
#     Hair = ["Deep Blue", "Greenish Blue", "Green"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Traits.extend(["Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardians of the Depths"])
    
# if Race == "Yuan-Ti Pureblood":
#     CHA = StatIncrease(CHA, 2)
#     INT = StatIncrease(INT, 1)
#     Age = Normal(20,60)
#     SizeMod = Normal(2,20)
#     Height = 4 * 12 + 8 + SizeMod
#     Weight = 110 + SizeMod * Normal(2,8)
#     Eyes = ["Red", "Orange", "Silver", "Copper", "Green", "Yellow"]
#     Eyes = random.choice(Eyes)
#     Skin = ["Light/Pale White", "White/Fair", "Lightly Tanned", "Medium/Tanned", "Olive/Moderate Brown", "Brown", "Dark Brown", "Very Dark Brown/Black"]
#     Skin = random.choice(Skin)
#     Hair = ["Black", "Brown", "Blonde", "Red", "White"]
#     Hair = random.choice(Hair)
#     Speed = 30
#     Immunities.extend(["Poison", "Poisoned"])
#     Traits.extend(["Darkvision (60ft)", "Innate Spellcasting", "Magic Resistance"])