# import Main


# if Class == "Barbarian":
#     if Level >= 3:
#         Subclass = ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Berserker", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of the Zealot"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(12)
#     ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
#     WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
#     SavingThrowProficiencies.extend(["STR", "CON"])
#     SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2))
#     Equipment.extend([random.choice(["Greataxe", random.choice(MartialMelee)]), random.choice(["Two Handaxes", random.choice(SimpleWeapons)]), "Explorer's Pack", "Four Javelins"])
    
# if Class == "Bard":
#     if Level >= 3:
#         Subclass = ["College of Glamour", "College of Lore", "College of Satire", "College of Swords", "College of Valor", "College of Whispers"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(8)
#     ArmourProficiencies.extend(["Light Armour"])
#     WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
#     ToolProficiencies.extend(random.sample(MusicalInstruments, 3))
#     SavingThrowProficiencies.extend(["DEX", "CHA"])
#     SkillProficiencies.extend(random.sample(Skills, 3))
#     Equipment.extend([random.choice(["Rapier", "Longsword", random.choice(SimpleWeapons)]), random.choice(["Diplomat's Pack", "Entertainer's Pack"]), random.choice(["Lute", random.choice(MusicalInstruments)]), "Leather Armour", "Dagger"])
    
# # =============================================================================
# # if Class == "Blood Hunter":
# # =============================================================================

# # =============================================================================
# # if Class == "Cardcaster":
# # =============================================================================
    
# if Class == "Cleric":
#     Subclass = ["Arcana Domain", "Ambition Domain", "City Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Order Domain", "Protection Domain", "Solidarity Domain", "Strength Domain", "Tempest Domain", "Trickery Domain", "War Domain", "Zeal Domain"]
#     Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(8)
#     ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
#     WeaponProficiencies.extend(["Simple Weapons"])
#     SavingThrowProficiencies.extend(["WIS", "CHA"])
#     SkillProficiencies.extend(random.sample(["History", "Insight", "Medicine", "Persuasion", "Religion"], 2))
#     if "Warhammer" in WeaponProficiencies or "Martial Weapons" in WeaponProficiencies:
#         Equipment.extend([random.choice(["Mace", "Warhammer"])])
#     else:
#         Equipment.extend(["Mace"])
#     if "Chain Mail" in ArmourProficiencies or "Heavy Armour" in ArmourProficiencies:
#         Equipment.extend([random.choice(["Scale Mail", "Leather Armour", "Chain Mail"])])
#     else:
#         Equipment.extend([random.choice(["Scale Mail", "Leather Armour"])])
#     Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Priest's Pack", "Explorer's Pack"]), "Shield", "Holy Symbol"])
    
# # =============================================================================
# # if Class == "Diabolist":
# # =============================================================================
    
# if Class == "Druid":
#     if Level >= 2:
#         Subclass = ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of Spores", "Circle of Twilight"]
#         Subclass = random.choice(Subclass)
#         if Subclass == "Circle of the Land":
#             Land = random.choice(["(Arctic)", "(Coast)", "(Desert)", "(Forest)", "(Grassland)", "(Mountain)", "(Swamp)", "(Underdark)"])
#             Subclass = "Circle of the Land " + Land
#     HP = HP + HitPoints(8)
#     ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
#     WeaponProficiencies.extend(["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"])
#     ToolProficiencies.extend(["Herbalism Kit"])
#     SavingThrowProficiencies.extend(["INT", "WIS"])
#     SkillProficiencies.extend(random.sample(["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2))
#     Equipment.extend([random.choice(["Wooden Shield", random.choice(SimpleWeapons)]), random.choice(["Scimitar", random.choice(SimpleMelee)]), "Leather Armour", "Explorer's Pack", "Druidic Focus"])
    
# # =============================================================================
# # if Class == "Feywalker":
# # =============================================================================
    
# if Class == "Fighter":
#     FightingStyle = ["Archery", "Defense", "Dueling", "Great Weapon Fighting", "Protection", "Two-Weapon Fighting"]
#     FightingStyle = random.choice(FightingStyle)
#     if Level >= 3:
#         Subclass = ["Arcane Archer", "Battle Master", "Brute", "Cavalier", "Champion", "Eldritch Knight", "Purple Dragon Knight", "Samurai", "Scout", "Sharpshooter"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(10)
#     ArmourProficiencies.extend(["Light Armour, Medium Armour, Heavy Armour", "Shields"])
#     WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
#     SavingThrowProficiencies.extend(["STR", "CON"])
#     SkillProficiencies.extend(random.sample(["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2))
# # =============================================================================
# #   This whole equipment section got messed up because one choice of equipment gives multiple items, which gives my code lists within lists. My print functions don't work with lists within lists. I'm looking for a way to simplify this. Similar issue encountered with Paladin and Ranger
# # =============================================================================
#     EqptExtnd = [random.choice(["Light Crossbow with 20 Bolts", "Two Handaxes"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"])]
#     EqptExtnd.extend(random.choice([["Chain Mail"], ["Leather Armour", "Longbow with 20 Arrows"]]))
#     EqptExtnd.extend(random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)]))
#     Equipment.extend(EqptExtnd)
    
# if Class == "Monk":
#     if Level >= 3:
#         Subclass = ["Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul", "Way of Tranquility"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(8)
#     WeaponProficiencies.extend(["Simple Weapons", "Shortswords"])
#     ToolProficiencies.extend([random.choice([random.choice(MusicalInstruments), random.choice(ArtisanTools)])])
#     SavingThrowProficiencies.extend(["STR", "DEX"])
#     SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2))
#     Equipment.extend([random.choice(["Shortsword", random.choice(SimpleWeapons)]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "10 Darts"])
    
