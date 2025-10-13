from functions.classes import *

#########################################
# Hero ##################################
#########################################
hero_player = player('Krynnlord', 100, 100, 0, 0, 0, 0, 1, 2, 0, 1, 2)

#########################################
# Items #################################
#########################################
potion = item("Potion of Healing", "potion", 500, 1, "") # 2d4 + 2 of healing, takes an action

hero_items = [potion]
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
hands = weapon("Hands", "blunt", 0, "1d2","")

# Blunt
club = weapon("Club", "blunt", 200, "1d4", "")
mace = weapon("Mace", "blunt", 500, "1d6", "")
lighthammer = weapon("Light Hammer", "blunt", 1000, "1d8", "")
warhammer = weapon("warhammer", "blunt", 1000, "1d10", "")
maul = weapon("Maul", "blunt", 5000, "2d6", "")

# Slashing
dagger = weapon("Dagger", "slashing", 200, "1d4", "")
handaxe = weapon("Handaxe", "slashing", 500, "1d6", "")
shortsword = weapon("Short Sword", "slashing", 1000, "1d8", "")
longsword = weapon("Long Sword", "slashing", 1500, "1d10", "")
greatsword = weapon("Great Sword", "slashing", 5000, "2d6", "")

hero_weapon = hands

#########################################
# Armor #################################
#########################################
# No Armor
tunic = armor("Tunic", "Light", 0, 1,"")

# Light
cloth_armor = armor("Cloth Armor", "Light", 50, 5, "")
leather_armor = armor("Leather Armor", "Light", 100, 11, "")

# Medium
chain_armor = armor("Chain Armor", "Medium", 500, 13, "")
scale_armor = armor("Scale Armor", "Medium", 600, 14, "")

# Heavy
splint_armor = armor("Splint Armor", "Heavy", 2000, 17, "")
plate_armor = armor("Plate Armor", "Heavy", 3000, 18, "")

hero_armor = tunic

#########################################
# Monsters ##############################
#########################################
zombie = monster("Zombie",22,22,0,0,0,0,1,0,8)
skeleton = monster("Skeleton",13,13,0,0,0,0,1,0,13)
giant_bat = monster("Giant Bat",22,22,0,0,0,0,1,0,13)
giant_boar = monster("Giant Boar",42,42,0,0,0,0,1,0,12)


# Create Final Hero
hero = [hero_player, hero_armor, hero_weapon, hero_items, hero_spells]