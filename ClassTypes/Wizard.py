
if Class == "Wizard":
    if Level >= 2:
        Subclass = ["Artificier", "Bladesinger", "Lore Mastery", "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Invention", "School of Necromancy", "School of Transmutation", "Technomancy", "Theurgy", "War Magic"]
        Subclass = random.choice(Subclass)
    HP = HP + HitPoints(6)
    WeaponProficiencies.extend(["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"])
    SavingThrowProficiencies.extend(["INT", "WIS"])
    SkillProficiencies.extend(random.sample(["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2))
    Equipment.extend([random.choice(["Quarterstaff", "Dagger"]), random.choice(["Component Pouch", "Arcane Focus"]), random.choice(["Scholar's Pack", "Explorer's Pack"]), "Spellbook"])
