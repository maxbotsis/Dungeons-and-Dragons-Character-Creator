
import random

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

Skills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
ArtisanTools = ["Alchemist's Supplies", "Brewer's Supplies", "Calligrapher's Supplies", "Carpenter's Tools", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools", "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Tools", "Potter's Tools", "Smith's Tools", "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"]
GamingSets = ["Dice Set", "Dragonchess Set", "Playing Card Set", "Three-Dragon Ante Set"]
MusicalInstruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute", "Shawm", "Viol"]
MartialWeapons = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip", "Blowgun", "Hand Crossbow", "Heavy Crossbow", "Longbow", "Net"]
MartialMelee = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "War Pick", "Warhammer", "Whip"]
SimpleWeapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear", "Light Crossbow", "Dart", "Shortbow", "Sling"]
SimpleMelee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]



class Acolyte:  
    def __init__(self):
        SkillProficiencies.append(["Insight", "Religion"])      
        Equipment.append(["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes", "15 gp"])        

class Anthropologist:  
    def __init__(self):    
        SkillProficiencies.append(["Insight", "Religion"])
        Equipment.append(["Leather-Bound Diary", "Bottle of Ink", "Ink Pen", "Set of Traveler's Clothes", "One Trinket of Special Significance", "10 gp"])
    
class Archaeologist:
    def __init__(self):
        SkillProficiencies.append(["History", "Survival"])
        ToolProficiencies.append([random.choice(["Cartographer's Tools", "Navigator's Tools"])])
        Equipment.append([random.choice(["Wooden Case Containing a Map to a Ruin", "Wooden Case Containing a Map to a Dungeon"]), "Bullseye Lantern", "Miner's Pick", "Set of Traveler's Clothes", "Shovel", "Two-Person Tent", "Trinket Recovered from a Dig Site", "25 gp"])

class BlackFistDoubleAgent:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Insight"])
        BlackFistDoubleAgentTool = random.choice([random.choice(GamingSets), random.choice(ArtisanTools)])
        ToolProficiencies.append(["Disguise Kit", BlackFistDoubleAgentTool])
        Equipment.append(["Disguise Kit", "Common Clothes", "Tears of Virulence Emblem", "Writ of Free Agency Signed by the Lord Regent", BlackFistDoubleAgentTool, "15 gp"])
    
class CaravanSpecialist:
    def __init__(self):
        SkillProficiencies.append(["Animal Handling", "Survival"])
        ToolProficiencies.append(["Land Vehicles"])
        Equipment.append(["Whip", "Tent", "Regional Map", "Traveling Clothes", "10 gp"])
    
class Charlatan:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Sleight of Hand"])
        ToolProficiencies.append(["Disguise Kit", "Forgery Kit"])
        Equipment.append(["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"]), "15 gp"])

