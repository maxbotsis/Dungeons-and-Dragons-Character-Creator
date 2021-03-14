import Main
import random



class Acolyte():  
    def __init__(self):
        Main.SkillProficiencies.extend(["Insight", "Religion"])      
        Main.Equipment.extend(["Holy Symbol", random.choice(["Prayer Book", "Prayer Wheel"]), "5 Sticks of Incense", "Vestments", "Common Clothes", "15 gp"])        

class Anthropologist():  
    def __init__(self):    
        Main.SkillProficiencies.extend(["Insight", "Religion"])
        Main.Equipment.extend(["Leather-Bound Diary", "Bottle of Ink", "Ink Pen", "Set of Traveler's Clothes", "One Trinket of Special Significance", "10 gp"])
    
class Archaeologist:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", "Survival"])
        Main.ToolProficiencies.extend([random.choice(["Cartographer's Tools", "Navigator's Tools"])])
        Main.Equipment.extend([random.choice(["Wooden Case Containing a Map to a Ruin", "Wooden Case Containing a Map to a Dungeon"]), "Bullseye Lantern", "Miner's Pick", "Set of Traveler's Clothes", "Shovel", "Two-Person Tent", "Trinket Recovered from a Dig Site", "25 gp"])

class BlackFistDoubleAgent:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Insight"])
        BlackFistDoubleAgentTool = random.choice([random.choice(GamingSets), random.choice(ArtisanTools)])
        Main.ToolProficiencies.extend(["Disguise Kit", BlackFistDoubleAgentTool])
        Main.Equipment.extend(["Disguise Kit", "Common Clothes", "Tears of Virulence Emblem", "Writ of Free Agency Signed by the Lord Regent", BlackFistDoubleAgentTool, "15 gp"])
    
class CaravanSpecialist:
    def __init__(self):
        Main.SkillProficiencies.extend(["Animal Handling", "Survival"])
        Main.ToolProficiencies.extend(["Land Vehicles"])
        Main.Equipment.extend(["Whip", "Tent", "Regional Map", "Traveling Clothes", "10 gp"])
    
class Charlatan:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Sleight of Hand"])
        Main.ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
        Main.Equipment.extend(["Fine Clothes", "Disguise Kit", random.choice(["Ten Stoppered Bottles Filled with Coloured Liquid", "Set of Weighted Dice", "Deck of Marked Cards", "Signet Ring of an Imaginary Duke"]), "15 gp"])

class CityWatch:
    def __init__(self):
    subBackground = random.choice(["City Watch Patrol", "City Watch Investigator"])
    Main.SkillProficiencies.extend(["Insight"])
    if subBackground == "City Watch Patrol":
        Main.SkillProficiencies.extend(["Athletics"])
    if subBackground == "City Watch Investigator":
        Main.SkillProficiencies.extend(["Investigation"])
    Main.Equipment.extend(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    
class ClanCrafter:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", "Insight"])
        ClanCrafterArtisanTools = random.choice(ArtisanTools)
        Main.ToolProficiencies.extend([ClanCrafterArtisanTools])
        Main.Equipment.extend([ClanCrafterArtisanTools, "Maker's Mark Chisel", "Traveler's Clothes", "Gem Worth 10 gp", "5 gp"])
    
class CloisteredScholar:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", random.choice(["Arcana", "Nature", "Religion"])])
        Main.Equipment.extend(["Scholar's Robes of Your Cloister", "Writing Kit", "Borrowed Book on the Subject of Your Current Study", "10 gp"])
    
class CormanthorRefugee:
    def __init__(self):
        Main.SkillProficiencies.extend(["Nature", "Survival"])
        CormanthorRefugeeArtisanTools = random.choice(ArtisanTools) # Introducing a temporary variable so the same artisan's tools will be included in the Main.Equipment and proficiencies
        Main.ToolProficiencies.extend([CormanthorRefugeeArtisanTools])
        Main.Equipment.extend(["Two-Person Tent", CormanthorRefugeeArtisanTools, "Holy Symbol", "Traveler's Clothes", "5 gp"])
    
class Courtier:
    def __init__(self):
        Main.SkillProficiencies.extend(["Insight", "Persuasion"])
        Main.Equipment.extend(["Set of Fine Clothes", "5 gp"])
    
class Criminal:
    def __init__(self):
        Specialty = ["Blackmailer", "Burglar", "Enforcer", "Fence", "Highway Robber", "Hired Killer", "Pickpocket", "Smuggler", "Spy"]
        Background = "Criminal " + random.choice(Specialty)
        Main.SkillProficiencies.extend(["Deception", "Stealth"])
        Main.ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])
    
