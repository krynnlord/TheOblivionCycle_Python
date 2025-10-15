from functions.variables import *
from functions.maps import *

# Game Metadata
GameDescInfo = {
'GameTitle' : 'The Oblivion Cycle',
'GameSubtitle' : 'Part I: The Shimmering Gate',
'GameVersion' : '0.1',
'Copyright' : 'RLM Productions',
'Author' : 'Richard Miller'
}

def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def battle_seq(hero):
    import random, cursor
    from rich.console import Console, Theme
    from rich.table import Table
    from functions.classes import monster
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    # Define Enemy 
    enemy_current = enemy_generator(hero[0].level)

    # Battle Strings
    hero_combat_string = "Ready for Combat."
    enemy_combat_string = "Ready for Combat."

    # Combat Active
    endcombat = False

    # Set Sounds *** 0-MISS 1-HIT 2-KILL 3-CRIT 4-NONE
    hitmiss = 4
    hitmiss_e = 4

    # Battle Loop
    while True:

        clear_screen()

        # Hero Display
        table = Table(title='Player', title_justify='left', style='green')
        hero_table_line = ("Name                   Level: "+ str(hero[0].level))
        table.add_column(hero_table_line, width = 35)
        hero_disp_hp = (str(hero[0].hp)+'/'+ str(hero[0].hp_max))
        hero_line1 = (hero[0].name)

        table.add_column("HP: " + hero_disp_hp, width = 25)


        # print HERO HPbar
        hp_bar = ""
        if hero[0].hp == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero[0].hp / hero[0].hp) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "[green]█[/green]"
            bar_ticks -= 1
        hero_line2 = (hp_bar)

        # Create Hero Table
        table.add_row(hero_line1,hero_line2)
        console.print(table)

        # Enemy Display
        table = Table(title = 'Enemy', title_justify='left', style="red")
        enemy_table_line = ("Name                   Level: "+ str(enemy_current.level))
        table.add_column(enemy_table_line, width = 35)

        enemy_disp_hp = (str(enemy_current.hp)+'/'+ str(enemy_current.hp_max))
        enemy_line1 = (enemy_current.name)

        table.add_column("HP: " + enemy_disp_hp, width = 25)

        # print HERO HPbar
        hp_bar = ""
        if enemy_current.hp_max == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current.hp / enemy_current.hp_max) * 100 / 4
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
        hero_combat_string = ("[green]"+hero[0].name+'[/green]: ' + hero_combat_string+'\n')          
        enemy_combat_string = ("[red]"+ enemy_current.name+'[/red]: '+enemy_combat_string)
        
        table.add_row(hero_combat_string+enemy_combat_string)
        console.print(table)
        
        # Actions Menu
        if endcombat == True:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline")        
            console.print("Press any key to Exit Combat")
            cursor.hide()
            choice_getch()
            break
                
        else:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline red")
            console.print("1) :dagger:  Attack with " + hero[2].name)
            console.print("2) :sparkler: Spellbook")
            console.print("3) :handbag: Inventory")
            console.print("4) :runner: Run")


        cursor.hide()
        ans = choice_getch()
        
        if ans == '1':

            # Hero Turn
            atk_value = random.randrange(0,20)
            modifier_value = 0
            hero_crit = 0
            luckmod = random.randrange(hero[0].luck, 20)
            if luckmod >= 16:
                modifier_value = round((atk_value*hero[0].luck) * 1.1)
                hero_crit = 1
            if hero_crit == 1:
                enemy_current.hp -= atk_value + modifier_value
            else:        
                enemy_current.hp -= atk_value
            if enemy_current.hp <= 0:
                enemy_current.hp = 0
                hero_combat_string = "Hits "+enemy_current.name+ " with "+hero[2].name +" for " + str(atk_value) +" damage, and kills it!"
                hitmiss = 2
                endcombat = True
            else:    
                if atk_value >= 1:
                    if hero_crit == 1:
                        hero_combat_string = "*CRITICAL* Hits "+enemy_current.name  +" with "+hero[2].name +" for " + str(atk_value+ modifier_value) +" damage."
                        hitmiss = 3
                    else:
                        hero_combat_string = "Hits "+enemy_current.name  +" with "+hero[2].name +" for " + str(atk_value) +" damage."
                        hitmiss = 1
                else:
                    hero_combat_string = "misses "+enemy_current.name  +"."
                    hitmiss = 0
            # Enemy Turn
            #print(enemy_current['name']+' attacks you.')
            atk_value = random.randrange(0,15)
            hero[0].hp -= atk_value
            if endcombat == True:
                atk_value = 0
            if hero[0].hp <= 0:
                hero[0].hp = 0
                enemy_combat_string = enemy_current.name+" has killed you."
                endcombat = True
            else:    
                if atk_value >= 1:
                    enemy_combat_string = "Hits " + hero[0].name +" for " + str(atk_value) +" damage."
                else:
                    if endcombat == True:
                        enemy_combat_string = "Dead."
                    else:
                        enemy_combat_string = "misses " + hero[0].name +"."
        
        if ans == '2':
            spellbook()
            hero_combat_string = 'Read Spellbook'
            enemy_combat_string = 'Waits'
        if ans == '3' or ans == 'I' or ans == 'i':
            inventory(hero)
            hero_combat_string = 'Looked at Inventory'
            enemy_combat_string = 'Waits'
        if ans == '4':
            endcombat = True
            hitmiss = 4
            hero_combat_string = 'Fled'
            enemy_combat_string = ''
        if ans not in ('1', '2', '3', '4'):
            hero_combat_string = 'Invalid Move'
            enemy_combat_string = 'Waits'
            
