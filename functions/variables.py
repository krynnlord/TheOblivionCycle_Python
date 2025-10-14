from functions.classes import *

#########################################
# Spells ################################
#########################################
# Circle 1
heal = spell("Heal", "Heals for a small amount", 3, 1, 15, 1, 1)
cure = spell("Cure", "Heals for a small amount", 0, 0, 15, 1, 2)
create_food = spell("Create Food", "Heals for a small amount", 0, 0, 15, 1, 3)
magic_missle = spell("Magic Missle", "Heals for a small amount", 0, 0, 15, 1, 4)

# Circle 2
greater_heal = spell("Greater Heal", "Heals for a small amount", 0, 0, 15, 2, 5)
barrier = spell("Barrier", "Creates a protective barrier around user", 0, 0, 1, 2, 6)
escape = spell("Escape", "Heals for a small amount", 0, 0, 15, 2, 7)
fireball = spell("Fireball","Sends a hurl of fire at opponent.", 2, 1, 25, 2, 8)

# Circle 3
regeneration = spell("Regeneration", "Heals for a small amount", 0, 0, 15, 3, 9)
holy_ground = spell("Holy Ground", "Heals for a small amount", 0, 0, 15, 3, 10)
double = spell("Double", "Heals for a small amount", 0, 0, 15, 3, 11)
immolation = spell("Immolation", "Heals for a small amount", 0, 0, 15, 3, 12)

hero_spells = [heal, cure, create_food, magic_missle, greater_heal, barrier, escape, fireball, regeneration, holy_ground, double, immolation]

#########################################
# Weapons ###############################
#########################################
# No Weapon
hands = weapon(1, "Hands", "blunt", 0, 1, "Your Hands")

# Slashing
dagger = weapon(2, "Dagger", "slashing", 100, 5, "Small blade")
short_sword = weapon(3, "Short Sword", "slashing", 200, 8, "A basic short sword")
long_sword = weapon(4, "Long Sword", "slashing", 400, 12, "A sturdy long sword")
greatsword = weapon(5, "Greatsword", "slashing", 800, 18, "A massive two-handed sword")

# Blunt
club = weapon(6, "Club", "blunt", 50, 4, "A simple wooden club")
mace = weapon(7, "Mace", "blunt", 250, 9, "A heavy iron mace")
warhammer = weapon(8, "Warhammer", "blunt", 600, 15, "A large two-handed hammer")
#########################################
# Armor #################################
#########################################
# No Armor
tunic = armor(1, "Tunic", "Light", 0, 1, "Basic Shirt")

# Light Armor
leather_armor = armor(2, "Leather Armor", "Light", 150, 3, "Basic leather armor")
studded_leather = armor(3, "Studded Leather", "Light", 300, 5, "Leather armor reinforced with metal studs")

# Medium Armor
chain_mail = armor(4, "Chain Shirt", "Medium", 500, 7, "A shirt made of interlocking metal rings")
scale_mail = armor(5, "Scale Mail", "Medium", 800, 10, "Armor made of overlapping metal scales")

# Heavy Armor
plate_mail = armor(6, "Plate Mail", "Heavy", 1500, 15, "Full suit of plate armor")