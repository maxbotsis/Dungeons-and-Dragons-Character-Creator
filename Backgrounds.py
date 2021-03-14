import Dungeons_and_Dragons_Character_Creation


# if Background == "Acolyte":
#     SkillProficiencies.extend(["Insight", "Religion"])
#     Equipment.extend(["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes", "15 gp"])
    
# if Background == "Anthropologist":
#     SkillProficiencies.extend(["Insight", "Religion"])
#     Equipment.extend(["Leather-Bound Diary", "Bottle of Ink", "Ink Pen", "Set of Traveler's Clothes", "One Trinket of Special Significance", "10 gp"])
    
# if Background == "Archaeologist":
#     SkillProficiencies.extend(["History", "Survival"])
#     ToolProficiencies.extend([random.choice(["Cartographer's Tools", "Navigator's Tools"])])
#     Equipment.extend([random.choice(["Wooden Case Containing a Map to a Ruin", "Wooden Case Containing a Map to a Dungeon"]), "Bullseye Lantern", "Miner's Pick", "Set of Traveler's Clothes", "Shovel", "Two-Person Tent", "Trinket Recovered from a Dig Site", "25 gp"])

# if Background == "Black Fist Double Agent":
#     SkillProficiencies.extend(["Deception", "Insight"])
#     BlackFistDoubleAgentTool = random.choice([random.choice(GamingSets), random.choice(ArtisanTools)])
#     ToolProficiencies.extend(["Disguise Kit", BlackFistDoubleAgentTool])
#     Equipment.extend(["Disguise Kit", "Common Clothes", "Tears of Virulence Emblem", "Writ of Free Agency Signed by the Lord Regent", BlackFistDoubleAgentTool, "15 gp"])
    
# if Background == "Caravan Specialist":
#     SkillProficiencies.extend(["Animal Handling", "Survival"])
#     ToolProficiencies.extend(["Land Vehicles"])
#     Equipment.extend(["Whip", "Tent", "Regional Map", "Traveling Clothes", "10 gp"])
    
# if Background == "Charlatan":
#     SkillProficiencies.extend(["Deception", "Sleight of Hand"])
#     ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
#     Equipment.extend(["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"]), "15 gp"])
    
# if Background == "City Watch":
#     Background = random.choice(["City Watch Patrol", "City Watch Investigator"])
#     SkillProficiencies.extend(["Insight"])
#     if Background == "City Watch Patrol":
#         SkillProficiencies.extend(["Athletics"])
#     if Background == "City Watch Investigator":
#         SkillProficiencies.extend(["Investigation"])
#     Equipment.extend(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    
# if Background == "Clan Crafter":
#     SkillProficiencies.extend(["History", "Insight"])
#     ClanCrafterArtisanTools = random.choice(ArtisanTools)
#     ToolProficiencies.extend([ClanCrafterArtisanTools])
#     Equipment.extend([ClanCrafterArtisanTools, "Maker's Mark Chisel", "Traveler's Clothes", "Gem Worth 10 gp", "5 gp"])
    
# if Background == "Cloistered Scholar":
#     SkillProficiencies.extend(["History", random.choice(["Arcana", "Nature", "Religion"])])
#     Equipment.extend(["Scholar's Robes of Your Cloister", "Writing Kit", "Borrowed Book on the Subject of Your Current Study", "10 gp"])
    
# if Background == "Cormanthor Refugee":
#     SkillProficiencies.extend(["Nature", "Survival"])
#     CormanthorRefugeeArtisanTools = random.choice(ArtisanTools) # Introducing a temporary variable so the same artisan's tools will be included in the equipment and proficiencies
#     ToolProficiencies.extend([CormanthorRefugeeArtisanTools])
#     Equipment.extend(["Two-Person Tent", CormanthorRefugeeArtisanTools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    
# if Background == "Courtier":
#     SkillProficiencies.extend(["Insight", "Persuasion"])
#     Equipment.extend(["Set of Fine Clothes", "5 gp"])
    
# if Background == "Criminal":
#     Specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
#     Background = "Criminal " + random.choice(Specialty)
#     SkillProficiencies.extend(["Deception", "Stealth"])
#     ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])

