# The Oblivion Cycle - Chapter I: The Shimmering Gate
# (C)opyright 2024 RLM Productions

import sqlite3, os
from rich.console import Console
from rich.theme import Theme
from functions.variables import *
from functions.gameFunctions import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Temp Skip Here
# l.adventuremenu()

# Read Game Options from database
con = sqlite3.connect('data.db')
cur = con.cursor()
result_music = cur.execute("select value from options where id = 1").fetchone() # 0 music is Off 1 is on
result_musictrack = cur.execute("select value from options where id = 3").fetchone() # music choice
result_title = cur.execute("select value from options where id = 2").fetchone() # 0 is show title 1 is skip

if result_music[0] == 1: # Check for Music
    music_selected = f'{result_musictrack[0]:02d}' # Convert to 2 digits if 1
    musictrack = 'asset/music/'+str(music_selected)+'.ogg'
    if music_selected == '11' or music_selected == '12':
        play_music(musictrack, .3) # play tracks 11 and 12 softer
    else:
        play_music(musictrack) # play Music 

if result_title[0] == 1: # Check for Intro
    intro()

### Main Menu ###
def main():
    while True:
        clear_screen()
        filetitle = 'asset/art/title.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[red]"+loadart(filetitle, data)+"[/red]")
        console.print("                          Chapter I: The Shimmering Gate")
        console.print('')

        # Print Choices
        console.print("([red]1[/red]) Play Game")
        console.print("([red]2[/red]) New Game")
        console.print("([red]3[/red]) Game Options")
        console.print("([red]4[/red]) Quit Game")
        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '2':
            createhero()
        elif ans == '1':
            adventuremenu()
        elif ans == '3':
            gameoptions()
        elif ans == '4':
            break

    ### EXIT CODE ###
    #close DB
    con.close()
    clear_screen()
    delay_print2("\nThank you for playing The Oblivion Cycle.\n")
    
if __name__ == "__main__":
    main()