def adventuremenu():
    import cursor
    from rich.console import Console, Theme    
  
    hero = load_game()
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

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
        elif ans == 'i' or ans == 'I':
            inventory(hero)    
        elif ans == '7':
            save_game(hero)
            break
        elif ans == 'b': 
            battle_seq(hero)
    
def blacksmith(hero):
    import cursor
    from rich.console import Console, Theme 
    from functions.variables import ColorStyle
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '3':
            break
         
def castle(hero):
    import cursor
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '1':
            if hero[0].level == 1:
                console.print(f"\nThe King looks at you with disdain.\n\n'You are not yet ready for a quest, {hero[0].name}. Return when you have proven yourself.'")
                console.input('\nPress any key to return...')
                hero[0].level += 1
                hero[0].exp += 200
                
        if ans == '2':
            break
        
def createhero():
    import cursor, time, sqlite3
    from functions.classes import ColorStyle
    
    clear_screen()
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
    delay_print2("\nAre you sure you want to start over as "+ f'{ColorStyle.YELLOW}'+shortname+f'{ColorStyle.RESET}' +"? (Y/N)")
    cursor.show()
    
    cursor.hide()
    ans = choice_getch()
    
    if ans == 'y' or ans == 'Y':
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        # Write to DB - HERO
        cur.execute("update hero set name='" + shortname + "',hp=100,hp_max=100,luck=5,DEF_m=0,DEF_s=0,DEF_b=0,level=1,mod=0,exp=0,stat=1,gold=0")
        con.commit()
        con.close()
        print('\nNew game created....')
        time.sleep(2)
        return        
    
    else:
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
    import os, cursor
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
    console.print("[yellow]    Music:[/yellow] Richard Miller")

    console.print('\n[yellow]Press any key to return...[/yellow]')
    
    cursor.hide()
    choice_getch()

def hero_status_bar(hero):
    
    from rich.console import Console, Theme
    
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    
    for i in range(90):
        console.print ("-", end="")
    console.print("\n[green]"+hero[0].name + "[white]   Level: " + str(hero[0].level) + "   Exp: " + str(hero[0].exp)+"   Gold: " + str(hero[0].gold) +"[/white]")
    console.print("HP: "+ str(hero[0].hp) + " / " + str(hero[0].hp_max) + "    Armor: " + hero[1].name + "    Weapon: " + hero[2].name)
    for i in range(90):
        console.print ("-", end="")
    console.print("\n")
    
