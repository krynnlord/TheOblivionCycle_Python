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

#########################################
# Weapons ###############################
#########################################
# No Weapon
hands = weapon(7, "Hands", "blunt", 0, 1, "Your Hands", 1)

# Slashing
dagger = weapon(8, "Dagger", "slashing", 100, 5, "Small blade", 0)
short_sword = weapon(9, "Short Sword", "slashing", 200, 8, "A basic short sword", 0)
long_sword = weapon(10, "Long Sword", "slashing", 400, 12, "A sturdy long sword", 0)
greatsword = weapon(11, "Greatsword", "slashing", 800, 18, "A massive two-handed sword", 0)

# Blunt
club = weapon(12, "Club", "blunt", 50, 4, "A simple wooden club", 0)
mace = weapon(13, "Mace", "blunt", 250, 9, "A heavy iron mace", 0)
warhammer = weapon(14, "Warhammer", "blunt", 600, 15, "A large two-handed hammer", 0)

#########################################
# Armor #################################
#########################################
# No Armor
tunic = armor(1, "Tunic", "Light", 0, 1, "Basic Shirt", 1)

# Light Armor
leather_armor = armor(2, "Leather Armor", "Light", 150, 3, "Basic leather armor", 0)
studded_leather = armor(3, "Studded Leather", "Light", 300, 5, "Leather armor reinforced with metal studs", 0)

# Medium Armor
chain_mail = armor(4, "Chain Shirt", "Medium", 500, 7, "A shirt made of interlocking metal rings", 0)
scale_mail = armor(5, "Scale Mail", "Medium", 800, 10, "Armor made of overlapping metal scales", 0)

# Heavy Armor
plate_mail = armor(6, "Plate Mail", "Heavy", 1500, 15, "Full suit of plate armor", 0)