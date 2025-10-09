# Structure of textbox image names "textbox(Faction)_(Rank)(Any Other Details)"
# character name structures (4 letters of first name)(1 letter of last name)(vini, cali, mosk, garn made before this)
# Meta Characters
define player = Character("[name]", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
define nar = Character("Narrative Ender", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))

# Ameowican Characters
define vini = Character("Secretary Meowstrong", window_background=Image("textboxameowican.png")) 
define cali = Character("Cali Meowford", window_background=Image("textboxameowican.png"))

# Animal Characters
# Dog Characters
define mosk = Character("Mischa Sobaka")
define garn = Character("Sloan Garner") 
define varam = Character ("Varash Moskvi")
# Establishes the movie
image launch = Movie(play="movies/Pngwars Backgrounds.webm", pos=(10, 10), anchor=(0, 0)) 
image concussion = Movie(play="movies/concussionstatic.webm", pos=(10, 10), anchor=(0, 0))
# Establishes variables
# Notebook/Met
default clearnotebook = True
default metvini = False
# Faction Reputations
default dogrep = 0
default animalrep = 0

# Personal Reputations
default calirep = 0
default garnrep = 0
default moskrep = 0

# Other
default knew_before = False
default garn_hurt = False
# The game starts here.

label start:
    play music "aura.mp3"
    # This launches the Start background and plays it
    show launch
    nar "Hello."
    nar "It's good to see you here. {p}You might imagine that I have some questions for you."
    show img ameowica:
        zoom 2
        yalign .25
        xalign .5
        rotate -90
    nar "Let's start with something basic, you are Ameowican."
    nar "How cool, you get to choose what state you're from. Big choice, think carefully"
# This determines what state the character is from. It will unlock blue options later
    hide img ameowica
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
    "I am from Mew York": # PLACEHOLDER // This is where parthenon is, maybe make a reference at that?
        $ state = "Mew York"
        jump start_continue 

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

    nar "Now, do you want to know a bit more about how this game works (I'd encourage this)"
    menu game_tutorial:
        "Yeah, I'd like to know more":
            nar "Awesome. So, you see this cool thing"
            show img variable:
                zoom 2
                yalign .5
                xalign .5
            nar "This is a variable, very cool, very useful. It's what lets the game remember your decisions. For example, I know your from [state]."
            nar "But theres something extra it does in this game on top of that"
            show img redoption:
                yalign .5
                xalign .5
            nar "These are red options! They are exclusive options unlocked by doing or selecting specific things."
            nar "At the start of them, you'll see some text in parentheses. This denotes why you are getting the special option."
            nar "For example, this red option has (state) before it, which means the state you selected is what unlocked this option for you"
            show img notebook:
                yalign .3
                zoom .75
            nar "This is the notebook tab. It's evil"
            nar "No, im not kidding. its broken, it'll crash your game"
            nar "Now, if you are wondering why I left it in the game...{w=3} I spent hours on it and don't want to have wasted all that time"
            show img attributions
            nar "Moving on, this is the attributions screen. I also spent hours on it, but this one works"
            nar "However be warned, it's a bit laggy, and has spoilers!"
            nar "But also, this game was only possible because all these people decided to upload images that anyone can use, for free."
            nar "So I'd check at least some of them out."
            hide img attributions
            nar "Well, that's it. You are ready to start!"
        "No, I'm ready":
            nar "If you're sure... See you later then"
            $ metvini == False
 
    hide launch
    jump true_start
# True starting zone
label true_start: 
    play music "pink.mp3"
    scene bg office: # Shows the oval office
        zoom .5
        xpos -400
        ypos -500
    player "One week ago, you recieved a call from the White House. They'd said something about having scouted you for a new position"
    player "You hadn't believed it was real at first, but now here you are. In the oval office"
    player "In front of you, is Secretary of State Vinick Meowstrong"
    
    # Shows Vinick   
    show vinick idle:
        xalign 0.5
        yalign 0.35
    $ metvini = True
    $ clearnotebook = False
    if name.lower() == "vinick": # Just in case they name themselves Vinick
        vini "Hello! Your name, your name... is Vinick? What a interesting coincidence. You're the one from the University of [state]?"
    elif name == "goob": # The True name
        vini "Hello! Your name... why?"
    else:
        vini "Hello! You are [name], I believe? You're that one from the University of [state]. It's nice to see you here, and if I may assume you are unsure as to why you were called here?"

