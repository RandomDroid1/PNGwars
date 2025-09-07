# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define sv = Character("Secretary Vinick")

# Establishes the movie


# The game starts here.

label start:
 
    scene bg office:
        zoom .5
        xpos -400
        ypos -500
    # This shows Secretary of State Vinicks character
    show vinick idle:
        xalign 0.5
        yalign 0.35

# probably go about adding something before this, the starts a touch too sudden
    
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
    
    show vinick lookup:
        yalign 0.15
        zoom .8
    sv "Well, we've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
    his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
    on his desk, by the way.,"

# This jumps you to the bathroom.
    
    # This ends the game.

    return