def inn(hero):
    import cursor
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '3':
            break

def intro():
    import os, time, cursor
    from functions.variables import ColorStyle
                 
    cursor.hide() #hides cursor

    clear_screen()
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
    clear_screen()
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

def inventory(hero):
    import os, copy, cursor
    from rich.console import Console, Theme
    from rich.table import Table
    
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    os.system("cls")
    # Equipped Table
    table = Table(title="Current Equipment", title_justify="left")
    table.add_column("Type", style="normal", width=10)
    table.add_column("Item", style="normal", width=20)
    table.add_column("Atk", style="normal", width=3)
    table.add_column("Def", style="normal", width=3)

    # Equipment Definition
    table.add_row("Body","[green]"+hero[1].name+"[/green]","-",str(hero[1].armorclass))
    table.add_row("Weapon","[red]"+hero[2].name+"[/red]",str(hero[2].damage),"-")
    console.print(table)

    # Inventory Table
    table = Table(title="Inventory", title_justify="left")
    table.add_column("Item Name", style="cyan", width=25)
    table.add_column("Description", style="normal")

    if hands.have == 1: table.add_row("7. " + hands.name,hands.description)
    if dagger.have == 1: table.add_row("8. "+ dagger.name,dagger.description)
    #for i in hero_inv:
    #    table.add_row("[normal]"+str(a)+') [/normal]'+ i.name,str(i.qty),i.desc)
    #    a +=1
    console.print(table)

    # Gold Table
    table = Table()
    table.add_column("Currency", style="yellow", width=10)
    table.add_column("Qty", style="yellow", width=5)
    table.add_row("Gold",str(hero[0].gold))
    console.print(table)
    cursor.hide()
    choice_getch()
  
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
    import cursor, sqlite3
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
        ans = ''
        filetitle = 'asset/art/music.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[cyan]"+loadart(filetitle, data)+"[/cyan]\n\n")
  
        # Print Choices
        console.print("[yellow]1[/yellow]) From Oblivion They Come")
        console.print("[yellow]2[/yellow]) To The Fallen")
        console.print("[yellow]3[/yellow]) Silver & Steel")
        console.print("[yellow]4[/yellow]) Gods & Demons")
        console.print("[yellow]5[/yellow]) The Ritual")
        console.print("[yellow]6[/yellow]) A Gate Manifests")
        console.print("[yellow]7[/yellow]) Ethereal Dreams")
        console.print("\n[yellow]0[/yellow]) Back")

        cursor.hide()
        ans = choice_getch()

        con = sqlite3.connect('data.db')
        cur = con.cursor()


        if ans == '1':
            play_music("asset/music/01.mp3")
            cur.execute("update options set value = 1 where id = 3")
            con.commit()
        if ans == '2':
            play_music("asset/music/02.mp3")
            cur.execute("update options set value = 2 where id = 3")
            con.commit()
        if ans == '3':
            play_music("asset/music/03.mp3")
            cur.execute("update options set value = 3 where id = 3")
            con.commit()
        if ans == '4':
            play_music("asset/music/04.mp3")
            cur.execute("update options set value = 4 where id = 3")
            con.commit()
        if ans == '5':
            play_music("asset/music/05.mp3")
            cur.execute("update options set value = 5 where id = 3")
            con.commit()            
        if ans == '6':
            play_music("asset/music/06.mp3")
            cur.execute("update options set value = 6 where id = 3")
            con.commit()
        if ans == '7':
            play_music("asset/music/07.mp3")
            cur.execute("update options set value = 7 where id = 3")
            con.commit()
        
        if ans == '0':
            return
        