class DragonCasualty: # Tool proficiency is based on origin
    def __init__(self):
        Origin = random.choice(["Dockworker/Fisherman", "Tradesperson/Merchant", "Black Fist Soldier", "Adventurer", "Entertainer", "Scholar/Healer", "Criminal", "Unskilled Labourer"])
        Background = "Dragon Casualty who used to be a " + Origin
        if Origin == "Dockworker/Fisherman":
            Main.ToolProficiencies.extend(["Water Vehicles"])
        if Origin == "Tradesperson/Merchant":
            Main.ToolProficiencies.extend([random.choice(ArtisanTools)])
        if Origin == "Black Fist Soldier":
            Main.ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), "Land Vehicles"])])
        if Origin == "Adventurer":
            Main.ToolProficiencies.extend(["Land Vehicles"])
        if Origin == "Entertainer":
            Main.ToolProficiencies.extend([random.choice(MusicalInstruments)])
        if Origin == "Scholar/Healer":
            Main.ToolProficiencies.extend([random.choice(["Alchemist's Supplies", "Herbalism Kit"])])
        if Origin == "Criminal":
            Main.ToolProficiencies.extend([random.choice(["Thieves' Tools", "Forgery Kit", "Disguise Kit"])])
        if Origin == "Unskilled Labourer":
            Main.ToolProficiencies.extend([random.choice(GamingSets)])
        Main.SkillProficiencies.extend(["Intimidation", "Survival"])
        Main.Equipment.extend(["Dagger", "Tattered Rags", "Loaf of Moldy Bread", "Small Cast-Off Scale Belonging to Vorgansharax - The Maimed Virulence", "5 gp"])

class EarthspurMiner:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Survival"])
        Main.Equipment.extend([random.choice(["Shovel", "Miner's Pick"]), "Block and Tackle", "Climber's Kit", "Set of Common Clothes", "5 gp"])
    
class Entertainer:
    def __init__(self):
    Routine = random.sample(["an Actor", "a Dancer", "a Fire-Eater", "a Gladiator", "a Jester", "a Juggler", "an Instrumentalist", "a Poet", "a Singer", "a Storyteller", "a Tumbler"], 3) # The handbook says up to 3 routines, going with 3 to spice things up. Gladiator is also included in here for fun
    Background = "Entertainer who is " + ", and ".join(Routine)
    Main.SkillProficiencies.extend(["Acrobatics", "Performance"])
    EntertainerMusicalInstrument = random.choice(MusicalInstruments)  # Introducing a temporary variable so the same instrument will be included in the Main.Equipment and proficiencies
    Main.ToolProficiencies.extend(["Disguise Kit", EntertainerMusicalInstrument])
    Main.Equipment.extend([EntertainerMusicalInstrument, random.choice(["Love Letter from an Admirer", "Lock of Hair from an Admirer", "Trinket from an Admirer"]), "Costume", "15 gp"])
    if "a Gladiator" in Routine:
        GladiatorWeapon = random.choice(["Trident", "Net"])
        WeaponProficiencies.extend([GladiatorWeapon])
        Main.Equipment.extend([GladiatorWeapon])
    
class FactionAgent:
    def __init__(self):
        Faction = random.choice(["The Emerald Enclave", "The Harpers", "The Lord's Alliance", "The Order of the Gauntlet", "The Zhentarim"])
        Background = "Faction Agent of " + Faction
        Main.SkillProficiencies.extend(["Insight"])
        if Faction == "The Emerald Enclave":
            Main.SkillProficiencies.extend(["Nature"])
        if Faction == "The Harpers":
            Main.SkillProficiencies.extend(["Investigation"])
        if Faction == "The Lord's Alliance":
            Main.SkillProficiencies.extend(["History"])
        if Faction == "The Order of the Gauntlet":
            Main.SkillProficiencies.extend(["Religion"])
        if Faction == "The Zhentarim":
            Main.SkillProficiencies.extend(["Deception"])
        Main.Equipment.extend([random.choice(["Badge of " + Faction, "Emblem of " + Faction]), "Set of Common Clothes", "15 gp"])
        if Faction == "The Harpers" or Faction == "The Zhentarim":
            Main.Equipment.extend(["Copy of a Code-Book from " + Faction])
        else: 
            Main.Equipment.extend(["Copy of a Seminal Text from " + Faction])
    
