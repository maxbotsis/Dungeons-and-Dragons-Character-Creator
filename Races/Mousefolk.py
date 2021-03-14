


 
if Race == "Mousefolk": # Extra Race I found https://www.dndbeyond.com/races/61879-mousefolk
    DEX = StatIncrease(DEX, 2)
    CHA = StatIncrease(CHA, 1)
    Age = Normal(10,45)
    SizeMod = Normal(2,8)
    Height = 2 * 12 + 11 + SizeMod
    Weight = 40 + SizeMod
    Eyes = ["Pink", "Black"]
    Eyes = random.choice(Eyes)
    Skin = "Pink"
    Hair = ["Beige Fur", "Black Fur", "Chocolate Fur", "Coffee Fur", "Cream Fur", "Ivory Fur", "Lilac Fur", "Silver Fur", "White Fur", "Tan Fur"]
    Hair = random.choice(Hair)
    Speed = 25
    Traits.extend(["Darkvision (60ft)", "Light Sleeper", "Mouse's Agility", "Mousefolk Senses", "Mouse's Survival"]) # I will be ediditing some of these for my campaign as they aren't well balanced
    