def play_music(mp3File,vol=.1):
    import pygame
    
    pygame.mixer.init()
    pygame.mixer.music.load(mp3File)
    pygame.mixer.music.set_volume(vol)
    pygame.mixer.music.play(-1)

def music_toggle():
    import pygame
    pygame.mixer.music.stop()

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
    new_volume = max(0.0, current_volume - 0.1)
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
    
    import cursor, sqlite3
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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
        
        # Print Choices
        if result_title[0] == 0:
            console.print("([red]1[/red]) Show Intro (Currently: [red]Off[/red])")
        else:
            console.print("([red]1[/red]) Show Intro (Currently: [green]On[/green])")

        if result_music[0] == 1:            
            console.print("([red]2[/red]) Play Music (Currently: [green]On[/green])",end="")
        else:    
            console.print("([red]2[/red]) Play Music (Currently: [red]Off[/red])" ,end="")
        
        console.print("   ([red]- / +[/red]) Lower / Raise Volume")
        console.print("([red]3[/red]) Game Information")
        console.print("([red]4[/red]) Music Player")
        console.print("([red]5[/red]) Return")

        cursor.hide()
        ans = choice_getch()

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
                musictrack = 'asset/music/'+str(music_selected)+'.mp3'
                play_music(musictrack)            
        
        elif ans == '3':
            gameinfo()
        
        elif ans == '4':
            music()
        
        elif ans == '5':
            break
        elif ans == '-':
            music_lower()
        elif ans == '+' or ans == '=':
            music_raise()    
    
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
    import cursor
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '3':
            break
        
def display_score(hero):
    import cursor
    from rich.console import Console, Theme
    
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    while True:
        clear_screen()
        filetitle="asset/art/score.dat"
        data = ''
        console.print("[yellow]"+loadart(filetitle, data)+"[/yellow]\n")
        hero_status_bar(hero)
        console.print("Luck: " + str(hero[0].luck),)
        console.print("Status: ", end="")
        if hero[0].stat == 1:
            console.print("Normal")
        elif hero[0].stat == 0:
            console.print("Dead")
        elif hero[0].stat == 2:
            console.print("Poisoned")

        cursor.hide()
        choice_getch()
        break
    
def spellbook():
    import os, cursor
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

    cursor.hide()
    choice_getch()
    
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
    import cursor
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '1':
            grid_mover(hero)
        
        if ans == '2':
            break
        
def temple(hero):
    import cursor
    from rich.console import Console, Theme
    
    while True:
        clear_screen()
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

        cursor.hide()
        ans = choice_getch()

        # Run Choices
        if ans == '3':
            break

def enemy_generator(hero_level):
    import random
    from functions.classes import monster
    
    enemy_current = monster('',0,0,0,0,0,0,0,0,0,0)
    
    enemy_list1 = ['Goblin','Hobgoblin','Orc','Orc Warrior','Orc Shaman','Skeleton','Zombie','Ghoul','Wraith','Bandit','Bandit Leader','Wolf','Dire Wolf','Spider','Giant Spider','Slime','Ogre','Troll','Giant','Dark Knight']
    
    enemy_list2 = ['Lizardman','Lizard Warrior','Lizard Shaman','Giant Lizardman','Giant Lizard Warrior','Giant Lizard Shaman',
                   'Kobold','Kobold Warrior','Kobold Shaman','Giant Kobold Warrior','Giant Kobold Shaman',
                   'Gnoll','Gnoll Warrior','Gnoll Shaman','Gnoll Chieftain',
                   'Harpy', 'Basilisk', 'Minotaur', 'Cyclops', 'Wyvern', 'Manticore', 'Hydra', 'Chimera', 'Griffin']
    
    enemy_list3 = ['Demon','Imp','Succubus','Barghest','Shadow Demon','Vrock','Hezrou','Glabrezu','Nalfeshnee','Balor'] 
    
    if hero_level >= 5:
        enemy_list1.extend(enemy_list2)
    if hero_level >= 10:
        enemy_list1.extend(enemy_list3)
  
    enemy_current.name = random.choice(enemy_list1)
    enemy_current.level = hero_level + random.randint(1,3)
    enemy_current.hp = random.randint(1,(hero_level+5)) * enemy_current.level
    enemy_current.hp_max = enemy_current.hp
    enemy_current.luck = random.randint(0,3)
    enemy_current.mod = random.randint(1,4)
    enemy_current.ac = random.randint(5,15)
    enemy_current.stat = 1  # 1=Normal 0=Dead 2
    enemy_current.DEF_b = 1
    enemy_current.DEF_m = 1
    enemy_current.DEF_s = 1
    
    return enemy_current