# # =============================================================================
# # if Background == "Dissenter":  # Don't know what Dissenters get for proficiencies or equipment
# #     SkillProficiencies.extend([])
# # =============================================================================
    
# if Background == "Dragon Casualty": # Tool proficiency is based on origin
#     Origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
#     Background = "Dragon Casualty who used to be a " + Origin
#     if Origin == "Dockworker/Fisherman":
#         ToolProficiencies.extend(["Water Vehicles"])
#     if Origin == "Tradesperson/Merchant":
#         ToolProficiencies.extend([random.choice(ArtisanTools)])
#     if Origin == "Black Fist Soldier":
#         ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), "Land Vehicles"])])
#     if Origin == "Adventurer":
#         ToolProficiencies.extend(["Land Vehicles"])
#     if Origin == "Entertainer":
#         ToolProficiencies.extend([random.choice(MusicalInstruments)])
#     if Origin == "Scholar/Healer":
#         ToolProficiencies.extend([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
#     if Origin == "Criminal":
#         ToolProficiencies.extend([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
#     if Origin == "Unskilled Labourer":
#         ToolProficiencies.extend([random.choice(GamingSets)])
#     SkillProficiencies.extend(["Intimidation", "Survival"])
#     Equipment.extend(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])

# if Background == "Earthspur Miner":
#     SkillProficiencies.extend(["Athletics", "Survival"])
#     Equipment.extend([random.choice(["Shovel", "Miner's Pick"]), "Block and Tackle", "Climber's Kit", "Set of Common Clothes", "5 gp"])
    
# if Background == "Entertainer":
#     Routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
#     Background = "Entertainer who is " + ", and ".join(Routine)
#     SkillProficiencies.extend(["Acrobatics", "Performance"])
#     EntertainerMusicalInstrument = random.choice(MusicalInstruments)  # Introducing a temporary variable so the same instrument will be included in the equipment and proficiencies
#     ToolProficiencies.extend(["Disguise Kit", EntertainerMusicalInstrument])
#     Equipment.extend([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
#     if "a Gladiator" in Routine:
#         GladiatorWeapon = random.choice(["Trident", "Net"])
#         WeaponProficiencies.extend([GladiatorWeapon])
#         Equipment.extend([GladiatorWeapon])
    
# if Background == "Faction Agent":
#     Faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
#     Background = "Faction Agent of " + Faction
#     SkillProficiencies.extend(["Insight"])
#     if Faction == "The Emerald Enclave":
#         SkillProficiencies.extend(["Nature"])
#     if Faction == "The Harpers":
#         SkillProficiencies.extend(["Investigation"])
#     if Faction == "The Lord's Alliance":
#         SkillProficiencies.extend(["History"])
#     if Faction == "The Order of the Gauntlet":
#         SkillProficiencies.extend(["Religion"])
#     if Faction == "The Zhentarim":
#         SkillProficiencies.extend(["Deception"])
#     Equipment.extend([random.choice(["Badge of " + Faction, "Emblem of " + Faction]), "Set of Common Clothes", "15 gp"])
#     if Faction == "The Harpers" or Faction == "The Zhentarim":
#         Equipment.extend(["Copy of a Code-Book from " + Faction])
#     else: 
#         Equipment.extend(["Copy of a Seminal Text from " + Faction])
    
# if Background == "Far Traveler":
#     Reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
#     Origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
#     Background = "Far Traveler " + Reason + " from " + Origin
#     SkillProficiencies.extend(["Insight", "Perception"])
#     FarTravelerTool = random.choice([random.choice(MusicalInstruments), random.choice(GamingSets)])
#     ToolProficiencies.extend([FarTravelerTool])
#     Equipment.extend([FarTravelerTool, "Poorly Wrought Maps from " + Origin, "Small Piece of Jewelry Worth 10 gp from " + Origin, "5 gp"])
    
# if Background == "Folk Hero":
#     SkillProficiencies.extend(["Animal Handling", "Survival"])
#     FolkHeroTools = random.choice(ArtisanTools)
#     ToolProficiencies.extend([FolkHeroTools, "Land Vehicles"])
#     Equipment.extend([FolkHeroTools, "Shovel", "Iron Pot", "Set of Common Clothes", "10 gp"])
    