class FarTraveler:
    def __init__(self):
        Reason = random.choice(["Emissary", "Exile", "Fugitive", "Pilgrim", "Sightseer", "Wanderer"])
        Origin = random.choice(["Evermeet", "Halruaa", "Kara-Tur", "Mulhorand", "Sossal", "Zakhara", "The Underdark"])
        Background = "Far Traveler " + Reason + " from " + Origin
        Main.SkillProficiencies.extend(["Insight", "Perception"])
        FarTravelerTool = random.choice([random.choice(MusicalInstruments), random.choice(GamingSets)])
        Main.ToolProficiencies.extend([FarTravelerTool])
        Main.Equipment.extend([FarTravelerTool, "Poorly Wrought Maps from " + Origin, "Small Piece of Jewelry Worth 10 gp from " + Origin, "5 gp"])
    
class FolkHero:
    def __init__(self):
        Main.SkillProficiencies.extend(["Animal Handling", "Survival"])
        FolkHeroTools = random.choice(ArtisanTools)
        Main.ToolProficiencies.extend([FolkHeroTools, "Land Vehicles"])
        Main.Equipment.extend([FolkHeroTools, "Shovel", "Iron Pot", "Set of Common Clothes", "10 gp"])
    
class GateUrchin:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Sleight of Hand"])
        GateUrchinMusicalInstrument = random.choice(MusicalInstruments)
        Main.ToolProficiencies.extend(["Thieves' Tools", GateUrchinMusicalInstrument])
        Main.Equipment.extend(["Battered Alms Box", GateUrchinMusicalInstrument, random.choice(["Cast-Off Military Jacket", "Cast-Off Cap", "Cast-Off Scarf"]), "Set of Common Clothes", "10 gp"])
    
class GuildArtisan:
    def __init__(self):
        Main.SkillProficiencies.extend(["Insight", "Persuasion"])
        GuildArtisanTools = random.choice(ArtisanTools)
        Main.ToolProficiencies.extend([GuildArtisanTools])
        Main.Equipment.extend([GuildArtisanTools, "Letter of Introduction from Your Guild", "15 gp"])
    
class Harborfolk:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Sleight of Hand"])
        HarborfolkGamingSet = random.choice(GamingSets)
        Main.ToolProficiencies.extend([HarborfolkGamingSet, "Water Vehicles"])
        Main.Equipment.extend([HarborfolkGamingSet, "Fishing Tackle", "Set of Common Clothes", "Rowboat", "5 gp"])
    
class HauntedOne:
    def __init__(self):
        Main.SkillProficiencies.extend(random.choice(["Arcana", "Investigation", "Religion", "Survival"]))
        Main.Equipment.extend(["Monster Hunter's Pack", "Gothic Trinket"])

class Hermit:
    def __init__(self):
        Main.SkillProficiencies.extend(["Medicine", "Religion"])
        Main.ToolProficiencies.extend(["Herbalism Kit"])
        Main.Equipment.extend(["Scroll Case Stuffed Full of Notes from Your " + random.choice(["Prayers", "Studies"]), "Winter Blanket", "Set of Common Clothes", "Herbalism Kit", "5 gp"])
    
class HillsfarMerchant:
    def __init__(self):
        Main.SkillProficiencies.extend(["Insight", "Persuasion"])
        Main.ToolProficiencies.extend(["Land Vehicles", "Water Vehicles"])
        Main.Equipment.extend(["Set of Clothes", "Signet Ring", "Letter of Introduction from Your Family's Trading House", "25 gp"])

class HillsfarSmuggler:
    def __init__(self):
        Main.SkillProficiencies.extend(["Perception", "Stealth"])
        Main.ToolProficiencies.extend(["Forgery Kit"])
        Main.Equipment.extend(["Forgery Kit", "Set of Common Clothes", "5 gp"])
    
