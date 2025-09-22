# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
    # Meta Characters
define player = Character("[name]", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
define nar = Character("Narrative Ender", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
    # Ameowican Characters
define vini = Character("Secretary Meowstrong", window_background=Image("textboxameowican.png")) 
define cali = Character("Cali Meowford", window_background=Image("textboxameowican.png"))

# Establishes the movie
image launch = Movie(play="movies/Pngwars Backgrounds.webm", pos=(10, 10), anchor=(0, 0)) 
 

# The game starts here.

label start:

    # This launches the Start background and plays it
    show launch
    nar "Hello."
    nar "It's good to see you here. {p}You might imagine that I have some questions for you."
    nar "Let's start with something basic, you are Ameowican. Where are you from?"
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
        $ state = "Mew York"
        jump start_continue 
    "I am not from any of these places.":
        nar "Yes you are."
        jump state

# Collects name info
label start_continue:
    nar "[state]. Interesting. {p}Lets continue, what is your name? We only need your first."
    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Josh Meowman"

    if name.lower() in ("whattah", "aidan", "djroxalot", "devin", "killeville", "amber", "bbq", "burger", "bbq burger", "jbowler12", "jacob", "potatojay", "ryder", "daniel"): # looks case insensitively
        $ bbq = True
        nar "...[name]? [name]?? Oh man your playing this game. Go message BBQ about it or something. {p}Okay, well go continue I guess. This is scary. (If you weren't from bbq you just caught a crazy stray)"
 
    else:
        nar "... {p=2}[name], good luck, we may never see eachother again after this."
 

    with Dissolve(1)
    pause .5
    show bg white # PLACEHOLDER // This background will give a fade to white and then a fade to the new scene
    pause .5
    with Dissolve(1)
    jump true_start
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

    if name.lower() == "vinick":
        vini "Hello! Your name, your name... is Vinick? What a interesting coincidence. You're the one from the University of [state]?"
    elif name == "goob":
        vini "Hello! Your name... why?"
    else:
        vini "Hello! You are [name], I believe? You're that one from the University of [state]. It's nice to see you here, and if I may assume you are unsure as to why you were called here?"

menu wawa:
    # keeps Vinicks text on screen

    "'No, I wasn't actually told why the President called me here.'":
        player "No, I wasn't actually told why the President called me here."
    
    "'Actually, I was told why the President called me here'":
        vini "Oh. That... you shouldn't have been told that already, it was pretty damn classified. {p} When you get back, i'm going to have a number for you to call, and your going to tell them who told you"

    "Use the BBQ blast" if name == "whattah":
        color "#7dcfffff"
        vini "wawawawaw"
label game_continue:
    show vinick lookup:
        yalign 0.15
        zoom .8
    vini "Well, we've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
    his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
    on his desk, by the way."

    pause .5

    # Introduces the President
        # PLACEHOLDER // Door open noise

    hide vinick # PLACEHOLDER // Text doesn't look right, check if functional later

    show bg ovalofficeoverlook:
        yalign .5
        zoom 1

    show cali lookback :
        yalign .5
        xalign .4

    cali "What a meeting. {p=3}you sure those ones were from Congress?"
    vini "Yes sir, they were. We have the-"
    show cali sit:
        zoom .8
    if (GameCompletions == 1):
        cali "Ah {w=1} I assume this is the one from [state]? Welcome to... Have you been here before? You don't have that... bit of wonder even the most powerful have when seeing this room."
        cali "... Nah, i'm probably just going crazy in my old age. You have an important reason to have been called here today!"
    else:
        cali "Ah {p}  I assume this is the one from [state]? Well, welcome to D.C., I assume this is your first visit here? 
            You have a very important reason for being here." # add secret dialogue if you've beaten the game before
    cali "This hasn't hit the news yet, but 3 days ago the country of Pnglandia split into 4 factions. Each with warring interests and ideals"
    cali "We... truthfully don't know too much about each faction. All of our resources are focused on... {w=2} other countries." # This dialogue sucks so bad god help me
    cali "That's where you come in, [name]. You will be on a flight to PNGlandia before the sun sets, and you will arrive around dawn. "
    show cali sidelay
    cali "Now, we need you to try and get them to agree on some stuff, {w=2} or at least tell us who to give {i}limited{/i} military assistance to."
    cali "Are you ready for this?"
    menu presidentquestion:
        "Yes Sir.":
            cali "Thats what I like to hear, we need more people like you in our government."
            cali "We don't have much for you in the way of a briefing, but we can get you on a plane in 1 hour."
        "That sounds like something I can do.":
            jump true_start
        "Why don't you send a trained negotiator?":
            cali "We... have all of our negotiators working on some more underground deals with some folks from other countries"
            cali "Anyway, they've requested someone who hasn't been in the DC system a long time. So we did some research, and landed on you."
            cali "We can get you on a plane in one hour, do you accept?"
        "I can't do that.":
            cali "That was an answer we thought about. Especially considering how secretive we were about the whole thing."
            cali "However, it might be worth reconsidering... theres a lot on the line."
            cali "We know you are capable of this. {p=3}It'd would be a damn shame if you backed out now." 
        
    # This ends the game.

    return