# if Background == "Gate Urchin":
#     SkillProficiencies.extend(["Deception", "Sleight of Hand"])
#     GateUrchinMusicalInstrument = random.choice(MusicalInstruments)
#     ToolProficiencies.extend(["Thieves' Tools", GateUrchinMusicalInstrument])
#     Equipment.extend(["Battered Alms Box", GateUrchinMusicalInstrument, random.choice(["Cast-Off Military Jacket", "Cast-Off Cap", "Cast-Off Scarf"]), "Set of Common Clothes", "10 gp"])
    
# if Background == "Guild Artisan":
#     SkillProficiencies.extend(["Insight", "Persuasion"])
#     GuildArtisanTools = random.choice(ArtisanTools)
#     ToolProficiencies.extend([GuildArtisanTools])
#     Equipment.extend([GuildArtisanTools, "Letter of Introduction from Your Guild", "15 gp"])
    
# if Background == "Harborfolk":
#     SkillProficiencies.extend(["Athletics", "Sleight of Hand"])
#     HarborfolkGamingSet = random.choice(GamingSets)
#     ToolProficiencies.extend([HarborfolkGamingSet, "Water Vehicles"])
#     Equipment.extend([HarborfolkGamingSet, "Fishing Tackle", "Set of Common Clothes", "Rowboat", "5 gp"])
    
# if Background == "Haunted One":
#     SkillProficiencies.extend(random.choice(["Arcana", "Investigation", "Religion", "Survival"]))
#     Equipment.extend(["Monster Hunter's Pack", "Gothic Trinket"])

# if Background == "Hermit":
#     SkillProficiencies.extend(["Medicine", "Religion"])
#     ToolProficiencies.extend(["Herbalism Kit"])
#     Equipment.extend(["Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit", "5 gp"])
    
# if Background == "Hillsfar Merchant":
#     SkillProficiencies.extend(["Insight", "Persuasion"])
#     ToolProficiencies.extend(["Land Vehicles", "Water Vehicles"])
#     Equipment.extend(["Set of Clothes", "Signet Ring", "Letter of Introduction from Your Family's Trading House", "25 gp"])

# if Background == "Hillsfar Smuggler":
#     SkillProficiencies.extend(["Perception", "Stealth"])
#     ToolProficiencies.extend(["Forgery Kit"])
#     Equipment.extend(["Forgery Kit", "Set of Common Clothes", "5 gp"])
    
# if Background == "House Agent":
#     House = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
#     Background = "House Agent of the " + House + " House"
#     SkillProficiencies.extend(["Investigation", "Persuasion"])
#     if House == "Cannith":
#         ToolProficiencies.extend(["Alchemist's Supplies", "Tinker's Tools"])
#     if House == "Deneith":
#         ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
#     if House == "Ghallanda":
#         ToolProficiencies.extend(["Brewer's Supplies", "Cook's Utensils"])
#     if House == "Jorasco":
#         ToolProficiencies.extend(["Alchemist's Supplies", "Herbalism Kit"])
#     if House == "Kundarak":
#         ToolProficiencies.extend(["Tinker's Tools", "Thieves' Tools"])
#     if House == "Lyrandar":
#         ToolProficiencies.extend(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
#     if House == "Medani":
#         ToolProficiencies.extend(["Thieves' Tools", "Disguise Kit"])
#     if House == "Orien":
#         ToolProficiencies.extend(["Land Vehicles", random.choice(GamingSets)])
#     if House == "Phiarlan":
#         ToolProficiencies.extend(["Disguise Kit", random.choice(MusicalInstruments)])
#     if House == "Sivis":
#         ToolProficiencies.extend(["Calligrapher's Tools", "Forgery Kit"])
#     if House == "Tharashk":
#         ToolProficiencies.extend(["Thieve's Tools", random.choice(GamingSets)])
#     if House == "Thuranni":
#         ToolProficiencies.extend(["Poisoner's Kit", random.choice(GamingSets)])
#     if House == "Vadalis":
#         ToolProficiencies.extend(["Land Vehicles", "Herbalism Kit"])
#     Equipment.extend(["Set of Fine Clothes", House + " Signet Ring", "ID Papers", "20 gp"])
    
