# Structure of textbox image names "textbox(Faction)_(Rank)(Any Other Details)"
# Meta Characters
define player = Character("[name]", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
define nar = Character("Narrative Ender", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))

# Ameowican Characters
define vini = Character("Secretary Meowstrong", window_background=Image("textboxameowican.png")) 
define cali = Character("Cali Meowford", window_background=Image("textboxameowican.png"))

# Animal Characters
# Dog Characters
define mosk = Character("Mischa Moskvi")
define garn = Character("Sloan Garner") 
# Establishes the movie
image launch = Movie(play="movies/Pngwars Backgrounds.webm", pos=(10, 10), anchor=(0, 0)) 
image concussion = Movie(play="movies/concussionstatic.webm", pos=(10, 10), anchor=(0, 0))
# Establishes variables
# Faction Reputations
default dogrep = 0
default animalrep = 0

# Personal Reputations
default calirep = 0
default garnrep = 0
default moskrep = 0
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
        nar "... {p=2}[name], that's a good choice."

    
    
 

    with Dissolve(1)
    pause .5
    show bg white # PLACEHOLDER // This background will give a fade to white and then a fade to the new scene
    pause .5
    with Dissolve(1)
    hide launch
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
        show vinick idle:
            yzoom 1
            parallel:
                linear .2 yzoom 1.5
            parallel:
                linear .2 yoffset -200
        jump game_continue
    
    "'Actually, I was told why the President called me here'":
        vini "Oh. That... you shouldn't have been told that already, it was pretty damn classified. {p} When you get back, i'm going to have a number for you to call, and your going to tell them who told you"

    "{color=#0080c0}Use the BBQ blast{/color}" if name == "whattah":
        vini "wawawawaw"
        jump game_continue

label game_continue:
    pause .1
    show vinick lookup:
        yalign 0.15
        zoom .8    
        yzoom 1.4
        block:
            parallel:
                linear .2  yzoom 1
            parallel:
                linear .2  yoffset 25

    vini "Well, we've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
    his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
    on his desk, by the way."
    show vinick lookup:
        linear .2 alpha 0
    show bg office: # The first transition animation for the oval office + cali
        xoffset 0
        parallel:
            linear .2 xoffset -200  
        parallel:
            linear .2  xzoom 1.1  
    jump president_introduced

label president_introduced:
    pause .2
    hide vinick
    show bg ovalofficeoverlook: # The second transition animation for the oval office + cali
        zoom 1
        yalign .5
        xzoom 1.2
        parallel: 
            linear .2 xoffset 150
        parallel:
            linear .2 xzoom 1
    show cali lookback:
        alpha 0
        yalign .5
        xalign .4
        linear .2 alpha 1
        

    cali "What a meeting. {p=3}you sure those ones were from Congress?"
    vini "Yes sir, they were. We have the-"
  
    show cali lookback:
        linear .1 yzoom 1.1
    pause .1    
    show cali sit:
        zoom .8
        yzoom 1.2
        linear .1 yzoom 1
    cali "Oh, we have a visitor! I assume this is the one from [state]? {p=3} Well, welcome to D.C., I assume this is your first visit here? 
            You have a very important reason for being here." # add secret dialogue if you've beaten the game before
    cali "This hasn't hit the news yet, but 3 days ago the country of Pnglandia split into 4 factions. Each with warring interests and ideals"
    cali "We... truthfully don't know too much about each faction. All of our resources are focused on... {w=4} other countries." # This dialogue sucks so bad god help me
    cali "That's where you come in, [name]. You will be on a flight to PNGlandia before the sun sets, and you will arrive around dawn. "
    pause .5
    show bg ovalofficeoverlook:
        linear .5 xpan -10
    pause .5
    show bg ovalofficesit:
        xoffset -400
        zoom .8
    show cali sidelay:
        rotate 0
        xoffset 400
        zoom 1
    cali "Now, we need you to try and get them to agree on some stuff, {w=2} or at least tell us who to give {i}limited{/i} military assistance to."
    cali "Are you ready for this?"

    menu presidentquestion:
        "Yes Sir.": # choice 1,  very positive
            $ calirep += 2
            cali "Thats what I like to hear, we need more people like you in our government."
            cali "We don't have much for you in the way of a briefing, but we can get you on a plane in 1 hour."
            cali "You are now the sole US ambassador to PNGlandia, congrats."
            jump jet_plane
        "That sounds like something I can do.": # choice 1 variation basically
            $ calirep += 1
            cali "That's good, that's what we want to hear."
            cali "Truthfully, we've not much for you in terms of a briefing, {p=3}but we can get you on a ejnc f4"
        "Why don't you send a trained negotiator?": # a bit more skeptical, can lead you either way
            cali "We... have all of our negotiators working on some more underground deals with some folks from other countries"
            cali "Anyway, they've requested someone who hasn't been in the DC system a long time. So we did some research, and landed on you."
            cali "We can get you on a plane in one hour, do you accept?"
            menu presidentsubquestion:
                "Yes. I accept.":
                    jump jet_plane
                "No, get someone qualified.":
                    cali "You..."
                    jump jet_plane
        "I can't do that.": # negative choice
            $ calirep -= 2
            cali "That was an answer we thought about. Especially considering how secretive we were about the whole thing."
            cali "However, it might be worth reconsidering... theres a lot on the line."
            cali "We know you are capable of this. {w=2} would be a damn shame if you backed out now."
            cali "Are you sure you want to turn your back on what you can do?"
            menu: # sub-choice of negative choice, chance to go back
                "I am sure, I don't want to do this.":
                    show cali sit
                    cali "Okay. Vinick, sorry to put this job on you, escort this young fellow out for me."
                    cali "... You could've done so much more. Sorry it ended like this"
                    cali "hey, maybe we'll call you back for something some other day."
                    return
                "I'm... No, I can do this. Get me on the plane.":
                    show cali sit
                    cali "Theres hope for you yet. We can have you on a plane in a few hours."
                    cali "Vinick will lead you to the Roosevelt room, and before you know it, you will be the sole US ambassador to Pnglandia."
                    jump jet_plane