def choice_getch():
    import sys
    if sys.platform.startswith('win'):
        try:
            import msvcrt
            return msvcrt.getch().decode('utf-8')
        except:
            return
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def save_game(hero):
    import sqlite3
    
    # Save data to database file:
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("""
        UPDATE hero SET 
            name = ?, 
            hp = ?, 
            hp_max = ?, 
            luck = ?, 
            DEF_m = ?, 
            DEF_s = ?, 
            DEF_b = ?, 
            level = ?, 
            mod = ?, 
            exp = ?, 
            stat = ?, 
            gold = ?
    """, (
        hero[0].name,
        hero[0].hp,
        hero[0].hp_max,
        hero[0].luck,
        hero[0].DEF_m,
        hero[0].DEF_s,
        hero[0].DEF_b,
        hero[0].level,
        hero[0].mod,
        hero[0].exp,
        hero[0].stat,
        hero[0].gold
    ))
    
    # Save equipped armor and weapon
    cur.execute("UPDATE equipment SET armor = ?, weapon = ?", (hero[1].id, hero[2].id))
    
    con.commit()
    con.close()
    
    return

def load_game():
    import sqlite3
    
    # Load data from database file:
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    result = cur.execute("select name,hp,hp_max,luck,DEF_m,DEF_s,DEF_b,level,mod,exp,stat,gold from hero").fetchone()
    resultplayer = player(*result)
    result_a = cur.execute("select armor from equipment").fetchone()    
    result_w = cur.execute("select weapon from equipment").fetchone()

    if result_a[0] == '1': result_armor = tunic
    if result_a[0] == '2': result_armor = leather_armor
    if result_a[0] == '3': result_armor = studded_leather
    if result_a[0] == '4': result_armor = chain_mail
    if result_a[0] == '5': result_armor = scale_mail
    if result_a[0] == '6': result_armor = plate_mail

    if result_w[0] == '7': result_weapon = hands
    if result_w[0] == '8': result_weapon = dagger
    if result_w[0] == '9': result_weapon = short_sword
    if result_w[0] == '10': result_weapon = long_sword
    if result_w[0] == '11': result_weapon = greatsword
    if result_w[0] == '12': result_weapon = club
    if result_w[0] == '13': result_weapon = mace
    if result_w[0] == '14': result_weapon = warhammer
    
    hero = [resultplayer, result_armor, result_weapon]
    con.close()
    
    return hero

