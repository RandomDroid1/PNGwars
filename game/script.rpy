# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sv = Character("Secretary Vinick")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office:
        zoom .5
        xpos -400
        ypos -500

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vinick idle:
        xalign 0.5
        yalign 0.35

    # These display lines of dialogue.

    sv "Hello! You're the one from the University of Mew-tah? Correct?"
menu:
    "Yes, I am":
        jump game_continue
    
    "No, I am not":
        sv "well, I think you took a real wrong turn, and should probably get out."
        return

label game_continue:


    sv "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
