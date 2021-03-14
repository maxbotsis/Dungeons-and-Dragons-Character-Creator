"""
=========DUNGEONS AND DRAGONS: RANDOM CHARACTER CREATION====================

Created on Tuesday April 30 2019
Co-Author Joined: March 12 2021

@author: terreratman
@co-author: minispuks

=================================OVERVIEW====================================
This program is a Dungeons and Dragons Character creator. It simply generates
A random character depending on the user's restrictions (if any).
=============================================================================
"""
# =================================GAPS====================================

# Does not account for the level 4, 8, 12, and 16 stat increase or feat choice 
# if making a higher level character does not include languages yet because I'm 
# still investigating a method to add a random item to a list only if the 
# addition is not already in the list, and if it was already in the list, pick 
# a new item and try to add does not have a seperate category for currency 
# because I'm not sure how to account for adding from multiple sources
# Does not account for Personality Traits, Ideals or Bonds because I 
# don't want to write a random.choice for things that bulky, trying to find 
# another way not all Skin/Hair/Eye colours may be correct, I just put 
# some in quickly it does not print class traits
# =============================================================================

import random
import collections
# import Races
import Backgrounds


# def Normal(Min, Max): # Not exactly sure how this one is working, but it gives a more realistic result for age, height and weight
#     r = round(random.triangular(low = Min, high = Max))# Round gives us a whole number for a character's age
#     return r

# def HitPoints(MaxDice):
#     n = 1
#     HITPOINTS = 0
#     if Level == 1:
#         HITPOINTS = MaxDice + CONMOD 
#         if HITPOINTS <= MaxDice:  # This makes it so that the minimum HP is your HP die but you can start stronger if it "rolls well"
#             HITPOINTS = MaxDice
#         return(HITPOINTS)
#     else:
#         HITPOINTS = MaxDice + Level * CONMOD
#         while n < Level:
#             ADDITION = random.randint(1,MaxDice)
#             HITPOINTS = HITPOINTS + ADDITION
#             n += 1
#     if HITPOINTS <= MaxDice + (Level - 1):  # This makes it so the minimum HP increase is 1, I don't like to play with weakening characters
#         HITPOINTS = MaxDice + (Level - 1)
#     return(HITPOINTS)

# def StatIncrease(Stat, NumberofIncrease):
#     if Stat <= 20 - NumberofIncrease:
#         Stat = Stat + NumberofIncrease
#     else:
#         Stat = 20
#     return(Stat)
        
# def StatDecrease(Stat, NumberofDecrease):
#     if Stat >= 1 + NumberofDecrease:
#         Stat = Stat - NumberofDecrease
#     else:
#         Stat = 1
#     return(Stat)
        
# def STATMOD(STAT):
#     if STAT == 1:
#         return -5
#     if STAT == 2 or STAT == 3:
#         return -4
#     if STAT == 4 or STAT == 5:
#         return -3
#     if STAT == 6 or STAT == 7:
#         return -2
#     if STAT == 8 or STAT == 9:
#         return -1
#     if STAT == 10 or STAT == 11:
#         return 0
#     if STAT == 12 or STAT == 13:
#         return 1
#     if STAT == 14 or STAT == 15:
#         return 2
#     if STAT == 16 or STAT == 17:
#         return 3
#     if STAT == 18 or STAT == 19:
#         return 4
#     if STAT == 20:
#         return 5
    
# def RemoveDuplicates(List):
#     final_list = []
#     for num in List:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list

# STR = random.randint (1,20)
# DEX = random.randint (1,20)
# CON = random.randint (1,20)
# INT = random.randint (1,20)
# WIS = random.randint (1,20)
# CHA = random.randint (1,20)

ArmourProficiencies = []
WeaponProficiencies = []
ToolProficiencies = []
SavingThrowProficiencies = []
SkillProficiencies = []
Resistances = []
Immunities = []
Vulnerabilities = []
Traits = []
Equipment = []

# Subrace 
# Subclass 
# FightingStyle 
# HP = 0
# Age = 0
# SizeMod = 0
# Height = 0
# Weight = 0
# Eyes 
# Skin
# Hair
# Speed = 0

# Skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
# ArtisanTools = ["Alchemist's Supplies", "Brewer's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Tools", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"]
# GamingSets = ["Dice Set", "Dragonchess Set", "Playing Card Set", "Three-Dragon Ante Set"]
# MusicalInstruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"]
# MartialWeapons = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
# MartialMelee = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
# SimpleWeapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
# SimpleMelee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]

# # Race list of race objects
# Race = [Aasimar, Bugbear, Dragonborn, Dryad, Dwarf, Elf, Firbolg, Genasi, Gith, Gnome, Goblin, 
# Goliath, Hobgoblin, HalfElf, Halfling, HalfOrc, Human, Juiblexian, Kender, Kenku, Kobold, Lizardfolk, 
# Mousefolk, Orc, Succubus,Tabaxi, Tiefling, Tortle, Triton, YuanTiPureblood]