menu wawa: # Why is this menu named this?
    "'No, I wasn't actually told why the President called me here.'":
        $ knew_before = False
        player "No, I wasn't actually told why the President called me here."
        show vinick idle:
            yzoom 1
            parallel:
                linear .2 yzoom 1.5
            parallel:
                linear .2 yoffset -200
        jump game_continue
    
    "'Actually, I was told why the President called me here'":
        $ knew_before = True
        player "Actually, I was told about why I'm here."
        vini "Well, that's interesting."
        vini "I imagine you won't tell me who told you, so that's hardly my problem"
        show vinick idle:
            yzoom 1
            parallel:
                linear .2 yzoom 1.5
            parallel:
                linear .2 yoffset -200
        jump game_continue
    
    "{color=#F54927}(State) Use the BBQ blast{/color}" if name == "whattah":
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
    if (knew_before == False):
        vini "Well, don't worry, you shouldn't have been told. We've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
        his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
        on his desk, by the way."
    else:
        vini "That is much more a job for the NSA than for me. Either way, we've been waiting for you. {color=#FF4D29}The President{/color} will arrive back from
        his meeting soon, something about the budget, nothing you need to care about. {p=3}Don't tell him I was laying
        on his desk, by the way."
        vini "Oh, and your still getting the whole thing explained, you don't get out of it that easy."
    show vinick lookup:
        linear .2 alpha 0
    show bg office: # The first transition animation for the oval office + cali
        xoffset 0
        parallel:
            linear .2 xoffset -400  
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
        alpha 1
    cali "Oh, is this the one from [state]?{p=3}Well, welcome to D.C. You have a very important reason for being here."
    cali "This hasn't hit the news yet, but 3 days ago the country of Pnglandia split into 4 factions. Each with warring interests and ideals"
    cali "We... truthfully don't know too much about each faction. All of our resources are focused on... {w=4} other countries." # This dialogue sucks so bad god help me
    cali "That's where you come in, [name]. You will be on a flight to PNGlandia before the sun sets, and you will arrive around dawn. "
    show bg ovalofficeoverlook:
        parallel:
            linear .2 xoffset -200  
        parallel:
            linear .2  xzoom 1.1  
    show cali sit:
        alpha 1
        linear .2 alpha 0
    pause .2
    show bg ovalofficesit:
        xoffset -400
        yzoom .8
        xzoom 1
        parallel:
            linear .1 xzoom .8
        parallel:
            linear .1 xoffset -100
    show cali sidelay:
        rotate 0
        xoffset 400
        zoom 1
        alpha 0
        linear .2 alpha 1
    pause .2
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
                    player "Yes, I accept."
                    jump jet_plane
                "No, get someone qualified.":
                    player "No... No, get someone qualified, i'm hardly qualified."
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
        zoom 1.5
        xpos 0 ypos 0
        pause 1.0
        parallel:
            linear 3 zoom .9
        parallel:
            linear 3 xpos -300
        parallel:
            linear 3 ypos -300
    show planescreen cali_jet_report # PLACEHOLDER
    player "The plane is relatively empty. A vast majority of flights to PNGlandia had been grounded, and the only reason this one is still flying to PNGlandia is because the President ordered it."
    player "All this stuff had hit the news sooner than the president expected, his press conference was pretty clearly prepared on a moments notice" # PLACEHOLDER // Put an image of that poor dishelveled calico on screen. maybe on like the plane screen
    player "You wonder if that bodes well for the quality of the intelligence the US has on this.{p=3}Or maybe you don't, i'm not in charge of you."
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
        zoom .8
        xalign 0.5 ypos 400
    player "You look out the window, and for just a moment, wonder why the pilot is flying so low, and why the turbulence was so bad."
    show bg black:
        zoom 20
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
    show concussion:
        linear .5 alpha 0
    pause .5
    hide concussion
    show bg forest1:
        zoom 1
        xalign 0
        ypos 600
    menu dog_scary:
        "Stay limp, pretend you are unconscious":  # Option One, Neutral
            hide concussion with dissolve
            mosk "Lets go."
        "Wake up and fight! These dogs don't seem too friendly.": # Option Two, The Negative option, garner won't like you after this
            hide concussion with dissolve
            $ animalrep -= 1
            $ dogrep -= 2
            $ garnrep -= -2
            $ garn_hurt = True
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
                linear .2 yoffset -600
            pause .2
            show bg forest1 with vpunch
            show bg forest1 with vpunch
            # PLACEHOLDER // Need continues
            mosk "The cat awakes! Who are you, small one?"
            show bg forest1:
                xpan 0
                linear 2 xpan 180
            pause 1
            show mosk stand:
                yalign .4
                xpos 2000
                linear 1 xoffset -1200
            pause 1
            # PLACEHOLDER // see if you can make this timed?
            jump wake_up_calm_dog_confrontation