def grid_mover(hero):
    import os
    import msvcrt
    from rich.console import Console, Theme
    import random


    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    
    width, height = 12, 12
    
    first_visit = True
    
    map_batch1 = [map_grid1, map_grid2, map_grid3, map_grid4]
    
    # Start with the first map in the batch
    current_map_index = 0

    if hero[0].level >= 1 and hero[0].level <= 10:
        map_grid = map_batch1[current_map_index]
        level_text = "Level 1"
        floor_text = "Floor "
    
    
    last_move = None  # Track last move direction

    while True:
        # Set avatar_location based on last move
        if last_move == "down":
            # Prefer "↑" as starting location when coming from below
            up_found = False
            for row_idx, row in enumerate(map_grid):
                for col_idx, cell in enumerate(row):
                    if cell == "↑":
                        avatar_location = (row_idx, col_idx)
                        up_found = True
                        break
                if up_found:
                    break
            else:
                # Fallback to "E" if no "↑" found
                for row_idx, row in enumerate(map_grid):
                    for col_idx, cell in enumerate(row):
                        if cell == "E":
                            avatar_location = (row_idx, col_idx)
                            break
                    else:
                        continue
                    break
 
        if last_move == "up":
            # Prefer "↑" as starting location when coming from below
            down_found = False
            for row_idx, row in enumerate(map_grid):
                for col_idx, cell in enumerate(row):
                    if cell == "↓":
                        avatar_location = (row_idx, col_idx)
                        down_found = True
                        break
                if down_found:
                    break
            else:
                # Fallback to "E" if no "↑" found
                for row_idx, row in enumerate(map_grid):
                    for col_idx, cell in enumerate(row):
                        if cell == "E":
                            avatar_location = (row_idx, col_idx)
                            break
                    else:
                        continue
                    break
        if last_move == None:
            # Always start on the first "E" in the map
            for row_idx, row in enumerate(map_grid):
                for col_idx, cell in enumerate(row):
                    if cell == "E":
                        avatar_location = (row_idx, col_idx)
                        break
                else:
                    continue
                break
                    
        while True:
            os.system('cls')
            # Print the map with avatar
            for row_idx, row in enumerate(map_grid):
                line = ""
                for col_idx, cell in enumerate(row):                    
                    if (row_idx, col_idx) == avatar_location:
                        line += "[green]@[/green] "
                    else:
                        if cell == "E":
                            line += "[red]"+ cell + "[/red] "
                        elif cell == "↑":
                            line += "[yellow]"+ cell + "[/yellow] "
                        elif cell == "↓":
                            line += "[blue]"+ cell + "[/blue] "
                        else:
                            line += cell + " "
                        
                console.print(line)

            console.print("\n                    ", level_text, floor_text, current_map_index + 1)
            console.print("[orange]LEGEND ------------------------------")
            console.print("[orange]|[/orange] [red]E[/red]: Gate Entrance    [green]@[/green]: Hero       [orange]|")
            console.print("[orange]|[/orange] [blue]↓[/blue]: Down Floor       [yellow]↑[/yellow]: Up Floor   [orange]|")
            console.print("[orange]-------------------------------------")
            console.print("[green]Move with Arrow Keys (← ↑ → ↓)[/green]")
            key = msvcrt.getch()
            if key == b'i':
                inventory(hero)
            if key == b'\xe0':  # Arrow key prefix
                arrow = msvcrt.getch()
                x, y = avatar_location
                new_x, new_y = x, y
                if arrow == b'M':     # Right arrow
                    new_y = y + 1
                elif arrow == b'K':   # Left arrow
                    new_y = y - 1
                elif arrow == b'H':   # Up arrow
                    new_x = x - 1
                elif arrow == b'P':   # Down arrow
                    new_x = x + 1
                # Check for wall and boundaries
                if (0 <= new_x < height and 0 <= new_y < width):
                    next_cell = map_grid[new_x][new_y]
                    if next_cell == "E":
                        avatar_location = (new_x, new_y)
                        return
                    elif next_cell == "↑":
                        # Move to next map in batch (cycle if at end)
                        current_map_index = (current_map_index + 1) % len(map_batch1)
                        map_grid = map_batch1[current_map_index]
                        first_visit = False
                        last_move = "up"
                        break  # Break inner loop to restart with new map
                    elif next_cell == "↓":
                        # Move to previous map in batch (cycle if at start)
                        current_map_index = (current_map_index - 1) % len(map_batch1)
                        map_grid = map_batch1[current_map_index]
                        last_move = "down"
                        break  # Break inner loop to restart with new map
                    elif next_cell != "#":
                        avatar_location = (new_x, new_y)
                    
                    # # Random encounter: 5% chance
                    # if random.random() < 0.05:
                    #     battle_seq(hero)
                    
        # Outer loop continues with new map

    return