# ChosenRace = random.choice(Race)
# ChosenRace = ChosenRace() # Make object instance
    
# STRMOD = STATMOD(STR)
# DEXMOD = STATMOD(DEX)
# CONMOD = STATMOD(CON)
# INTMOD = STATMOD(INT)
# WISMOD = STATMOD(WIS)
# CHAMOD = STATMOD(CHA)

# # Class list of class objects
# Class = [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard]
# Class = random.choice(Class)
# ChosenClass - Class() # Make object instance


# Background = [Acolyte, Anthropologist, Archaeologist, BlackFistDoubleAgent, CaravanSpecialist, Charlatan, 
# CityWatch, ClanCrafter, CloisteredScholar, Courtier, Criminal, DragonCasualty, EarthspurMiner, 
# Entertainer, FactionAgent, FarTraveller, FolkHero, GateUrchin, GuildArtisan, Harborfolk, HauntedOne, 
# Hermit, HillsfarMerchant, HillsfarSmuggler, HouseAgent, Inheritor, Initiate, Inquisitor, IronRouteBandit, 
# KnightOfTheOrder, MercenaryVeteran, MulmasterAristocrat, Noble, Outlander, PhlanInsurgent, PhlanRefugee, 
# Sage, Sailor, SecretIdentity, ShadeFanatic, Soldier, StojanowPrisoner, TicklebellyNomad, TradeSheriff, 
# UrbanBountyHunter, Urchin, UthgardtTribeMember Vizier WaterdhavianNoble]

# Background = random.choice(Background)
 
# Alignment = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
# Alignment = random.choice(Alignment)

# SkillExpertises = [item for item, count in collections.Counter(SkillProficiencies).items() if count > 1] # I included this so if you get the same skill proficiency from two different sources, it becomes an expertise (it's pretty darn rare)
# ToolExpertises = [item for item, count in collections.Counter(ToolProficiencies).items() if count > 1] # You can delete these two rows if you don't want innate expertises

# #print statements

# printSummary()

# def printSummary():
#     print("Race:", Race)

#     print("Class:", Class)
#     # print("Level:", Level)
#     print("Alignment:", Alignment)
#     print("Background:", Background)
#     print("STR ", STR, " STRMOD: ", STRMOD) 
#     print("DEX ", DEX, " DEXMOD: ", DEXMOD)
#     print("CON ", CON, " CONMOD: ", CONMOD)
#     print("INT ", INT, " INTMOD: ", INTMOD)
#     print("WIS ", WIS, " WISMOD: ", WISMOD)
#     print("CHA ", CHA, " CHAMOD: ", CHAMOD)
#     print("Hit Points: ", HP)


#     if Race == "Dwarf":
#     print("Speed:", Speed, "Feet (Your Speed is not Reduced by Wearing Heavy Armour)")
#     else:
#     print("Speed:", Speed, "Feet")

#     # This can be improved

#     if ArmourProficiencies != []:
#         print("Armour Proficiencies:", ", ".join(sorted(RemoveDuplicates(ArmourProficiencies))))
#     if WeaponProficiencies != []:
#         print("Weapon Proficienceis:", ", ".join(sorted(RemoveDuplicates(WeaponProficiencies))))
#     if ToolProficiencies != []:
#         print("Tool Proficiencies:", ", ".join(sorted(RemoveDuplicates(ToolProficiencies))))
#     if ToolExpertises != []:
#         print ("Tool Expertises: ", ", ".join(sorted(RemoveDuplicates(ToolExpertises))))
#     if SavingThrowProficiencies != []:
#         print("Saving Throw Proficiencies:", ", ".join(sorted(RemoveDuplicates(SavingThrowProficiencies))))
#     if SkillProficiencies != []:
#         print("Skill Proficiencies:", ", ".join(sorted(RemoveDuplicates(SkillProficiencies))))
#     if SkillExpertises != []:
#         print ("Skill Expertises: ", ", ".join(sorted(RemoveDuplicates(SkillExpertises))))
#     if Resistances != []:
#         print("Resistances:", ", ".join(sorted(RemoveDuplicates(Resistances))))
#     if Immunities != []:
#         print("Immunities:", ", ".join(sorted(RemoveDuplicates(Immunities))))
#     if Vulnerabilities != []:
#         print("Vulnerabilities:", ", ".join(sorted(RemoveDuplicates(Vulnerabilities))))
#     if Traits != []:
#         print("Traits:", ", ".join(sorted(RemoveDuplicates(Traits))))
#     if Equipment != []:
#         print("Equipment and Weapons:", ", ".join(sorted(RemoveDuplicates(Equipment))))


    
#     print("Age:",Age)
#     print("Height: ", (Height//12), "' ", Height%12, '"', sep='')
#     print("Weight:", Weight, "Pounds")
#     print("Eye Colour:", Eyes)
#     print("Skin Colour:", Skin)
#     print("Hair Colour:", Hair)

ac = Backgrounds.Acolyte()
print(f"Skills Proficienceis:{SkillProficiencies}")