menu wake_up_calm_dog_confrontation: # continues from the players meeting with the dog where they wake up and calmly explain
                "Lie: I'm just a random cat! I was on the flight before I heard about the split":
                    player "Look, I'm just so-some random cat. {w=1} I got on the flight before I heard about the split!"
                    $ moskrep -= 2
                    $ dogrep -= 1
                    $ animalrep -= 1
                    mosk "Your Ameowican, I presume... {w=3} Your flight would've taken, what? 2 hours to get here."
                    mosk "The news broke 3 hours ago, and a vast majority of flights here were cancelled."
                    mosk "So... either your lying to me, or you are one oblivious cat who managed to make their way here."
                    mosk "Personally, I think your lying. {w=1}So let's try that again, who are you, and what is your name"
                    menu mosk_who_are_you_really: # gives you the chance to double down or back out.
                        "Lie: My name is James Meowsidan. I just wanted to take a vacation.":
                            $ moskrep -= 1
                            mosk "Alright 'James'. Let's bring you back to camp, we can get your identity confirmed there, right?"
                            jump lietold_jamesmeowdisan
                        "Truth: My name is [name]. I'm an ambassador from the United States of Ameowica.":
                            $ moskrep += 1
                            mosk "Thats better. So, an Ameowican Ambassador crashes into our territory right after our country splits."
                            mosk "That's... at the very best unfortunate for you, assuming your telling the truth.{p=3}Luckily, i'd like to say you crashed in the right place."
                            mosk "Follow us. Believe me, you'll fare better than if you run around the forest alone."
                            jump lietold_truthtold
                    # PLACEHOLDER // Need continues
                "Lie: I'm one of yours! You hired me to tell you what the cats were up to!":
                    $ garnrep -= 2
                    $ moskrep -= 2
                    $ dogrep -= 2
                    $ animalrep -= 1
                    # they hate this more than the lie about being someone random because you are pretending to be one of the
                    player "Okay! Okay! Look, I'm one of yours, you hired me to tell you what the cats were up to!"
                    mosk "Who hired you?"
                    player "They didn't tell me their name! Okay?"
                    garn "Captain, it's obvious their lying, I say we-"
                    mosk "I don't disagree with you, but whats the harm in taking them back to camp."
                    mosk "See how truthful they're being about this whole spy thing"
                    jump lietold_espionage
                    # PLACEHOLDER // Need continues

                "Truth: I'm an Ambassador from the United States of Ameowica! Let me go!":
                    $ moskrep += 1
                    $ garnrep += 1 #you get a rep boost in this one because garn likes your spunk
                    $ animalrep += 1
                    $ dogrep += 2
                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "What, they're sending fiesty children to negotiate in other countries now?"
                    garn "What an absolutely pathetic display, how do you expec-"
                    mosk "Wait just a second Garner, let's give this cat a {i}small{/i}chance. {w=3} They just got out of a plane crash, they might be injured"
                    mosk "Follow us. Not like you have much of a choice. These forests aren't safe nowadays."
                    # PLACEHOLDER // Need continues
                    jump truthtold_spunky
                "Truth: I'm an Ambassador from the United States of Ameowica. I don't want trouble, I'm here to help.":
                    $ moskrep += 1
                    $ animalrep += 1
                    $ dogrep += 2 # A small reward for choosing the peaceful option. 
                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "They're sending children to try and fix other countries business now?"
                    garn "Absolutely patheti-"
                    mosk "Hold on Garner, let's give them {i}some{/i} kind of chance, they just survived a plane crash, {w=3} I imagine they might have some kind of concussion"
                    mosk "You're going to want to follow us. Much safer than wandering into those woods alone. We can also give you medical help, for free."
                    jump truthtold_calm