# # =============================================================================
# # if Class == "Morph":
# # =============================================================================
    
# # =============================================================================
# # if Class == "Occultist":
# # =============================================================================
    
# if Class == "Paladin":
#     if Level >= 2:
#         FightingStyle = ["Defense", "Dueling", "Great Weapon Fighting", "Protection"]
#         FightingStyle = random.choice(FightingStyle)
#     if Level >= 3:
#         Subclass = ["Oath of the Ancients", "Oath of Conquests", "Oath of the Crown", "Oath of Devotion", "Oath of Redemption", "Oath of Vengeance", "Oathbreaker", "Oath of Treachery"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(10)
#     ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Heavy Armour", "Shields"])
#     WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
#     SavingThrowProficiencies.extend(["WIS", "CHA"])
#     SkillProficiencies.extend(random.sample(["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2))
#     EqptExtnd = random.choice([[random.choice(MartialWeapons), "Shield"], random.sample(MartialWeapons, 2)])
#     EqptExtnd.extend([random.choice(["5 Javelins", random.choice(SimpleMelee)])])
#     EqptExtnd.extend(["Chain Mail", "Holy Symbol"])
#     Equipment.extend(EqptExtnd)
    
# if Class == "Ranger":
#     if Level >= 2:
#         FightingStyle = ["Archery", "Defense", "Dueling", "Two-Weapon Fighting"]
#         FightingStyle = random.choice(FightingStyle)
#     if Level >= 3:
#         Subclass = ["Beast Master", "Gloom Stalker", "Horizon Walker", "Hunter", "Monster Slayer", "Primeval Guardian"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(10)
#     ArmourProficiencies.extend(["Light Armour", "Medium Armour", "Shields"])
#     WeaponProficiencies.extend(["Simple Weapons", "Martial Weapons"])
#     SavingThrowProficiencies.extend(["STR", "DEX"])
#     SkillProficiencies.extend(random.sample(["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3))
#     EqptExtnd =[random.choice(["Scale Mail", "Leather Armour"])]
#     EqptExtnd.extend(random.choice([["Two Shortswords"], random.sample(SimpleMelee, 2)]))
#     EqptExtnd.extend([random.choice(["Dungeoneer's Pack", "Explorer's Pack"])])
#     EqptExtnd.extend(["Longbow with 20 Arrows"])
#     Equipment.extend(EqptExtnd)
    
# if Class == "Rogue":
#     if Level >= 3:
#         Subclass = ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Scout", "Swashbuckler", "Thief"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(8)
#     ArmourProficiencies.extend(["Light Armour"])
#     WeaponProficiencies.extend(["Simple Weapons", "Hand Crossbows", "Longswords", "Rapiers", "Shortswords"])
#     ToolProficiencies.extend(["Thieves' Tools"])
#     SavingThrowProficiencies.extend(["DEX", "INT"])
#     SkillProficiencies.extend(random.sample(["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4))
#     Equipment.extend([random.choice(["Rapier", "Shortsword"]), random.choice(["Shortbow with 20 Arrows", "Shortsword"]), random.choice(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"]), "Leather Armour", "Two Daggers", "Thieves's Tools"])
    
# if Class == "Sorcerer":
#     Subclass = ["Divine Soul", "Draconic Bloodline", "Giant Soul", "Pheonix Sorcery", "Pyromancer", "Sea Sorcery", "Shadow Magic", "Stone Soercery", "Storm Sorcery", "Wild Magic"]
#     Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(6)
#     WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
#     SavingThrowProficiencies.extend(["CON", "CHA"])
#     SkillProficiencies.extend(random.sample(["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2))
#     Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Dungeoneer's Pack", "Explorer's Pack"]), "Two Daggers"])
    
# if Class == "Warlock":
#     Subclass = ["The Archfey", "The Celestial", "The Fiend", "The Ghost in the Machine", "The Great Old One", "The Hexblade", "The Raven Queen", "The Seeker", "The Undying"]
#     Subclass = random.choice(Subclass)
#     if Level >= 3:
#         FightingStyle = ["Pact of the Chain", "Pact of the Blade", "Pact of the Tome"]
#         FightingStyle = random.choice(FightingStyle)
#     HP = HP + HitPoints(8)
#     ArmourProficiencies.extend(["Light Armour"])
#     WeaponProficiencies.extend(["Simple Weapons"])
#     SavingThrowProficiencies.extend(["WIS", "CHA"])
#     SkillProficiencies.extend(random.sample(["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2))
#     Equipment.extend([random.choice(["Light Crossbow with 20 Bolts", random.choice(SimpleWeapons)]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Dungeoneer's Pack"]), "Leather Armour", random.choice(SimpleWeapons), "Two Daggers"])
    
# if Class == "Wizard":
#     if Level >= 2:
#         Subclass = ["Artificier", "Bladesinger", "Lore Mastery", "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Invention", "School of Necromancy", "School of Transmutation", "Technomancy", "Theurgy", "War Magic"]
#         Subclass = random.choice(Subclass)
#     HP = HP + HitPoints(6)
#     WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
#     SavingThrowProficiencies.extend(["INT", "WIS"])
#     SkillProficiencies.extend(random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2))
#     Equipment.extend([random.choice(["Quarterstaff", "Dagger"]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Explorer's Pack"]), "Spellbook"])