class HouseAgent:
    def __init__(self):
        House = random.choice(["Cannith", "Deneith", "Ghallanda", "Jorasco", "Kundarak", "Lyrandar", "Medani", "Orien", "Phiarlan", "Sivis", "Tharashk", "Thuranni", "Vadalis"])
        Background = "House Agent of the " + House + " House"
        Main.SkillProficiencies.extend(["Investigation", "Persuasion"])
        if House == "Cannith":
            Main.ToolProficiencies.extend(["Alchemist's Supplies", "Tinker's Tools"])
        if House == "Deneith":
            Main.ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
        if House == "Ghallanda":
            Main.ToolProficiencies.extend(["Brewer's Supplies", "Cook's Utensils"])
        if House == "Jorasco":
            Main.ToolProficiencies.extend(["Alchemist's Supplies", "Herbalism Kit"])
        if House == "Kundarak":
            Main.ToolProficiencies.extend(["Tinker's Tools", "Thieves' Tools"])
        if House == "Lyrandar":
            Main.ToolProficiencies.extend(["Sea Vehicles", "Air Vehicles", "Navigator's Tools"])
        if House == "Medani":
            Main.ToolProficiencies.extend(["Thieves' Tools", "Disguise Kit"])
        if House == "Orien":
            Main.ToolProficiencies.extend(["Land Vehicles", random.choice(GamingSets)])
        if House == "Phiarlan":
            Main.ToolProficiencies.extend(["Disguise Kit", random.choice(MusicalInstruments)])
        if House == "Sivis":
            Main.ToolProficiencies.extend(["Calligrapher's Tools", "Forgery Kit"])
        if House == "Tharashk":
            Main.ToolProficiencies.extend(["Thieve's Tools", random.choice(GamingSets)])
        if House == "Thuranni":
            Main.ToolProficiencies.extend(["Poisoner's Kit", random.choice(GamingSets)])
        if House == "Vadalis":
            Main.ToolProficiencies.extend(["Land Vehicles", "Herbalism Kit"])
        Main.Equipment.extend(["Set of Fine Clothes", House + " Signet Ring", "ID Papers", "20 gp"])
    
class Inheritor:
    def __init__(self):
        Main.SkillProficiencies.extend(["Survival", random.choice(["Arcana", "History", "Religion"])])
        InheritorTool = random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])
        Main.ToolProficiencies.extend([InheritorTool])
        Main.Equipment.extend(["Your Inheritance: " + random.choice([random.choice(["A Map", "A Letter", "A Journal"]), "A Trinket", "An Article of Clothing", "A Piece of Jewelry", "An Arcane " + random.choice(["Book", "Formulary"]), "A Written " + random.choice(["Story", "Song", "Poem", "Secret"]), "A Tattoo"]), "Set of Traveler's Clothes", InheritorTool, "15 gp"])
    
class Initiate:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Intimidation"])
        InitiateGamingSet = random.choice(GamingSets)
        Main.ToolProficiencies.extend([InitiateGamingSet, "Land Vehicles"])
        Main.Equipment.extend(["Simple Puzzle Box", "Scroll Containing the Teachings of the Gods", InitiateGamingSet, "Set of Common Clothes", "15 gp"])
    
class Inquisitor:
    def __init__(self):
        Main.SkillProficiencies.extend(["Investigation", "Religion"])
        Main.ToolProficiencies.extend([random.choice(ArtisanTools), "Thieves' Tools"])
        Main.Equipment.extend(["Holy Symbol", "Set of Traveler's Clothes", "15 gp"])
    
class IronRouteBandit:
    def __init__(self):
        Main.SkillProficiencies.extend(["Animal Handling", "Stealth"])
        Main.ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
        Main.Equipment.extend(["Set of Dark Common Clothes", "Pack Saddle", "Burglar's Pack", "5 gp"])
    