label jet_plane: # The plane sequence that leads into
    hide cali
    show bg planeseat1:
        zoom 1.0
        xpos 0 ypos 0
        pause 1.0
        parallel:
            linear 3 zoom .5
        parallel:
            linear 3 xpos -300
        parallel:
            linear 3 ypos -700
    show planescreen cali_jet_report # PLACEHOLDER
    player "The plane is relatively empty. Not many people want to go to PNGlandia, especially since the news of the faction splitting broke."
    player "It hit the news sooner than the president expected, he seemed quite unprepared in his press conference" # PLACEHOLDER // Put an image of that poor dishelveled calico on screen. maybe on like the plane screen
    player "You wonder if that bodes well for the quality of the intelligence the US has on this.{p=3} Or maybe you don't, i'm not in charge of you."
    player "You have about half an hour until you touch down on the airport closest to the PNGlandia capitol, what do you want to do?"
    menu plane_choice: # The illusion of choice hahaha
        "Sleep":
            player "You let your eyes shut as you drift to sleep."
            player "It's nice to get some rest before..."
            # PLACEHOLDER // add this background later
            jump jet_plane_crash
        "Watch a show":
            player "You turn on you favorite show, 'The Mewsroom', and sit back."
            show planescreen Mewsroom
            player "Soon, you begin to feel your eyes drift shut"
            player "Maybe it's a good idea to get some rest before..."
            # PLACEHOLDER // add this background later
            jump jet_plane_crash
        "Watch the news":
            show planescreen Mews
            # PLACEHOLDER // Maybe give them a variable for being studious that like... blue options.
            player "You turn on the news, and sit back"
            player "It's probably a good idea to get an idea of the current geopolitical climate before you go in and try to negotiate a treaty"
            player "However despite your best efforts, you begin to feel drowsy"
            player "Soon, you begin to feel your eyes drift shut"
            player "Maybe it's a good idea to get some rest before..."
            # PLACEHOLDER // add this background later
            jump jet_plane_crash

