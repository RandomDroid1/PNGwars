# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sv = Character("Secretary Vinick")
define player = Character("[name]", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
define nar = Character("Narrative Ender", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
# Establishes the movie
image launch = Movie(play="movies/Pngwars Backgrounds.webm", pos=(10, 10), anchor=(0, 0)) 
 

# The game starts here.

label start:
    # This launches the Start background and plays it
    
    show launch
    nar "Hello."
    nar "It's good to see you here. {p}You might imagine that I have some questions for you."
    nar "Let's start with something basic, where are you from?"
# This determines what state the character is from. It will unlock blue options later
menu state:
    "I am from Mew-tah.":
        $ state = "Mew-tah"
        jump start_continue
    "I am from Meow-izona.":
        $ state = "Meow-izona"
        jump start_continue        
    "I am from Alaskat":
        $ state = "Alas-kat"
        jump start_continue
    "I am from Meowyland":
        $ state = "Meowyland"
        jump start_continue     
    "I am from Mew York":
        $ state = "Mew_York"
        jump start_continue 

# Collects name info
label start_continue:
    nar "[state]. Interesting. {p}Lets continue, what is your name? We only need your first."
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Josh Meowman"
        print(name)

    if name.lower in ("whattah", "aidan"): #Note, figure out how to case-insentitzes
        nar "I will turn on hard mode if you don't change that. Go fix that."
        jump start_continue
    else:
        nar "Falsed"
 

    with Dissolve(.5)
    pause .5
# True starting zone
label true_start: 
# This shows changes the background
    scene bg office:
        zoom .5
        xpos -400
        ypos -500
    
    # This shows Secretary of State Vinicks character    
    show vinick idle:
        xalign 0.5
        yalign 0.35
    with Dissolve(.5)

    if name == "vinick":
        sv "Hello! Your name, your name... is vinick? What a interesting coincidence. You're the one from the University of [state]?"
    elif name == "goob":
        sv "Hello! Your name"
    else:
        sv "Hello! Your name, your name... [name]. You're the one from the University of [state]? right? "

menu:
    # keeps Vinicks text on screen

    "Yes, I am":
        jump game_continue
    
    "No, I am not":
        sv "well, I think you took a real wrong turn, and should probably get out."
        return

label game_continue:
    $ renpy.movie_cutscene("movies/PNGWars Backgrounds.webm")
    show vinick lookup:
        yalign 0.15
        zoom .8
    sv "Well, we've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
    his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
    on his desk, by the way."

# This jumps you to the bathroom.
    
    # This ends the game.

    return
