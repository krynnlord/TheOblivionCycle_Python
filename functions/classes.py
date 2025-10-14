# Player Class
class player:
    def __init__(self, name, hp, hp_max, luck, DEF_m, DEF_s, DEF_b, level, mod, exp, stat, gold):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.luck = luck
        self.DEF_m = DEF_m
        self.DEF_s = DEF_s
        self.DEF_b = DEF_b
        self.level = level
        self.mod = mod
        self.exp = exp
        self.stat = stat
        self.gold = gold

# Monster Class
class monster:
    def __init__(self, name, hp, hp_max, luck, DEF_m, DEF_s, DEF_b, level, mod, ac, stat):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.luck = luck
        self.DEF_m = DEF_m
        self.DEF_s = DEF_s
        self.DEF_b = DEF_b
        self.level = level
        self.mod = mod
        self.ac = ac
        self.stat = stat
        
# Spells Class
class spell:
    def __init__(self, name, desc, qty, ready, modifier, circle, levelreq):
        self.name = name
        self.desc = desc
        self.qty = qty
        self.ready = ready
        self.modifier = modifier # Heal or Damage
        self.circle = circle
        self.levelreq = levelreq

# Flask Class
class flask:
	def __init__(self, name, qty, desc):
		self.name = name
		self.qty = qty
		self.desc = desc
	
	def add(self,qty):
		self.qty += qty

	def remove(self,qty):
		self.qty -= qty

# Weapons Class 
class weapon:
    def __init__(self, id, name, type,  cost, damage, description, have):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = damage
        self.description = description
        self.have = have
         
# Armor Class 
class armor:
    def __init__(self, id, name, type,  cost, armorclass, description, have):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost
        self.armorclass = armorclass
        self.description = description
        self.have = have

class ColorStyle():
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"