label jet_plane_crash:
    show bg planewindow1:
        zoom .6
        xpos 0 ypos -1000
    player"You look out the window, and for just a moment, wonder why the pilot is flying so low."
    show bg black
    pause .5
    show concussion:
        zoom 5
        xpos -50 ypos -50
        alpha .3
        parallel:
            linear 1 xpos 0
            linear 2 xpos -100
            zoom 6
            zoom 4
            repeat
        parallel:
            linear 1 ypos 0
            linear 2 ypos -100
            repeat
        parallel:
            linear 2 alpha .1
            linear 2 alpha .3
            repeat
    hide planescreen cali_jet_report
    # PLACEHOLDER // ALARM BELLS, BABIES CRYING, WAAH WAAH WAAH, CARS CRASHING, PANDEMONIUM, WEEWOO WEEWOO, REPORTING LIVE FROM THE SCENE
    # PLACEHOLDER // Have it be fuzzy, a bit of them wavy lines. My mans got concuss.
    mosk "Hey! Can we get some... The pilot's are dead."
    # PLACEHOLDER // Buzzy sound effects, make the text box blur and shake. The text is from a different dog saying this cats the sole survivor.
    garn "We have a survivor!"
    vara "Weren't all flights supposed to be grounded? They're shooting down anything they see!"
    garn "Well, it looks like this plane didn't listen. {w=1} We have a survivor, and no other bodies."
    mosk "They're one of those damn cats. Grab them, lets see what a 'commerical' jet was doing over our territory, risking getting shot down."
    player "You feel yourself begin to wake up"
    show bg forest1:
        zoom .5
        xpos -50
        ypos -350
    menu dog_scary:
        "Stay limp, pretend you are unconscious":  # Option One, Neutral
            mosk "Lets go." 
        "Wake up and fight! These dogs don't seem too friendly.": # Option Two, The Negative option, garner won't like you after this
            $ animalrep -= 1
            $ dogrep -= 2
            $ garnrep -= -2
            player "you twist around to smack the dog holding you with your claws"
            show garn standalert
            garn "you {cps=7}BASTARD{/cps}"
            garn "I'm going to-"
            # PLACEHOLDER // find some way to make it clear Garner makes a go at you. Initialize a battle UI?
            show battle garnui
            show mosk stand
            mosk "Hold on! Lets see why this one is here."
            # PLACEHOLDER // Need continues
        "Wake up, but stay calm. These are the ones your supposed to be negotiating with, after all": # Option 3, the good option
            player "Hey! Let me go... please."
            hide concussion with dissolve
            show bg forest1:
                ypos -350
                linear .2 ypos -600
            show bg forest1 with vpunch
            # PLACEHOLDER // Need continues
            mosk "The cat awakes! Who are you, small one?"
            show bg forest:
                xpan 0
                linear 2 xpan 50
            # PLACEHOLDER // see if you can make this timed?
            jump wake_up_calm_dog_confrontation

menu wake_up_calm_dog_confrontation: # continues from the players meeting with the dog where they wake up and calmly explain
                "Lie: I'm just a random cat! I was on the flight before I heard about the split":
                    player "Look, I'm just so-some random cat. {w=1} I got on the flight before I heard about the split!"
                    $ moskrep -= 2
                    $ dogrep -= 1
                    $ animalrep -= 1
                    mosk "Your Ameowican, I presume. {w=3} Your flight would've taken about 2 hours to get here."
                    mosk "The news broke 3 hours ago, and a vast majority of flights here were cancelled."
                    mosk "So... either your lying to me, or you are one oblivious cat who managed to make their way here."
                    mosk "Personally {w=2}, I think your lying. {w=1}So let's try that again, who are you, and what is your name"
                    menu mosk_who_are_you_really: # gives you the chance to double down or back out.
                        "Lie: My name is James Meowsidan. I just wanted to take a vacation.":
                            $ moskrep -= 1
                            mosk "Alright 'James'. Let's bring you back to camp, we can get your identity confirmed there, right?"

                        "Truth: My name is [name]. I'm an ambassador from the United States of Ameowica.":
                            $ moskrep += 1
                            mosk "Thats better. So, an Ameowican Ambassador crashes into our territory right after our country splits."
                            mosk "That's... at the very best unfortunate for you.{p=3}Luckily, i'd like to say you crashed in the right place."
                            mosk "Follow us. Believe me, you'll fare better than if you run around the forest alone."
                    jump wake_up_calm_dog_confrontation
                    # PLACEHOLDER // Need continues
                "Lie: I'm one of yours! You hired me to tell you what the cats were up to!":
                    jump wake_up_calm_dog_confrontation
                    # PLACEHOLDER // Need continues

                "Truth: I'm an Ambassador from the United States of Ameowica! Let me go!":

                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "What, they're sending fiesty children to negotiate in other countries now?"
                    garn "What an absolutely pathetic display, how do you expec-"
                    mosk "Wait just a second Garner, let's give this cat a {i}small{/i}chance. {w=3} They just got out of a plane crash, they might be injured"
                    mosk "Follow us. Not like you have much of a choice. These forests aren't safe nowadays."
                    # PLACEHOLDER // Need continues
                    jump wake_up_calm_dog_confrontation
                "Truth: I'm an Ambassador from the United States of Ameowica. I don't want trouble, I'm here to help.":
                    $ moskrep += 1
                    $ animalrep += 1
                    $ dogrep += 2 # A small reward for choosing the peaceful option. 
                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "They're sending children to try and fix other countries buisness now?"
                    garn "Absolutely patheti-"
                    mosk "Hold on Garner, let's give them {i}some{/i} kind of chance, they just survived a plane crash, {w=3} I imagine they might have some kind of concussion"
                    mosk "You're going to want to follow us. Much safer than wandering into those woods alone. We can also give you medical help, for free."
                    jump wake_up_calm_dog_confrontation  

return
