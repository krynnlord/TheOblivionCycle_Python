# Game Metadata
GameDescInfo = { 
'GameTitle' : 'The Oblivion Cycle',
'GameSubtitle' : 'Part I: The Shimmering Gate',
'GameVersion' : '0.1',
'Copyright' : 'RLM Productions',
'Author' : 'Richard Miller'
}

def battle_seq():
    import os, random
    from rich.console import Console, Theme
    from rich.table import Table
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    # Define Hero
    hero_class = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck': 0,'level' : 0}
    hero1 = hero_class
    hero1['name'] = 'Kyrnnlord'
    hero1['level'] = 4
    hero1['HP'] = 200
    hero1['HP_max'] = 200
    hero1['MP'] = 100
    hero1['MP_max']  = 100
    hero1['luck'] = 2

    # Hero Equiped
    equipment = {'weapon' : '', 'armor' :'' }
    hero_equip = equipment
    hero_equip['weapon'] = 'Short Sword'
    hero_equip['armor'] = 'Cloth Armor'

    # Define Enemy 
    enemy = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck' : 0, 'level': 0}
    enemy_current = enemy
    enemy_current['name'] = 'Ghoul'
    enemy_current['level'] = 1
    enemy_current['HP'] = 200
    enemy_current['HP_max'] = 200
    enemy_current['MP'] = 0
    enemy_current['MP_max']  = 0
    enemy_current['luck'] = 1

    # Battle Strings
    hero_combat_string = "Ready for Combat."
    enemy_combat_string = "Ready for Combat."

    # Combat Active
    endcombat = False

    # Set Sounds *** 0-MISS 1-HIT 2-KILL 3-CRIT 4-NONE
    hitmiss = 4
    hitmiss_e = 4
    # l.play_music("asset/music/11.ogg",.5)

    # Battle Loop


    while True:

        os.system('cls')

        # Hero Display
        table = Table(title='Player', title_justify='left', style='green')
        hero_table_line = ("Name                   Level: "+ str(hero1['level']))
        table.add_column(hero_table_line, width = 35)
        hero_disp_hp = (str(hero1['HP'])+'/'+ str(hero1['HP_max']))
        hero_line1 = (hero1['name'])

        table.add_column("HP: " + hero_disp_hp, width = 25)


        # print HERO HPbar
        hp_bar = ""
        if hero1['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero1['HP'] / hero1['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "[green]█[/green]"
            bar_ticks -= 1
        hero_line2 = (hp_bar)

        # Create Hero Table
        table.add_row(hero_line1,hero_line2)
        console.print(table)

        # Enemy Display
        table = Table(title = 'Enemy', title_justify='left', style="red")
        enemy_table_line = ("Name                   Level: "+ str(enemy_current['level']))
        table.add_column(enemy_table_line, width = 35)

        enemy_disp_hp = (str(enemy_current['HP'])+'/'+ str(enemy_current['HP_max']))
        enemy_line1 = (enemy_current['name'])

        table.add_column("HP: " + enemy_disp_hp, width = 25)

        # print HERO HPbar
        hp_bar = ""
        if enemy_current['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['HP'] / enemy_current['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "[green]█[/green]"
            bar_ticks -= 1
        enemy_line2 = (hp_bar)

        # Create Enemy Table
        table.add_row(enemy_line1,enemy_line2)
        console.print(table)

        # Setup Battle Log Table
        table = Table(title ='Battle Log:', style="white", title_justify="left", width=75)
        table.add_column("[yellow]Combat[/yellow]")
        if hitmiss == 1: 
            play_sound('asset/sounds/hit.wav')
        if hitmiss == 0:
            play_sound('asset/sounds/miss.wav')
        if hitmiss == 2:
            play_sound('asset/sounds/kill.wav')
        if hitmiss == 3:
            play_sound('asset/sounds/crit.wav')       
        if hitmiss_e == 1:
            play_sound('asset/sounds/hit.wav')
        if hitmiss_e == 2:
            play_sound('asset/sounds/kill.wav')
        if hitmiss_e == 0:
            play_sound('asset/sounds/miss.wav')
        if hitmiss_e == 3:
            play_sound('asset/sounds/crit.wav') 
        
        # Print the combat strings    
        hero_combat_string = ("[green]"+hero1['name']+'[/green]: ' + hero_combat_string+'\n')          
        enemy_combat_string = ("[red]"+ enemy_current['name']+'[/red]: '+enemy_combat_string)
        
        table.add_row(hero_combat_string+enemy_combat_string)
        console.print(table)
        
        # Actions Menu
        if endcombat == True:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline")        
            console.print("1) :door: Exit Combat")
            ans = input('\nCommand > ')
            # l.play_music("asset/music/11.ogg",.5)
            break
        else:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline red")
            console.print("1) :dagger:  Attack with " + hero_equip['weapon'])
            console.print("2) :sparkler: Spellbook")
            console.print("3) :handbag: Inventory")
            console.print("4) :runner: Run")


        ans = input('\nCommand > ')
        if ans == '1' or ' ':

            # Hero Turn
            atk_value = random.randrange(0,20)
            modifier_value = 0
            hero_crit = 0
            luckmod = random.randrange(hero1['luck'], 20)
            if luckmod >= 16:
                modifier_value = round((atk_value*hero1['luck']) * 1.1)
                hero_crit = 1
            if hero_crit == 1:
                enemy_current['HP'] -= atk_value + modifier_value
            else:        
                enemy_current['HP'] -= atk_value
            if enemy_current['HP'] <= 0:
                enemy_current['HP'] = 0
                hero_combat_string = "Hits "+enemy_current['name']+ " with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage, and kills it!"
                hitmiss = 2
                endcombat = True
            else:    
                if atk_value >= 1:
                    if hero_crit == 1:
                        hero_combat_string = "*CRITICAL* Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value+ modifier_value) +" damage."
                        hitmiss = 3
                    else:
                        hero_combat_string = "Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage."
                        hitmiss = 1
                else:
                    hero_combat_string = "misses "+enemy_current['name']  +"."
                    hitmiss = 0
            # Enemy Turn
            #print(enemy_current['name']+' attacks you.')
            atk_value = random.randrange(0,15)
            hero1['HP'] -= atk_value
            if endcombat == True:
                atk_value = 0
            if hero1['HP'] <= 0:
                hero1['HP'] = 0
                enemy_combat_string = enemy_current['name']+" has killed you."
                endcombat = True
            else:    
                if atk_value >= 1:
                    enemy_combat_string = "Hits " + hero1['name'] +" for " + str(atk_value) +" damage."
                else:
                    if endcombat == True:
                        enemy_combat_string = "Dead."
                    else:
                        enemy_combat_string = "misses " + hero1['name'] +"."

        if ans == '2':
            spellbook()
            hitmiss = 4
        if ans == '3':
            inventory()
            hitmiss = 4
        if ans == '4':
            endcombat = True
            hitmiss = 4

def adventuremenu():
    from functions.classes import player
    import os, sqlite3
    from rich.console import Console, Theme    

    hero = player('','','','','','','','','','','','')
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    result = cur.execute("select name,hp,hp_max,luck,DEF_m,DEF_s,DEF_b,level,mod,exp,stat,gold from hero").fetchone()
    hero.name = result[0]
    hero.hp = result[1]
    hero.hp_max = result[2]
    hero.luck = result[3]
    hero.DEF_m = result[4]
    hero.DEF_s = result[5]
    hero.DEF_b = result[6]
    hero.level = result[7]
    hero.mod = result[8]
    hero.exp = result[9]
    hero.stat = result[10]
    hero.gold = result[11]
    con.close()
    
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/village.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) The Circle of Stones")
        console.print("([red]2[/red]) The Castle")
        console.print("([red]3[/red]) The Temple")
        console.print("([red]4[/red]) The Blacksmith")
        console.print("([red]5[/red]) The Provisioner")
        console.print("([red]6[/red]) The Inn")
        console.print("([red]7[/red]) Back to Main Menu")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1':
            stones(hero)
        elif ans == '2':
            castle(hero)
        elif ans == '3':
            temple(hero)
        elif ans == '4':
            blacksmith(hero)
        elif ans == '5':
            provisioner(hero)          
        elif ans == '6':
            inn(hero)
        elif ans == 's' or ans == 'S':
            display_score(hero)    
        elif ans == '7':
            break
    
def blacksmith(hero):
    import os, cursor, time, sqlite3
    from rich.console import Console, Theme 
    from functions.variables import ColorStyle
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/blacksmith.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Buy Weapons")
        console.print("([red]2[/red]) Buy Armor")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break
         
def castle(hero):
    import os
    from rich.console import Console, Theme
    from functions.variables import chain_armor, shortsword
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/castle.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Speak with King")
        console.print("([red]2[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1':
            if hero.level == 1:
                console.print(f"\nThe King looks at you with disdain.\n\n'You are not yet ready for a quest, {hero.name}. Return when you have proven yourself.'")
                console.input('\nPress any key to return...')
                hero.level += 1
                hero.exp += 200


        if ans == '2':
            break
        
def createhero():
    import os, cursor, time, sqlite3
    from functions.classes import ColorStyle
    
    os.system('cls')
    filetitle = 'asset/art/createhero.dat'
    data = ''
    print(f"{ColorStyle.YELLOW}"+loadart(filetitle, data)+f"{ColorStyle.RESET}")
    print("\nCreating a new game. Please enter a name for your hero.")
    cursor.show()
    name = input('Name: ' )
    if name == '':
        cursor.hide()
        print('You must enter a name.')
        time.sleep(2)
        createhero()
    if len(name) < 3:
        cursor.hide()
        print('Your name must be 3 characters or more in length')
        time.sleep(2)
        createhero()
    #Verification on new game
    cursor.hide()
    shortname = name[:10]
    delay_print2(f'{ColorStyle.RED}\nWARNING: {ColorStyle.RESET}This will delete your current game progress!')
    delay_print2("\nAre you sure you want to start over as "+ f'{ColorStyle.YELLOW}'+shortname+f'{ColorStyle.RESET}' +"?")
    cursor.show()
    ans = input(" (Y/N) ")
    
    if ans == 'y' or ans == 'Y':
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        # Write to DB - HERO
        cur.execute("update hero set name='" + shortname + "',hp=10,hp_max=10,luck=5,DEF_m=0,DEF_s=0,DEF_b=0,level=1,mod=0,exp=0,stat=1,gold=0")
        con.commit()
        con.close()
        print('New game started....')
        time.sleep(2)
        return        
    
    if ans == 'n' or ans == 'N':
        return

def diceroller(diceroll):
	import random
 
	total = []

	for i in range(int(diceroll[0])):
		roll = random.randrange(1, int(diceroll[2])+1)
		total.append(roll)
		final = sum(total)
	
	return final

def critroller(luck):
#################################################################
# Crit Chance roller. Dice must be 20 to crit. Improved by Luck #
#################################################################
	import random
 
	crit = 0
	roll = random.randrange((1 + luck), 21)

	if roll == 20:
		crit = 1 # Critical Strike
	elif roll == 1:
		crit = 2 # Miss
	else:
		crit = 0 # Normal Strike
	return crit

def damage_calc(luck, mod, weapon_damage):
##########################
# Main Damage Calculator #
##########################
	# Base Attack Value
	atk_value = diceroller(weapon_damage) + mod
	
	# Initilize Modifier and Crit(0-No 1-Yes)
	modifier_value = 0
	success_crit = 0
	
	# Roll Crit Dice
	success_crit = critroller(luck)
	
	# Result in crit or no crit
	if success_crit == 1:
		modifier_value = atk_value + mod + diceroller(weapon_damage)
	elif success_crit == 2:
		modifier_value = 0
	else:
		modifier_value = atk_value + mod

	# return value and crit value
	return modifier_value, success_crit 

def gameinfo():
    import os
    from rich.console import Console, Theme
    
    os.system("cls")
    data = ''
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    filetitle = 'asset/art/gameinfo.dat'
    console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n\n")
    
    console.print("[yellow]     Game:[/yellow] "+GameDescInfo["GameTitle"] + ' - ' + GameDescInfo["GameSubtitle"])
    console.print("[yellow]Copyright:[/yellow] "+GameDescInfo["Copyright"])
    console.print("[yellow]   Author:[/yellow] "+str(GameDescInfo["Author"]))
    console.print("[yellow]  Version:[/yellow] "+str(GameDescInfo["GameVersion"]))
    console.print("[yellow]    Music:[/yellow] Alkakrab @ https://alkakrab.itch.io/")

    console.input('\n[yellow]Press any key to return...[/yellow]')

def hero_status_bar(hero):
    
    from rich.console import Console, Theme
    
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    
    for i in range(90):
        console.print ("-", end="")
    console.print("\n[green]"+hero.name + "[white]   Level: " + str(hero.level) + "   Exp: " + str(hero.exp)+"[/white]", end="   ")
    
    console.print("Gold: " + str(hero.gold))
    for i in range(90):
        console.print ("-", end="")
    console.print("\n")
    
def inn(hero):
    import os
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/inn.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Rest")
        console.print("([red]2[/red]) Open Wardrobe")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break

def intro():
    import os, time, cursor
    from functions.variables import ColorStyle
                 
    cursor.hide() #hides cursor

    os.system('cls')
    time.sleep(2.2) # pause for Dramatic Musical Intro

    # Load RLM Productions Logo
    filetitle = 'asset/art/rlm.dat'
    data = ''    
    print(f"{ColorStyle.YELLOW}"+loadart(filetitle, data)+f"{ColorStyle.RESET}")
    for i in range(54):
        print(" ", end="")
    time.sleep(2)    
    delay_print("presents an original game")
    time.sleep(5)

    # Main Logo Display
    filetitle = 'asset/art/title.dat'
    data = ''
    os.system('cls')
    print(f"{ColorStyle.RED}"+loadart(filetitle, data)+f"{ColorStyle.RESET}")
    time.sleep(2)
    delay_print("                          Chapter I: The Shimmering Gate")
    time.sleep(2)
    delay_print("\n\nOur story begins in a kingdom just south of the mighty river Hyatin,\n")
    delay_print("known for its production of a special mineral name Shieya.\n\n")
    time.sleep(1)
    delay_print("This mineral has an unique property that many nations seek, and is coveted beyond\n")
    delay_print("measure to the point where many are willing to kill for it.\n\n")
    time.sleep(1)
    delay_print("In these trying times a hero emerges....")
    time.sleep(4)

def inventory():
    import os, copy
    from rich.console import Console, Theme
    from rich.table import Table
    
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

  # Temp Variables
    class Item:
        def __init__(self, name, attack:int, defense:int, desc, qty:int):
            self.name = name
            self.attack = attack
            self.defense = defense
            self.desc = desc
            self.qty = qty

    cloth_armor = Item("Cloth Armor", 0, 2, "A robe that covers the wearer but supplies little armor", 1)
    short_sword = Item("Short Sword",5, 0, "A small sword that deals normal damage", 1)

    real_cloth_armor = copy.deepcopy(cloth_armor)

    hero_inv = [real_cloth_armor,short_sword]
    hero_equip_armor = cloth_armor
    hero_equip_weapon = short_sword
    hero_gold = 2232 

    real_cloth_armor.qty = real_cloth_armor.qty + 5  


    os.system("cls")
    # Equipped Table
    table = Table(title="Current Equipment", title_justify="left")
    table.add_column("Type", style="normal", width=10)
    table.add_column("Item", style="normal", width=20)
    table.add_column("Atk", style="normal", width=3)
    table.add_column("Def", style="normal", width=3)

    # Equipment Definition
    table.add_row("Body","[green]"+hero_equip_armor.name+"[/green]",str(hero_equip_armor.attack),str(hero_equip_armor.defense))
    table.add_row("Weapon","[red]"+hero_equip_weapon.name+"[/red]",str(hero_equip_weapon.attack),str(hero_equip_weapon.defense))
    console.print(table)

    # Inventory Table
    table = Table(title="Inventory", title_justify="left")
    table.add_column("Item Name", style="cyan", width=25)
    table.add_column("Qty", style="normal", width=3)
    table.add_column("Description", style="normal")

    a = 1
    for i in hero_inv:
        table.add_row("[normal]"+str(a)+') [/normal]'+ i.name,str(i.qty),i.desc)
        a +=1
    console.print(table)

    # Gold Table
    table = Table()
    table.add_column("Currency", style="yellow", width=10)
    table.add_column("Qty", style="yellow", width=5)
    table.add_row("Gold",str(hero_gold))
    console.print(table)
    console.print('\n')
    console.input('Press any key to return...')
  
def checklevelup(level, prof, exp):
	 
    if exp >= 300 and exp < 900:
        level = 2
        prof = 4
    if exp >= 900 and exp < 2700:
        level = 3
        prof = 6
    if exp >= 2700 and exp < 6500:
        level = 4
        prof = 8
    if exp >= 6500 and exp < 14000:
        level = 5
        prof = 11
    if exp >= 14000 and exp < 23000:
        level = 6
        prof = 14
    if exp >= 23000 and exp < 34000:
        level = 7
        prof = 17
    if exp >= 34000 and exp < 48000:
        level = 8
        prof = 20
    if exp >= 48000 and exp < 64000:
        level = 9
        prof = 24
    if exp >= 64000 and exp < 85000:
        level = 10
        prof = 28
    if exp >= 85000 and exp < 100000:
        level = 11
        prof = 32
    if exp >= 100000 and exp < 120000:
        level = 12
        prof = 36
    if exp >= 120000 and exp < 140000:
        level = 13
        prof = 41    
    if exp >= 140000 and exp < 165000:
        level = 14
        prof = 46
    if exp >= 165000 and exp < 195000:
        level = 15
        prof = 51
    if exp >= 195000 and exp < 225000:
        level = 16
        prof = 56
    if exp >= 225000 and exp < 265000:
        level = 17
        prof = 62
    if exp >= 265000 and exp < 305000:
        level = 18
        prof = 68
    if exp >= 305000 and exp < 355000:
        level = 19
        prof = 74
    if exp > 355000:
        level = 20
        prof = 80
            
    return level, prof

def loadart(filetitle, data):
    with open(filetitle, 'r') as file:
        data = file.read().rstrip()
        return(data)
    
def music():
    import os, sqlite3
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/music.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[cyan]"+loadart(filetitle, data)+"[/cyan]\n\n")
  
        # Print Choices
        console.print("[yellow]1[/yellow]) Elven Ruins         [yellow]7[/yellow]) The Iron Wall")
        console.print("[yellow]2[/yellow]) To Oblivion         [yellow]8[/yellow]) Lullaby")
        console.print("[yellow]3[/yellow]) Mysterious Portal   [yellow]9[/yellow]) Spiraling Descent")
        console.print("[yellow]4[/yellow]) Cryptic Walls      [yellow]10[/yellow]) Distant Stars")
        console.print("[yellow]5[/yellow]) Bard's Story       [yellow]11[/yellow]) Judgement")
        console.print("[yellow]6[/yellow]) Shimmering Lights  [yellow]12[/yellow]) Ascendancy")
        console.print("\n[yellow]0[/yellow]) Back")
        ans = console.input("\n[yellow]Selection> [/yellow]")

        con = sqlite3.connect('data.db')
        cur = con.cursor()


        if ans == '1':
            play_music("asset/music/01.ogg")
            cur.execute("update options set value = 1 where id = 3")
            con.commit()
        if ans == '2':
            play_music("asset/music/02.ogg")
            cur.execute("update options set value = 2 where id = 3")
            con.commit()
        if ans == '3':
            play_music("asset/music/03.ogg")
            cur.execute("update options set value = 3 where id = 3")
            con.commit()
        if ans == '4':
            play_music("asset/music/04.ogg")
            cur.execute("update options set value = 4 where id = 3")
            con.commit()
        if ans == '5':
            play_music("asset/music/05.ogg")
            cur.execute("update options set value = 5 where id = 3")
            con.commit()            
        if ans == '6':
            play_music("asset/music/06.ogg")
            cur.execute("update options set value = 6 where id = 3")
            con.commit()
        if ans == '7':
            play_music("asset/music/07.ogg")
            cur.execute("update options set value = 7 where id = 3")
            con.commit()
        if ans == '8':
            play_music("asset/music/08.ogg")
            cur.execute("update options set value = 8 where id = 3")
            con.commit()
        if ans == '9':
            play_music("asset/music/09.ogg")
            cur.execute("update options set value = 9 where id = 3")
            con.commit()
        if ans == '10':
            play_music("asset/music/10.ogg")
            cur.execute("update options set value = 10 where id = 3")
            con.commit()
        if ans == '11':
            play_music("asset/music/11.ogg", .3)
            cur.execute("update options set value = 11 where id = 3")
            con.commit()
        if ans == '12':
            play_music("asset/music/12.ogg", .3)
            cur.execute("update options set value = 12 where id = 3")
            con.commit()            

        if ans == '0':
            return
        
def play_music(mp3File,vol=.5):
    import pygame
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound(mp3File)
    channel = pygame.mixer.Channel(0)
    channel.play(sound, -1)
    channel.set_volume(vol)

def music_toggle():
    import pygame
    
    if pygame.mixer.Channel(0).get_busy():
        pygame.mixer.Channel(0).pause()
    else:
        pygame.mixer.Channel(0).unpause()

def play_midi(midifile,vol):
    import pygame
    
    pygame.mixer.init(44100,-16,1,1024)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.load(midifile)
    pygame.mixer.music.play(-1)

def midi_toggle():
    import pygame
    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def music_lower():
    import pygame
    
    current_volume = pygame.mixer.music.get_volume()
    new_volume = current_volume - .1
    pygame.mixer.music.set_volume(new_volume)
    
def music_raise():
    import pygame
    
    current_volume = pygame.mixer.music.get_volume()
    new_volume = current_volume + .1
    pygame.mixer.music.set_volume(new_volume)

def play_sound(mp3File):
    import pygame
    
    pygame.mixer.init()
    sound = pygame.mixer.Sound(mp3File)
    channel = pygame.mixer.Channel(1)
    channel.set_volume(1)
    channel.play(sound)    

def gameoptions():
    
    import os, sqlite3
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/options.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n\n")

        # Read Game Options from database
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        result_music = cur.execute("select value from options where id = 1").fetchone() 
        result_title = cur.execute("select value from options where id = 2").fetchone()
        result_battle = cur.execute("select value from options where id = 4").fetchone() 
        

        # Print Choices
        if result_title[0] == 0:
            console.print("([red]1[/red]) Show Intro (Currently: [red]Off[/red])")
        else:
            console.print("([red]1[/red]) Show Intro (Currently: [green]On[/green])")

        if result_music[0] == 1:            
            console.print("([red]2[/red]) Play Music (Currently: [green]On[/green])")
        else:    
            console.print("([red]2[/red]) Play Music (Currently: [red]Off[/red])")
        
        if result_battle[0] == 1:            
            console.print("([red]3[/red]) Modern Battle System (Currently: [green]On[/green])")
        else:    
            console.print("([red]3[/red]) Modern Battle System (Currently: [red]Off[/red])")
        console.print("([red]4[/red]) Game Information")
        console.print("([red]5[/red]) Music Player")
        console.print("([red]6[/red]) Return")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1': # Toggle Intro Logic
            
            if result_title[0] == 1:
                cur.execute("update options set value = 0 where id = 2")
                con.commit()
            else:
                cur.execute("update options set value = 1 where id = 2")
                con.commit()

        elif ans == '2': # Toggle Music Logic
            if result_music[0] == 1:
                cur.execute("update options set value = 0 where id = 1")
                con.commit()
                music_toggle()
            else:
                cur.execute("update options set value = 1 where id = 1")
                con.commit()
                result_musictrack = cur.execute("select value from options where id = 3").fetchone()
                music_selected = f'{result_musictrack[0]:02d}' # Convert to 2 digits if 1
                musictrack = 'asset/music/'+str(music_selected)+'.ogg'
                play_music(musictrack)
        
        elif ans == '3': # Toggle Battle Version
            
            if result_battle[0] == 1:
                cur.execute("update options set value = 0 where id = 4")
                con.commit()
            else:
                cur.execute("update options set value = 1 where id = 4")
                con.commit()                
        
        elif ans == '4':
            gameinfo()
        
        elif ans == '5':
            music()
        
        elif ans == '6':
            break
    
def delay_print(s):
    import sys, time
    # Text-Printer Slow
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
        
def delay_print2(s):
    import sys, time
    # Text-Printer Normal
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
        
def provisioner(hero):
    import os
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/provisions.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Buy Items")
        console.print("([red]2[/red]) Sell Items")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break
        
def r_battle_seq():
    import os, random
    from rich.console import Console, Theme
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    # Define Hero
    hero_class = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck': 0,'level' : 0}
    hero1 = hero_class
    hero1['name'] = 'Kyrnnlord'
    hero1['level'] = 4
    hero1['HP'] = 200
    hero1['HP_max'] = 200
    hero1['MP'] = 100
    hero1['MP_max']  = 100
    hero1['luck'] = 2

    # Hero Equiped
    equipment = {'weapon' : '', 'armor' :'' }
    hero_equip = equipment
    hero_equip['weapon'] = 'Short Sword'
    hero_equip['armor'] = 'Cloth Armor'

    # Define Enemy 
    enemy = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck' : 0, 'level': 0}
    enemy_current = enemy
    enemy_current['name'] = 'Ghoul'
    enemy_current['level'] = 1
    enemy_current['HP'] = 200
    enemy_current['HP_max'] = 200
    enemy_current['MP'] = 0
    enemy_current['MP_max']  = 0
    enemy_current['luck'] = 1

    # Battle Strings
    hero_combat_string = "Ready for Combat."
    enemy_combat_string = "Ready for Combat."

    # Combat Active
    endcombat = False

    # Set Sounds *** 0-MISS 1-HIT 2-KILL 3-CRIT 4-NONE
    hitmiss = 4
    hitmiss_e = 4
    # l.play_music("asset/music/11.ogg",.5)

    # Battle Loop
    while True:

        os.system('cls')

        # Hero Display
        console.print("Hero")
        for i in range(70):
            console.print("-", end="")
        console.print("\nName: " + hero1['name'], end="    ")
        console.print("Level: "+ str(hero1['level']), end="   ")
        console.print("Weapon: " + hero_equip['weapon'], end="   ")
        console.print("Armor: " + hero_equip['armor'])

        hppercent = 100 * round(hero1['HP']) / round(hero1['HP_max'])
        if hppercent >= 75:
            console.print("[green]" + str(hppercent) + '%[/green]',end="   ")
        elif hppercent < 75 and hppercent > 40:
            console.print("[yellow]" + str(hppercent) + '%[/yellow]',end="   ")
        else:
            console.print("[red]" + str(hppercent) + '%[/red]',end="   ")
        console.print("HP: " + str(hero1['HP'])+'/'+ str(hero1['HP_max']))

        # print HERO HPbar
        hp_bar = ""
        if hero1['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero1['HP'] / hero1['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += ":"
            bar_ticks -= 1
        hero_line2 = (hp_bar)
        if hppercent >= 75:
            console.print("[green]"+ hero_line2 + "[/green]")
        elif hppercent < 75 and hppercent > 40:
            console.print("[yellow]" + hero_line2 + "[/yellow]")
        else:
            console.print("[red]" + hero_line2 + "[/red]")
        
        console.print("\n")
        
        # Enemy Display
        console.print("Enemy")
        for i in range(70):
            console.print("-", end="")
        console.print("\nName: " + enemy_current['name'], end="    ")
        console.print("Level: "+ str(enemy_current['level']), end="\n")
        
        hppercent_e = 100 * round(enemy_current['HP']) / round(enemy_current['HP_max'])
        if hppercent_e >= 75:
            console.print("[green]" + str(hppercent_e) + '%[/green]',end="   ")
        elif hppercent_e < 75 and hppercent_e > 40:
            console.print("[yellow]" + str(hppercent_e) + '%[/yellow]',end="   ")
        else:
            console.print("[red]" + str(hppercent_e) + '%[/red]',end="   ")
        console.print("HP: " + str(enemy_current['HP'])+'/'+ str(enemy_current['HP_max']))
        
        # print Enemy HPbar
        hp_bar = ""
        if enemy_current['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['HP'] / enemy_current['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += ":"
            bar_ticks -= 1
        enemy_line2 = (hp_bar)
        if hppercent_e >= 75:
            console.print("[green]"+ enemy_line2 + "[/green]")
        elif hppercent_e < 75 and hppercent_e > 40:
            console.print("[yellow]" + enemy_line2 + "[/yellow]")
        else:
            console.print("[red]" + enemy_line2 + "[/red]")
        
        console.print("\n")
  
        # Attack Sounds
        if hitmiss == 1: 
            play_sound('asset/sounds/hit.wav')
        if hitmiss == 0:
            play_sound('asset/sounds/miss.wav')
        if hitmiss == 2:
            play_sound('asset/sounds/kill.wav')
        if hitmiss == 3:
            play_sound('asset/sounds/crit.wav')       
        if hitmiss_e == 1:
            play_sound('asset/sounds/hit.wav')
        if hitmiss_e == 2:
            play_sound('asset/sounds/kill.wav')
        if hitmiss_e == 0:
            play_sound('asset/sounds/miss.wav')
        if hitmiss_e == 3:
            play_sound('asset/sounds/crit.wav') 
        
        # Print the combat strings 
        console.print("Battle Log")
        for i in range(70):
            console.print("-", end="")       
        hero_combat_string = ("\n[green]"+hero1['name']+'[/green]: ' + hero_combat_string+'\n')          
        enemy_combat_string = ("[red]"+ enemy_current['name']+'[/red]: '+enemy_combat_string)
        console.print(hero_combat_string+enemy_combat_string, end="\n\n")

        # Actions Menu
        if endcombat == True:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline yellow")        
            console.print("1) Exit Combat")
            ans = input('\nCommand > ')
            # l.play_music("asset/music/11.ogg",.5)
            break
        else:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline yellow")
            console.print("1) Attack")
            console.print("2) Spellbook")
            console.print("3) Inventory")
            console.print("4) Run")


        ans = input('\nCommand > ')
        if ans == '1' or ' ':

            # Hero Turn
            atk_value = random.randrange(0,20)
            modifier_value = 0
            hero_crit = 0
            luckmod = random.randrange(hero1['luck'], 20)
            if luckmod >= 16:
                modifier_value = round((atk_value*hero1['luck']) * 1.1)
                hero_crit = 1
            if hero_crit == 1:
                enemy_current['HP'] -= atk_value + modifier_value
            else:        
                enemy_current['HP'] -= atk_value
            if enemy_current['HP'] <= 0:
                enemy_current['HP'] = 0
                hero_combat_string = "Hits "+enemy_current['name']+ " with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage, and kills it!"
                hitmiss = 2
                endcombat = True
            else:    
                if atk_value >= 1:
                    if hero_crit == 1:
                        hero_combat_string = "*CRITICAL* Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value+ modifier_value) +" damage."
                        hitmiss = 3
                    else:
                        hero_combat_string = "Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage."
                        hitmiss = 1
                else:
                    hero_combat_string = "misses "+enemy_current['name']  +"."
                    hitmiss = 0

            # Enemy Turn
            atk_value = random.randrange(0,15)
            hero1['HP'] -= atk_value
            if endcombat == True:
                atk_value = 0
            if hero1['HP'] <= 0:
                hero1['HP'] = 0
                enemy_combat_string = enemy_current['name']+" has killed you."
                endcombat = True
            else:    
                if atk_value >= 1:
                    enemy_combat_string = "Hits " + hero1['name'] +" for " + str(atk_value) +" damage."
                else:
                    if endcombat == True:
                        enemy_combat_string = "Dead."
                    else:
                        enemy_combat_string = "misses " + hero1['name'] +"."

        if ans == '2':
            spellbook()
            hitmiss = 4
        if ans == '3':
            inventory()
            hitmiss = 4
        if ans == '4':
            endcombat = True
            hitmiss = 4

def display_score(hero):
    import os
    from rich.console import Console, Theme
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    while True:
        os.system('cls')
        filetitle="asset/art/score.dat"
        data = ''
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")
        hero_status_bar(hero)
        console.print("Luck: " + str(hero.luck),)
        console.print("Status: ", end="")
        if hero.stat == 1:
            console.print("Normal")
        elif hero.stat == 0:
            console.print("Dead")
        elif hero.stat == 2:
            console.print("Poisoned")
        ans = console.input("\n")

        break
    
def spellbook():
    import os
    from rich.console import Console, Theme
    from rich.table import Table
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    os.system("cls")

    table = Table(title="Spellbook", padding=(0, 0), width=85, title_justify='left')
    table.add_column("[red]Spells of the Magi[/red]", justify='left')
    table.add_column("[yellow]Lore[/yellow]", justify='left', style='normal')

    st = Table(
        padding=(0, 0),
        show_edge=False,
        show_lines=False,
    )
    st.add_column("Name", width=15, justify='left', style='cyan' )
    st.add_column("Circle", justify='center')
    st.add_column("Min Lvl", justify='center')
    st.add_column('Learned',justify='center')
    st.add_row('Heal', '1','1', '[green]Y[/green]')
    st.add_row('Cure', '1', '2','[red]N[/red]')
    st.add_row('Create Food', '1','3', '[red]N[/red]')
    st.add_row('Magic Missle', '1','4', '[red]N[/red]')
    st.add_row('Greater Heal', '2','5', '[red]N[/red]')
    st.add_row('Barrier', '2','6', '[red]N[/red]')
    st.add_row('Escape', '2', '7','[red]N[/red]')
    st.add_row('Fireball', '2', '8','[red]N[/red]')
    st.add_row('Regeneration', '3','9', '[red]N[/red]')
    st.add_row('Holy Ground', '3', '10','[red]N[/red]')
    st.add_row('Double', '3', '11','[red]N[/red]')
    st.add_row('Immolation', '3', '12','[red]N[/red]')

    tt="The spells of the Magi are composed of 3 circles. Each of these circles has 4 spells from each of the dispiplines. These are Invocation, Abjuration, Conjuration, and Evocation.\n\nInvocation is the study of healing spells. Abjuration focuses on protective magic. Conjuration creates objects, and Evocation is the destructive arts. Master each of these displines in their respective circles to become one with the elements.\n\n- Magnus Dylisia"
    table.add_row(st, tt)
    console.print(table)

    console.input('Press any key to return...')
    
def spellcast(hero_spells):
    from rich.console import Console, Theme
    from functions.variables import fireball, heal
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    for i in hero_spells:
        if i.ready == 1 and i.qty > 0:              
            console.print("[white]" + i.name + "[/white]("+str(i.qty) + ") ", end="")   

    ans2 = console.input("\nCast which spell? ")
    
    if ans2.lower() in ["fir", "fireball"] and fireball.qty > 0:
        console.input("You cast [red]Fireball[/red]")
        fireball.qty-= 1

    elif ans2.lower() in ["hea", "heal"] and heal.qty > 0:
        console.input("You cast [red]Heal[/red]")
        heal.qty -= 1        
    
    else:
        console.input("That is not a valid spell.")   
        
def stones(hero):
    import os
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/circleofstones.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)

        # Print Choices
        console.print("([red]1[/red]) Embark on quest")
        console.print("([red]2[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '2':
            break
        
def temple(hero):
    import os
    from rich.console import Console, Theme
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/temple.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Pray")
        console.print("([red]2[/red]) Memorize Spells")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break



        