class CityWatch:
    def __init__(self):
        subBackground = random.choice(["City Watch Patrol", "City Watch Investigator"])
        SkillProficiencies.append(["Insight"])
        if subBackground == "City Watch Patrol":
            SkillProficiencies.append(["Athletics"])
        if subBackground == "City Watch Investigator":
            SkillProficiencies.append(["Investigation"])
        Equipment.append(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    
class ClanCrafter:
    def __init__(self):
        SkillProficiencies.append(["History", "Insight"])
        ClanCrafterArtisanTools = random.choice(ArtisanTools)
        ToolProficiencies.append([ClanCrafterArtisanTools])
        Equipment.append([ClanCrafterArtisanTools, "Maker's Mark Chisel", "Traveler's Clothes", "Gem Worth 10 gp", "5 gp"])
    
class CloisteredScholar:
    def __init__(self):
        SkillProficiencies.append(["History", random.choice(["Arcana", "Nature", "Religion"])])
        Equipment.append(["Scholar's Robes of Your Cloister", "Writing Kit", "Borrowed Book on the Subject of Your Current Study", "10 gp"])
    
class CormanthorRefugee:
    def __init__(self):
        SkillProficiencies.append(["Nature", "Survival"])
        CormanthorRefugeeArtisanTools = random.choice(ArtisanTools) # Introducing a temporary variable so the same artisan's tools will be included in the Equipment and proficiencies
        ToolProficiencies.append([CormanthorRefugeeArtisanTools])
        Equipment.append(["Two-Person Tent", CormanthorRefugeeArtisanTools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    
class Courtier:
    def __init__(self):
        SkillProficiencies.append(["Insight", "Persuasion"])
        Equipment.append(["Set of Fine Clothes", "5 gp"])
    
class Criminal:
    def __init__(self):
        Specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
        Background = "Criminal " + random.choice(Specialty)
        SkillProficiencies.append(["Deception", "Stealth"])
        ToolProficiencies.append([random.choice(GamingSets), "Thieves' Tools"])
    
class DragonCasualty: # Tool proficiency is based on origin
    def __init__(self):
        Origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
        Background = "Dragon Casualty who used to be a " + Origin
        if Origin == "Dockworker/Fisherman":
            ToolProficiencies.append(["Water Vehicles"])
        if Origin == "Tradesperson/Merchant":
            ToolProficiencies.append([random.choice(ArtisanTools)])
        if Origin == "Black Fist Soldier":
            ToolProficiencies.append([random.choice([random.choice(ArtisanTools), "Land Vehicles"])])
        if Origin == "Adventurer":
            ToolProficiencies.append(["Land Vehicles"])
        if Origin == "Entertainer":
            ToolProficiencies.append([random.choice(MusicalInstruments)])
        if Origin == "Scholar/Healer":
            ToolProficiencies.append([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
        if Origin == "Criminal":
            ToolProficiencies.append([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
        if Origin == "Unskilled Labourer":
            ToolProficiencies.append([random.choice(GamingSets)])
        SkillProficiencies.append(["Intimidation", "Survival"])
        Equipment.append(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])

class EarthspurMiner:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Survival"])
        Equipment.append([random.choice(["Shovel", "Miner's Pick"]), "Block and Tackle", "Climber's Kit", "Set of Common Clothes", "5 gp"])
    
class Entertainer:
    def __init__(self):
        Routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
        Background = "Entertainer who is " + ", and ".join(Routine)
        SkillProficiencies.append(["Acrobatics", "Performance"])
        EntertainerMusicalInstrument = random.choice(MusicalInstruments)  # Introducing a temporary variable so the same instrument will be included in the Equipment and proficiencies
        ToolProficiencies.append(["Disguise Kit", EntertainerMusicalInstrument])
        Equipment.append([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
        if "a Gladiator" in Routine:
            GladiatorWeapon = random.choice(["Trident", "Net"])
            WeaponProficiencies.append([GladiatorWeapon])
            Equipment.append([GladiatorWeapon])
    
class FactionAgent:
    def __init__(self):
        Faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
        Background = "Faction Agent of " + Faction
        SkillProficiencies.append(["Insight"])
        if Faction == "The Emerald Enclave":
            SkillProficiencies.append(["Nature"])
        if Faction == "The Harpers":
            SkillProficiencies.append(["Investigation"])
        if Faction == "The Lord's Alliance":
            SkillProficiencies.append(["History"])
        if Faction == "The Order of the Gauntlet":
            SkillProficiencies.append(["Religion"])
        if Faction == "The Zhentarim":
            SkillProficiencies.append(["Deception"])
        Equipment.append([random.choice(["Badge of " + Faction, "Emblem of " + Faction]), "Set of Common Clothes", "15 gp"])
        if Faction == "The Harpers" or Faction == "The Zhentarim":
            Equipment.append(["Copy of a Code-Book from " + Faction])
        else: 
            Equipment.append(["Copy of a Seminal Text from " + Faction])
    
class FarTraveller:
    def __init__(self):
        Reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
        Origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
        Background = "Far Traveler " + Reason + " from " + Origin
        SkillProficiencies.append(["Insight", "Perception"])
        FarTravelerTool = random.choice([random.choice(MusicalInstruments), random.choice(GamingSets)])
        ToolProficiencies.append([FarTravelerTool])
        Equipment.append([FarTravelerTool, "Poorly Wrought Maps from " + Origin, "Small Piece of Jewelry Worth 10 gp from " + Origin, "5 gp"])
    
class FolkHero:
    def __init__(self):
        SkillProficiencies.append(["Animal Handling", "Survival"])
        FolkHeroTools = random.choice(ArtisanTools)
        ToolProficiencies.append([FolkHeroTools, "Land Vehicles"])
        Equipment.append([FolkHeroTools, "Shovel", "Iron Pot", "Set of Common Clothes", "10 gp"])
    
class GateUrchin:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Sleight of Hand"])
        GateUrchinMusicalInstrument = random.choice(MusicalInstruments)
        ToolProficiencies.append(["Thieves' Tools", GateUrchinMusicalInstrument])
        Equipment.append(["Battered Alms Box", GateUrchinMusicalInstrument, random.choice(["Cast-Off Military Jacket", "Cast-Off Cap", "Cast-Off Scarf"]), "Set of Common Clothes", "10 gp"])
    
class GuildArtisan:
    def __init__(self):
        SkillProficiencies.append(["Insight", "Persuasion"])
        GuildArtisanTools = random.choice(ArtisanTools)
        ToolProficiencies.append([GuildArtisanTools])
        Equipment.append([GuildArtisanTools, "Letter of Introduction from Your Guild", "15 gp"])
    
class Harborfolk:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Sleight of Hand"])
        HarborfolkGamingSet = random.choice(GamingSets)
        ToolProficiencies.append([HarborfolkGamingSet, "Water Vehicles"])
        Equipment.append([HarborfolkGamingSet, "Fishing Tackle", "Set of Common Clothes", "Rowboat", "5 gp"])
    
class HauntedOne:
    def __init__(self):
        SkillProficiencies.append(random.choice(["Arcana", "Investigation", "Religion", "Survival"]))
        Equipment.append(["Monster Hunter's Pack", "Gothic Trinket"])

class Hermit:
    def __init__(self):
        SkillProficiencies.append(["Medicine", "Religion"])
        ToolProficiencies.append(["Herbalism Kit"])
        Equipment.append(["Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit", "5 gp"])
    
class HillsfarMerchant:
    def __init__(self):
        SkillProficiencies.append(["Insight", "Persuasion"])
        ToolProficiencies.append(["Land Vehicles", "Water Vehicles"])
        Equipment.append(["Set of Clothes", "Signet Ring", "Letter of Introduction from Your Family's Trading House", "25 gp"])

class HillsfarSmuggler:
    def __init__(self):
        SkillProficiencies.append(["Perception", "Stealth"])
        ToolProficiencies.append(["Forgery Kit"])
        Equipment.append(["Forgery Kit", "Set of Common Clothes", "5 gp"])
    
class HouseAgent:
    def __init__(self):
        House = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
        Background = "House Agent of the " + House + " House"
        SkillProficiencies.append(["Investigation", "Persuasion"])
        if House == "Cannith":
            ToolProficiencies.append(["Alchemist's Supplies", "Tinker's Tools"])
        if House == "Deneith":
            ToolProficiencies.append([random.choice(GamingSets), "Land Vehicles"])
        if House == "Ghallanda":
            ToolProficiencies.append(["Brewer's Supplies", "Cook's Utensils"])
        if House == "Jorasco":
            ToolProficiencies.append(["Alchemist's Supplies", "Herbalism Kit"])
        if House == "Kundarak":
            ToolProficiencies.append(["Tinker's Tools", "Thieves' Tools"])
        if House == "Lyrandar":
            ToolProficiencies.append(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
        if House == "Medani":
            ToolProficiencies.append(["Thieves' Tools", "Disguise Kit"])
        if House == "Orien":
            ToolProficiencies.append(["Land Vehicles", random.choice(GamingSets)])
        if House == "Phiarlan":
            ToolProficiencies.append(["Disguise Kit", random.choice(MusicalInstruments)])
        if House == "Sivis":
            ToolProficiencies.append(["Calligrapher's Tools", "Forgery Kit"])
        if House == "Tharashk":
            ToolProficiencies.append(["Thieve's Tools", random.choice(GamingSets)])
        if House == "Thuranni":
            ToolProficiencies.append(["Poisoner's Kit", random.choice(GamingSets)])
        if House == "Vadalis":
            ToolProficiencies.append(["Land Vehicles", "Herbalism Kit"])
        Equipment.append(["Set of Fine Clothes", House + " Signet Ring", "ID Papers", "20 gp"])
    
class Inheritor:
    def __init__(self):
        SkillProficiencies.append(["Survival", random.choice(["Arcana", "History", "Religion"])])
        InheritorTool = random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])
        ToolProficiencies.append([InheritorTool])
        Equipment.append(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", InheritorTool, "15 gp"])
    
class Initiate:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Intimidation"])
        InitiateGamingSet = random.choice(GamingSets)
        ToolProficiencies.append([InitiateGamingSet, "Land Vehicles"])
        Equipment.append(["Simple Puzzle Box", "Scroll Containing the Teachings of the Gods", InitiateGamingSet, "Set of Common Clothes", "15 gp"])
    
class Inquisitor:
    def __init__(self):
        SkillProficiencies.append(["Investigation", "Religion"])
        ToolProficiencies.append([random.choice(ArtisanTools), "Thieves' Tools"])
        Equipment.append(["Holy Symbol", "Set of Traveler's Clothes", "15 gp"])
    
class IronRouteBandit:
    def __init__(self):
        SkillProficiencies.append(["Animal Handling", "Stealth"])
        ToolProficiencies.append([random.choice(GamingSets), "Land Vehicles"])
        Equipment.append(["Set of Dark Common Clothes", "Pack Saddle", "Burglar's Pack", "5 gp"])
    
class KnightOfTheOrder:
    def __init__(self):
        Order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
        Background = "Knight of the Order of " + Order
        SkillProficiencies.append(["Persuasion"])
        if Order == "the Unicorn":
            SkillProficiencies.append([random.choice(["Arcana", "Religion"])])
        if Order == "Myth Drannor":
            SkillProficiencies.append([random.choice(["Nature", "History"])])
        if Order == "the Silver Chalice":
            SkillProficiencies.append([random.choice(["History", "Religion"])])
        ToolProficiencies.append([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
        Equipment.append(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + Order, "10 gp"])
    
class MercenaryVeteran:
    def __init__(self):
        Company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
        Background = "Mercenary Veteran from " + Company
        SkillProficiencies.append(["Athletics", "Persuasion"])
        MercenaryVeteranGamingSet = random.choice(GamingSets)
        ToolProficiencies.append([MercenaryVeteranGamingSet, "Land Vehicles"])
        Equipment.append(["Uniform from " + Company, "Insignia of Your Rank from " + Company, MercenaryVeteranGamingSet, "10 gp"])
    
class MulmasterAristocrat:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Performance"])
        MulmasterAristocratArtisanTool = random.choice(ArtisanTools)
        MulmasterAristocratMusicalInstrument = random.choice(MusicalInstruments)
        ToolProficiencies.append([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument])
        Equipment.append([random.choice([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument]), "Set of Fine Clothes", "10 gp"])
    
class Noble:
    def __init__(self):
        SkillProficiencies.append(["History", "Persuasion"])
        ToolProficiencies.append([random.choice(GamingSets)])
        Equipment.append(["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 gp"])
    
class Outlander:
    def __init__(self):
        Origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
        Background = "Outlander " + Origin
        SkillProficiencies.append(["Athletics", "Survival"])
        ToolProficiencies.append([random.choice(MusicalInstruments)])
        Equipment.append(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
    
class PhlanInsurgent:
    def __init__(self):
        SkillProficiencies.append(["Stealth", "Survival"])
        ToolProficiencies.append([random.choice(ArtisanTools), "Land Vehicles"])
        Equipment.append(["Bag of 20 Caltrops", "Small Trinket from Your Home", "Healer's Kit", "Set of Dark Common Clothes", "5 gp"])

class PhlanRefugee:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Insight"])
        PhlanRefugeeTool = random.choice(ArtisanTools)
        ToolProficiencies.append([PhlanRefugeeTool])
        Equipment.append([PhlanRefugeeTool, "Token from Home", "Set of Traveler's Clothes", "15 gp"])
    
class Sage:
    def __init__(self):
        Specialty = random.choice(["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor", "Researcher", "Wizard's Apprentice", "Scribe"])
        Background = "Sage " + Specialty
        SkillProficiencies.append(["Arcana", "History"])
        Equipment.append(["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes", "10 gp"])
    
class Sailor:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Perception"])
        ToolProficiencies.append(["Navigator's Tools", "Water Vehicles"])
        Equipment.append(["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes", "10 gp"])
    
class SecretIdentity: # Has to be non human
    def __init__(self):
        SkillProficiencies.append(["Deception", "Stealth"])
        ToolProficiencies.append(["Disguise Kit", "Forgery Kit"])
        Equipment.append(["Disguise Kit", "Forgery Kit", "Set of Common Clothes", "5 gp"])
    
class ShadeFanatic:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Intimidation"])
        ToolProficiencies.append(["Forgery Kit"])
        Equipment.append(["Forgery Kit", "Transparent Cylinder of Shadow that has no Opening", "Signet Ring", "Set of Fine Clothes", "15 gp"])
    
class Soldier:
    def __init__(self):
        Specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
        Background = "Soldier " + Specialty
        SkillProficiencies.append(["Athletics", "Intimidation"])
        ToolProficiencies.append([random.choice(GamingSets), "Land Vehicles"])
        Equipment.append(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    
class StojanowPrisoner:
    def __init__(self):
        SkillProficiencies.append(["Deception", "Perception"])
        ToolProficiencies.append([random.choice(GamingSets), "Thieves' Tools"])
        Equipment.append(["Small Knife", "Set of Common Clothes", "Trinket from Home", "10 gp"])
    
class TicklebellyNomad:
    def __init__(self):
        SkillProficiencies.append(["Animal Handling", "Nature"])
        ToolProficiencies.append(["Herbalism Kit"])
        Equipment.append(["Herbalism Kit", "Small Article of Jewelry Distinct to Your Tribe", "Hunting Trap", "Set of Common Clothes", "5 gp"])
    
class TradeSheriff:
    def __init__(self):
        SkillProficiencies.append(["Investigation", "Persuasion"])
        ToolProficiencies.append(["Thieves' Tools"])
        Equipment.append(["Thieves' Kit", "Gray Cloak", "Sherrif's Insignia", "Set of Fine Clothes", "17 gp"])
    
class UrbanBountyHunter:
    def __init__(self):
        SkillProficiencies.append(random.sample(["Deception", "Insight", "Persuasion", "Stealth"], 2))
        ToolProficiencies.append(random.sample([random.choice(GamingSets), random.choice(MusicalInstruments), "Theives' Tools"],2))
        Equipment.append([random.choice(["Set of Common Clothes", "Set of Traveler's Clothes", "Set of Fine Clothes"]), "20 gp"])
    
class Urchin:
    def __init__(self):
        SkillProficiencies.append(["Sleight of Hand", "Stealth"])
        ToolProficiencies.append(["Disguise Kit", "Thieve's Tools"])
        Equipment.append(["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes", "10 gp"])
    
class UthgardtTribeMember:
    def __init__(self):
        SkillProficiencies.append(["Athletics", "Survival"])
        ToolProficiencies.append([random.choice([random.choice(ArtisanTools), random.choice(MusicalInstruments)])])
        Equipment.append(["Hunting Trap", random.choice(["Totemic Token", "Set of Tattoos"]) + " Marking Your Loyalty to Uthgar", "Set of Traveler's Clothes", "10 gp"])
    
class Vizier:
    def __init__(self):
        SkillProficiencies.append(["History", "Religion"])
        VizierArtisanTool = random.choice(ArtisanTools)
        VizierMusicalInstrument = random.choice(MusicalInstruments)
        ToolProficiencies.append([VizierArtisanTool, VizierMusicalInstrument])
        Equipment.append([random.choice([VizierArtisanTool, VizierMusicalInstrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    
class WaterdhavianNoble:
    def __init__(self):
        SkillProficiencies.append(["History", "Persuasion"])
        ToolProficiencies.append([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
        Equipment.append(["Set of Fine Clothes", random.choice(["Signet Ring", "Brooch"]), "Scroll of Pedigree", "Skin of Fine " + random.choice(["Zzar", "Wine"]), "25 gp"])

class Main:
    BackgroundList = [Acolyte, Anthropologist, Archaeologist, BlackFistDoubleAgent, CaravanSpecialist, Charlatan, 
    CityWatch, ClanCrafter, CloisteredScholar, Courtier, Criminal, DragonCasualty, EarthspurMiner, 
    Entertainer, FactionAgent, FarTraveller, FolkHero, GateUrchin, GuildArtisan, Harborfolk, HauntedOne, 
    Hermit, HillsfarMerchant, HillsfarSmuggler, HouseAgent, Inheritor, Initiate, Inquisitor, IronRouteBandit, 
    KnightOfTheOrder, MercenaryVeteran, MulmasterAristocrat, Noble, Outlander, PhlanInsurgent, PhlanRefugee, 
    Sage, Sailor, SecretIdentity, ShadeFanatic, Soldier, StojanowPrisoner, TicklebellyNomad, TradeSheriff, 
    UrbanBountyHunter, Urchin, UthgardtTribeMember, Vizier, WaterdhavianNoble]

    chosenBackground = random.choice(BackgroundList)
    