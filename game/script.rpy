# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define sv = Character("Secretary Vinick")
define nar = Character("", window_background=Frame("narbox.png"))
# Establishes the movie
image launch = Movie(play="movies/Pngwars Backgrounds.webm", pos=(10, 10), anchor=(0, 0)) 
 

# The game starts here.

label start:
    # This launches the Start background and plays it
    
    show launch
    nar "Hello."
    nar "It's good to see you here. {p}You might imagine that I have some questions for you."
    nar "Let's start with something basic, where are you from?"
menu:
    "I am from Mew-tah.":
        $ state = "Mew-tah"
        jump start_continue
    "I am from Meow-izona.":
        $ state = "Meow-izona"
        jump start_continue        
    "I am from Meow-izona.":
        $ state = "Meow-izona"
        jump start_continue         
label start_continue:
    nar "test [state]"
# This shows Secretary of State Vinicks character


# True starting zone
label true_start: 
    show vinick idle:
        xalign 0.5
        yalign 0.35
   
    sv "Hello! You're the one from the University of Mew-tah? Correct?"


menu:
    # keeps Vinicks text on screen
    sv "Hello! You're the one from the University of Mew-tah? Correct?"
     
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