# if Background == "Inheritor":
#     SkillProficiencies.extend(["Survival", random.choice(["Arcana", "History", "Religion"])])
#     InheritorTool = random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])
#     ToolProficiencies.extend([InheritorTool])
#     Equipment.extend(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", InheritorTool, "15 gp"])
    
# if Background == "Initiate":
#     SkillProficiencies.extend(["Athletics", "Intimidation"])
#     InitiateGamingSet = random.choice(GamingSets)
#     ToolProficiencies.extend([InitiateGamingSet, "Land Vehicles"])
#     Equipment.extend(["Simple Puzzle Box", "Scroll Containing the Teachings of the Gods", InitiateGamingSet, "Set of Common Clothes", "15 gp"])
    
# if Background == "Inquisitor":
#     SkillProficiencies.extend(["Investigation", "Religion"])
#     ToolProficiencies.extend([random.choice(ArtisanTools), "Thieves' Tools"])
#     Equipment.extend(["Holy Symbol", "Set of Traveler's Clothes", "15 gp"])
    
# if Background == "Iron Route Bandit":
#     SkillProficiencies.extend(["Animal Handling", "Stealth"])
#     ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
#     Equipment.extend(["Set of Dark Common Clothes", "Pack Saddle", "Burglar's Pack", "5 gp"])
    
# if Background == "Knight of the Order":
#     Order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
#     Background = "Knight of the Order of " + Order
#     SkillProficiencies.extend(["Persuasion"])
#     if Order == "the Unicorn":
#         SkillProficiencies.extend([random.choice(["Arcana", "Religion"])])
#     if Order == "Myth Drannor":
#         SkillProficiencies.extend([random.choice(["Nature", "History"])])
#     if Order == "the Silver Chalice":
#         SkillProficiencies.extend([random.choice(["History", "Religion"])])
#     ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
#     Equipment.extend(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + Order, "10 gp"])
    
# if Background == "Mercenary Veteran":
#     Company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
#     Background = "Mercenary Veteran from " + Company
#     SkillProficiencies.extend(["Athletics", "Persuasion"])
#     MercenaryVeteranGamingSet = random.choice(GamingSets)
#     ToolProficiencies.extend([MercenaryVeteranGamingSet, "Land Vehicles"])
#     Equipment.extend(["Uniform from " + Company, "Insignia of Your Rank from " + Company, MercenaryVeteranGamingSet, "10 gp"])
    
# if Background == "Mulmaster Aristocrat":
#     SkillProficiencies.extend(["Deception", "Performance"])
#     MulmasterAristocratArtisanTool = random.choice(ArtisanTools)
#     MulmasterAristocratMusicalInstrument = random.choice(MusicalInstruments)
#     ToolProficiencies.extend([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument])
#     Equipment.extend([random.choice([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument]), "Set of Fine Clothes", "10 gp"])
    
# if Background == "Noble":
#     SkillProficiencies.extend(["History", "Persuasion"])
#     ToolProficiencies.extend([random.choice(GamingSets)])
#     Equipment.extend(["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 gp"])
    
# if Background == "Outlander":
#     Origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
#     Background = "Outlander " + Origin
#     SkillProficiencies.extend(["Athletics", "Survival"])
#     ToolProficiencies.extend([random.choice(MusicalInstruments)])
#     Equipment.extend(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
    
# if Background == "Phlan Insurgent":
#     SkillProficiencies.extend(["Stealth", "Survival"])
#     ToolProficiencies.extend([random.choice(ArtisanTools), "Land Vehicles"])
#     Equipment.extend(["Bag of 20 Caltrops", "Small Trinket from Your Home", "Healer's Kit", "Set of Dark Common Clothes", "5 gp"])

# if Background == "Phlan Refugee":
#     SkillProficiencies.extend(["Athletics", "Insight"])
#     PhlanRefugeeTool = random.choice(ArtisanTools)
#     ToolProficiencies.extend([PhlanRefugeeTool])
#     Equipment.extend([PhlanRefugeeTool, "Token from Home", "Set of Traveler's Clothes", "15 gp"])
    