class KnightOfTheOrder:
    def __init__(self):
        Order = random.choice(["the Unicorn", "Myth Drannor", "the Silver Chalice"])
        Background = "Knight of the Order of " + Order
        Main.SkillProficiencies.extend(["Persuasion"])
        if Order == "the Unicorn":
            Main.SkillProficiencies.extend([random.choice(["Arcana", "Religion"])])
        if Order == "Myth Drannor":
            Main.SkillProficiencies.extend([random.choice(["Nature", "History"])])
        if Order == "the Silver Chalice":
            Main.SkillProficiencies.extend([random.choice(["History", "Religion"])])
        Main.ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
        Main.Equipment.extend(["Set of Traveler's Clothes", random.choice(["Signet", "Banner", "Seal"]) + " Representing Your Rank in the Order of " + Order, "10 gp"])
    
class MercenaryVeteran:
    def __init__(self):
        Company = random.choice(["The Chill", "Silent Rain", "The Bloodaxes"])
        Background = "Mercenary Veteran from " + Company
        Main.SkillProficiencies.extend(["Athletics", "Persuasion"])
        MercenaryVeteranGamingSet = random.choice(GamingSets)
        Main.ToolProficiencies.extend([MercenaryVeteranGamingSet, "Land Vehicles"])
        Main.Equipment.extend(["Uniform from " + Company, "Insignia of Your Rank from " + Company, MercenaryVeteranGamingSet, "10 gp"])
    
class MulmasterAristocrat:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Performance"])
        MulmasterAristocratArtisanTool = random.choice(ArtisanTools)
        MulmasterAristocratMusicalInstrument = random.choice(MusicalInstruments)
        Main.ToolProficiencies.extend([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument])
        Main.Equipment.extend([random.choice([MulmasterAristocratArtisanTool, MulmasterAristocratMusicalInstrument]), "Set of Fine Clothes", "10 gp"])
    
class Noble:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", "Persuasion"])
        Main.ToolProficiencies.extend([random.choice(GamingSets)])
        Main.Equipment.extend(["Set of Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 gp"])
    
class Outlander:
    def __init__(self):
        Origin = random.choice(["Forester", "Trapper", "Homesteader", "Guide", "Exile", "Outcast", "Bounty Hunter", "Pilgrim", "Tribal Nomad", "Hunter-Gatherer", "Tribal Marauder"])
        Background = "Outlander " + Origin
        Main.SkillProficiencies.extend(["Athletics", "Survival"])
        Main.ToolProficiencies.extend([random.choice(MusicalInstruments)])
        Main.Equipment.extend(["Staff", "Hunting Trap", "Trophy from an Animal You Killed", "Set of Traveler's Clothes", "10 gp"])
    
class PhlanInsurgent:
    def __init__(self):
        Main.SkillProficiencies.extend(["Stealth", "Survival"])
        Main.ToolProficiencies.extend([random.choice(ArtisanTools), "Land Vehicles"])
        Main.Equipment.extend(["Bag of 20 Caltrops", "Small Trinket from Your Home", "Healer's Kit", "Set of Dark Common Clothes", "5 gp"])

class PhlanRefugee:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Insight"])
        PhlanRefugeeTool = random.choice(ArtisanTools)
        Main.ToolProficiencies.extend([PhlanRefugeeTool])
        Main.Equipment.extend([PhlanRefugeeTool, "Token from Home", "Set of Traveler's Clothes", "15 gp"])
    
class Sage:
    def __init__(self):
        Specialty = random.choice(["Alchemist", "Astronomer", "Discredited Academic", "Librarian", "Professor", "Researcher", "Wizard's Apprentice", "Scribe"])
        Background = "Sage " + Specialty
        Main.SkillProficiencies.extend(["Arcana", "History"])
        Main.Equipment.extend(["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Dead Colleague Posing a Question You Cannot yet Answer", "Set of Common Clothes", "10 gp"])
    
class Sailor:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Perception"])
        Main.ToolProficiencies.extend(["Navigator's Tools", "Water Vehicles"])
        Main.Equipment.extend(["Belaying Pin (Club)", "50 ft of Silk Rope", "Lucky Charm (Trinket)", "Set of Common Clothes", "10 gp"])
    
class SecretIdentity: # Has to be non human
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Stealth"])
        Main.ToolProficiencies.extend(["Disguise Kit", "Forgery Kit"])
        Main.Equipment.extend(["Disguise Kit", "Forgery Kit", "Set of Common Clothes", "5 gp"])
    
