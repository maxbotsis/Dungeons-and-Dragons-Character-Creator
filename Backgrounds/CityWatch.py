
if Background == "City Watch":
    Background = random.choice(["City Watch Patrol", "City Watch Investigator"])
    SkillProficiencies.extend(["Insight"])
    if Background == "City Watch Patrol":
        SkillProficiencies.extend(["Athletics"])
    if Background == "City Watch Investigator":
        SkillProficiencies.extend(["Investigation"])
    Equipment.extend(["Uniform in the Style of Your Unit and Indicative of Your Rank", "Horn with which to Summon Help", "Set of Manacles", "10 gp"])
    