# if Background == "Sage":
#     Specialty = random.choice(["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor", "Researcher", "Wizard's Apprentice", "Scribe"])
#     Background = "Sage " + Specialty
#     SkillProficiencies.extend(["Arcana", "History"])
#     Equipment.extend(["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes", "10 gp"])
    
# if Background == "Sailor":
#     SkillProficiencies.extend(["Athletics", "Perception"])
#     ToolProficiencies.extend(["Navigator's Tools", "Water Vehicles"])
#     Equipment.extend(["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes", "10 gp"])
    
# if Background == "Secret Identity": # Has to be non human
#     SkillProficiencies.extend(["Deception", "Stealth"])
#     ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
#     Equipment.extend(["Disguise Kit", "Forgery Kit", "Set of Common Clothes", "5 gp"])
    
# if Background == "Shade Fanatic":
#     SkillProficiencies.extend(["Deception", "Intimidation"])
#     ToolProficiencies.extend(["Forgery Kit"])
#     Equipment.extend(["Forgery Kit", "Transparent Cylinder of Shadow that has no Opening", "Signet Ring", "Set of Fine Clothes", "15 gp"])
    
# if Background == "Soldier":
#     Specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
#     Background = "Soldier " + Specialty
#     SkillProficiencies.extend(["Athletics", "Intimidation"])
#     ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
#     Equipment.extend(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    
# if Background == "Stojanow Prisoner":
#     SkillProficiencies.extend(["Deception", "Perception"])
#     ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])
#     Equipment.extend(["Small Knife", "Set of Common Clothes", "Trinket from Home", "10 gp"])
    
# if Background == "Ticklebelly Nomad":
#     SkillProficiencies.extend(["Animal Handling", "Nature"])
#     ToolProficiencies.extend(["Herbalism Kit"])
#     Equipment.extend(["Herbalism Kit", "Small Article of Jewelry Distinct to Your Tribe", "Hunting Trap", "Set of Common Clothes", "5 gp"])
    
# if Background == "Trade Sheriff":
#     SkillProficiencies.extend(["Investigation", "Persuasion"])
#     ToolProficiencies.extend(["Thieves' Tools"])
#     Equipment.extend(["Thieves' Kit", "Gray Cloak", "Sherrif's Insignia", "Set of Fine Clothes", "17 gp"])
    
# if Background == "Urban Bounty Hunter":
#     SkillProficiencies.extend(random.sample(["Deception", "Insight", "Persuasion", "Stealth"], 2))
#     ToolProficiencies.extend(random.sample([random.choice(GamingSets), random.choice(MusicalInstruments), "Theives' Tools"],2))
#     Equipment.extend([random.choice(["Set of Common Clothes", "Set of Traveler's Clothes", "Set of Fine Clothes"]), "20 gp"])
    
# if Background == "Urchin":
#     SkillProficiencies.extend(["Sleight of Hand", "Stealth"])
#     ToolProficiencies.extend(["Disguise Kit", "Thieve's Tools"])
#     Equipment.extend(["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes", "10 gp"])
    
# if Background == "Uthgardt Tribe Member":
#     SkillProficiencies.extend(["Athletics", "Survival"])
#     ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), random.choice(MusicalInstruments)])])
#     Equipment.extend(["Hunting Trap", random.choice(["Totemic Token", "Set of Tattoos"]) + " Marking Your Loyalty to Uthgar", "Set of Traveler's Clothes", "10 gp"])
    
# if Background == "Vizier":
#     SkillProficiencies.extend(["History", "Religion"])
#     VizierArtisanTool = random.choice(ArtisanTools)
#     VizierMusicalInstrument = random.choice(MusicalInstruments)
#     ToolProficiencies.extend([VizierArtisanTool, VizierMusicalInstrument])
#     Equipment.extend([random.choice([VizierArtisanTool, VizierMusicalInstrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    
# if Background == "Waterdhavian Noble":
#     SkillProficiencies.extend(["History", "Persuasion"])
#     ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
#     Equipment.extend(["Set of Fine Clothes", random.choice(["Signet Ring", "Brooch"]), "Scroll of Pedigree", "Skin of Fine " + random.choice(["Zzar", "Wine"]), "25 gp"])