class ShadeFanatic:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Intimidation"])
        Main.ToolProficiencies.extend(["Forgery Kit"])
        Main.Equipment.extend(["Forgery Kit", "Transparent Cylinder of Shadow that has no Opening", "Signet Ring", "Set of Fine Clothes", "15 gp"])
    
class Soldier:
    def __init__(self):
        Specialty = random.choice(["Officer", "Scout", "Infantry", "Cavalry", "Healer", "Quartermaster", "Standard Bearer", "Support Staff"])
        Background = "Soldier " + Specialty
        Main.SkillProficiencies.extend(["Athletics", "Intimidation"])
        Main.ToolProficiencies.extend([random.choice(GamingSets), "Land Vehicles"])
        Main.Equipment.extend(["Insignia of Rank", "Trophy Taken from a Fallen Enemy", random.choice(["Bond Dice Set", "Playing Card Set"]), "Set of Common Clothes", "10 gp"])
    
class StojanowPrisoner:
    def __init__(self):
        Main.SkillProficiencies.extend(["Deception", "Perception"])
        Main.ToolProficiencies.extend([random.choice(GamingSets), "Thieves' Tools"])
        Main.Equipment.extend(["Small Knife", "Set of Common Clothes", "Trinket from Home", "10 gp"])
    
class TicklebellyNomad:
    def __init__(self):
        Main.SkillProficiencies.extend(["Animal Handling", "Nature"])
        Main.ToolProficiencies.extend(["Herbalism Kit"])
        Main.Equipment.extend(["Herbalism Kit", "Small Article of Jewelry Distinct to Your Tribe", "Hunting Trap", "Set of Common Clothes", "5 gp"])
    
class TradeSheriff:
    def __init__(self):
        Main.SkillProficiencies.extend(["Investigation", "Persuasion"])
        Main.ToolProficiencies.extend(["Thieves' Tools"])
        Main.Equipment.extend(["Thieves' Kit", "Gray Cloak", "Sherrif's Insignia", "Set of Fine Clothes", "17 gp"])
    
class UrbanBountyHunter:
    def __init__(self):
        Main.SkillProficiencies.extend(random.sample(["Deception", "Insight", "Persuasion", "Stealth"], 2))
        Main.ToolProficiencies.extend(random.sample([random.choice(GamingSets), random.choice(MusicalInstruments), "Theives' Tools"],2))
        Main.Equipment.extend([random.choice(["Set of Common Clothes", "Set of Traveler's Clothes", "Set of Fine Clothes"]), "20 gp"])
    
class Urchin:
    def __init__(self):
        Main.SkillProficiencies.extend(["Sleight of Hand", "Stealth"])
        Main.ToolProficiencies.extend(["Disguise Kit", "Thieve's Tools"])
        Main.Equipment.extend(["Small Knife", "Map of Your Home City", "Pet Mouse", "Token to Remember Your Parents", "Set of Common Clothes", "10 gp"])
    
class UthgardtTribeMember:
    def __init__(self):
        Main.SkillProficiencies.extend(["Athletics", "Survival"])
        Main.ToolProficiencies.extend([random.choice([random.choice(ArtisanTools), random.choice(MusicalInstruments)])])
        Main.Equipment.extend(["Hunting Trap", random.choice(["Totemic Token", "Set of Tattoos"]) + " Marking Your Loyalty to Uthgar", "Set of Traveler's Clothes", "10 gp"])
    
class Vizier:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", "Religion"])
        VizierArtisanTool = random.choice(ArtisanTools)
        VizierMusicalInstrument = random.choice(MusicalInstruments)
        Main.ToolProficiencies.extend([VizierArtisanTool, VizierMusicalInstrument])
        Main.Equipment.extend([random.choice([VizierArtisanTool, VizierMusicalInstrument]), "Scroll of Your God's Teachings", "Vizier's Cartouche", "Set of Fine Clothes", "25 gp"])
    
class WaterdhavianNoble:
    def __init__(self):
        Main.SkillProficiencies.extend(["History", "Persuasion"])
        Main.ToolProficiencies.extend([random.choice([random.choice(GamingSets), random.choice(MusicalInstruments)])])
        Main.Equipment.extend(["Set of Fine Clothes", random.choice(["Signet Ring", "Brooch"]), "Scroll of Pedigree", "Skin of Fine " + random.choice(["Zzar", "Wine"]), "25 gp"])
