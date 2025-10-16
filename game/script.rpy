# Structure of textbox image names "textbox_(Faction)_(Rank)(Any Other Details)"
# character name structures (4 letters of first name)(1 letter of last name)(vini, cali, mosk, garn made before this)
# Meta Characters
define player = Character("[name]", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))
define nar = Character("Narrator", window_background=Frame("narbox.png"), namebox_background=Frame("narname.png"))

# Ameowican Characters
define vini = Character("Vinick Meowsker", window_background=Image("textbox_ameowican_secretaryofstate.png"), namebox_background=Frame("namebox_ameowican.png")) 
define cali = Character("Cali Meowford", window_background=Image("textbox_ameowican_president.png"), namebox_background=Frame("namebox_ameowican.png"))

# Animal Characters
# Dog Characters
define mosk = Character("Mischa Sobaka", window_background=Image("textbox_animal_dog.png"), namebox_background=Frame("namebox_dog.png"))
define garn = Character("Sloan Garner", window_background=Image("textbox_animal_dog.png"), namebox_background=Frame("namebox_dog.png")) 
define varam = Character ("Plankton from spongebob")
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
default window_icon = "standard"
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
    $ window_icon = "office"
    nar "How cool, you get to choose what state you're from. Big choice, think carefully"
    $ window_icon = "forest"
# This determines what state the character is from. It will unlock blue options later
    hide img ameowica
menu state:
    "I am from Mew-tah.":
        play sound "click.wav"
        $ state = "Mew-tah"
        jump start_continue
    "I am from Meow-izona.":
        play sound "click.wav"
        $ state = "Meow-izona"
        jump start_continue        
    "I am from Alaskat":
        play sound "click.wav"
        $ state = "Alas-kat"
        jump start_continue
    "I am from Meowyland":
        play sound "click.wav"
        $ state = "Meowyland"
        jump start_continue     
    "I am from Mew York": # PLACEHOLDER // This is where parthenon is, maybe make a reference at that?
        play sound "click.wav"
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
    elif name.lower() in ("wawa"):
        nar "... {p=2}[name], that's a good choice. It was also the name used for the development of most of this game. Rainworld fan spotted"
    else:
        nar "... {p=2}[name], that's a good choice."

    nar "Now, do you want to know a bit more about how this game works (I'd encourage this)"
    menu game_tutorial:
        "Yeah, I'd like to know more":
            play sound "click.wav"
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
            nar "Also this is Super-Duper early access, and I hope to have this fixed by the time I ship it properly"
            show img attributions
            nar "Moving on, this is the attributions screen. I also spent hours on it, but this one works"
            nar "However be warned, it's a bit laggy, and has spoilers!"
            nar "But also, this game was only possible because all these people decided to upload images that anyone can use, for free."
            nar "So I'd check at least some of them out."
            hide img attributions
            nar "Well, that's it. You are ready to start!"
        "No, I'm ready":
            play sound "click.wav"
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
        alpha .2
        xalign 0.5
        yalign 0.35
        linear .3 alpha 1
    $ metvini = True
    $ clearnotebook = False
    if name.lower() == "vinick": # Just in case they name themselves Vinick
        vini "Hello! Your name, your name... is Vinick? What a interesting coincidence. You're the one from the University of [state]?"
    elif name == "goob": # The True name.
        vini "Hello! Your name... why?"
    elif name == "2149-0403":
        nar "You've entered a dev skip name, go back if unintended"
        jump jet_plane_crash
    else:
        vini "Hello! You are [name], I believe? You're that one from the University of [state]. It's nice to see you here, and if I may assume you are unsure as to why you were called here?"

menu wawa: # Why is this menu named this?
    "'No, I wasn't actually told why the President called me here.'":
        play sound "click.wav"
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
        play sound "click.wav"
        $ knew_before = True
        player "Actually, I was told about why I'm here."
        vini "Well, that's interesting... Any chance you'll tell me who told you?"
        player "No sir."
        vini "Well, that... You know what, nope. It's not my problem, I've got other things to deal with"
        show vinick idle:
            yzoom 1
            parallel:
                linear .2 yzoom 1.5
            parallel:
                linear .2 yoffset -200
        jump game_continue
    
    "{color=#F54927}(State) Use the BBQ blast{/color}" if name == "whattah":
        play sound "click.wav"
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
        vini "Oh, and your still getting the whole thing explained to you by President Meowford, you don't get out of it that easy." # This guy hates you fr. I Can't decide if he hates his job or not though
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
        

    cali "What a meeting. Vinick, are you sure those ones were from Congress?"
    vini "Yes sir, they were. We have the-"
  
    show cali lookback:
        linear .1 yzoom 1.1
    pause .1    
    show cali sit:
        zoom .8
        yzoom 1.2
        linear .1 yzoom 1
        alpha 1
    cali "Ah, is this the one from [state]? I'd been wondering when their flight would come in. Well, [name], welcome to the White House, It's a very lovely place.{p=2}We'll have to get you a tour once you get back"
menu meowford_rhetorical:
    "Thank you. I imag- Wait... What do you mean when I get back?": # Channel your inner Cal Bradford
        $ calirep += 1
        cali "I was wondering when you'd pick up on that. Sounds like your already pretty good at listening to what people are saying. {w=3} That's good. You're going to need that"
        cali "Let's start at the beginning. 3 days ago, the country of Png-landia dissolved their government, and split into 4 factions, each with warring interests and different ideals"
        cali "Truthfully, we don't know all too much beyond that, our intelligence services are focused on.... {w=4} other countries"
        cali "I shouldn't have to explain to you that this is a big problem, especially once the press gets a hold of it in a few days. Ameowica has vested interests in the success of Png-landia, or at least the stability of it"
        cali "Not to mention it's not good for me politically if one of our allies collapses under my watch, but that parts less your problem and more mine" # holy yapathon
        cali "I should get to the point... The four factions will only let us send a negotiator if it's someone who hasn't been in the DC system for all that long. That, combined with other factors, led us to start doing some scouting"
        cali "Eventually Vinick started looking at your college, asking around, seeing who'd be a good fit." # establishes that it was Vinick who chose you... maybe it wasn't as much of a coincidence as it sounds like. I feel like Vinick is evil, I really do. Wait I'm the game dev I decide
        cali "Your name began to come up, some Political Science teachers mention you, a few clubs too. So Vinick made a few calls, and then we called you."
        cali "And now your here, with the opportunity of a lifetime in front of you."
        cali "Will you accept our offer to be the official ambassador of the United States of Ameowica to the PNG-landia factions. We can get you on a plane in an hour, just say {color=#00A36C}{i}yes.{/i}{/color}"
        jump main_continue
    "Thank you. I imagine it is, and I'll be looking forward to that":
        $ calirep -= 1
        cali "Really, your not going to... You're going to have to get better at listening to conversations, especially with what we've got planned for you. Where'd you find this one Vinick?"
        cali "I had a whole bit going, whatever."
        cali "Let's start at the beginning. 3 days ago, the country of Png-landia,{w=2} you know that one, right? Of course you do. Well, it's government dissolved, very suddenly" # buddy is a little petty
        cali "We've no idea why yet. Our resources are spread very thin with the state of the world already, and we haven't had the time to get that info out of them, to tell you the truth" # he sounds depressed now that you messed up the course of his speech poor cat he doesn't even know his secretary of state is evil. I want Vinick to be somewhat responsible for the state of the world
        cali "They also don't want to talk to anyone thats been in the DC system for that long. They almost hung up on me, and as the leader of the free world, I can say that is one of the first times thats happened" # Just like his namesake cal bradford (this is nothin glike the plot of paradise Im just saying things)
        cali "So, what we needed was a negotiator who wasn't in the DC system, who wouldn't demand too much info beforehand or now, and who would be capable of it"
        cali "So we started scourting colleges. Eventually Vinick landed on your college, he asked around... {w=3} time and time again we'd here your name be mentioned"
        cali "So he made some calls, and eventually we called you. Your first test was actually agreeing to the flight, I know a lot of people might not have"
        cali "But you did, and now you've ended up here"
        cali "So... Will you accept our offer, and be the first official ambassador of the United States of America to the Png-landia factions. C'mon, we can get you on a plane in an hour, just say {color=#00A36C}{i}yes.{/i}{/color}"
        jump main_continue
label main_continue:
    menu presidentquestion:
        "Yes Sir. I accept your offer": # choice 1,  very positive
            play sound "click.wav"
            $ calirep += 2
            show bg ovalofficeoverlook: # Cali Transition
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
                linear .2 alpha 1 # end of cali Transition
            pause .2
            cali "Theres the good news I needed. We will get you everything you need for your trip, please... request anything we miss"
            cali "We don't have much for you in the way of a briefing, which I imagine you might have figured out already"
            cali "You are now the sole US ambassador to PNGlandia, congrats."
            if calirep == 3:
                cali "good luck, I mean it. I'm not just saying that, I really think you can do some good stuff out there."
                jump jet_plane
            else:
                jump jet_plane
        "That sounds like something I can do.": # choice 1 variation basically
            show bg ovalofficeoverlook: # Cali Transition
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
                linear .2 alpha 1 # end of cali Transition
            play sound "click.wav"
            $ calirep += 1
            cali "That's good, that's what we want to hear."
            cali "Truthfully, we've not got much for you in terms of a briefing, {p=3}but we can get you on a plane in a few hours"
            cali "We'll get you on a plane in an hour, you'll be given everything you need for your trip"
        "Why don't you send a trained negotiator?": # a bit more skeptical, can lead you either way
            show bg ovalofficeoverlook: # Cali Transition
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
                linear .2 alpha 1 # end of cali Transition
            play sound "click.wav"
            cali "We... have all of our negotiators working on some more deals with some folks from other countries."
            cali "You are... our most qualified option. At least the only one we can get without screwing up some other deal"
            if calirep == -1:
                cali "Anyway, you seem... clever enough... {w=2}Nah, I'm kidding, you seem pretty smart."
            else:
                cali "Anyway, you seem pretty clever, I hope anyway. Clever enough to be picked out in a competition you didn't even know you were in"
            cali "So that brings us right back around, do you accept our offer?" 
            menu presidentsubquestion:
                "Yes. I accept.":
                    play sound "click.wav"
                    player "Yes, I accept."
                    cali "That's the news we needed"
                    cali "You'll be on a plane in an hour, we'll get you everything you need." #hmmmm, hes a little angry after having to think about how bad the world is. We aint elaborating though
                    jump jet_plane
                "No, get someone qualified.":
                    play sound "click.wav"
                    player "No... No, get someone qualified, i'm hardly qualified."
                    cali "You..."
                    pause 1
                    cali "Okay... well. Not much we can do about that then. Security will see you out."
                    # PLACEHOLDER // Link this to the I can't do that option??
                    cali "Thats... do we have a next on the list? Please tell me we have a next on the list, Vinick."
                    return
        "I can't do that.": # negative choice
            show bg ovalofficeoverlook: # Cali Transition
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
                linear .2 alpha 1 # end of cali Transition
            play sound "click.wav"
            $ calirep -= 3 # You shouldn't have made me beg, John.
            cali "That... was an answer we'd thought about, especially considering how little we told you"
            cali "But please reconsider, theres a... lot more depending on this than you realize"
            cali "Enough to get the leader of the free world to beg, which is more than most world leaders could get" 
            cali "We know your capable of this, even if you don't. So if you can't trust yourself, trust us. Trust me."
            menu: # sub-choice of negative choice, chance to go back
                "No. I'm sure, I don't want to do this.":
                    play sound "click.wav"
                    show cali sit
                    cali "Alright. Security will escort you out soon"
                    cali "Vinick, can we... get the next person on the list."
                    return
                "I'm... No, I can do this. Get me on the plane.":
                    play sound "click.wav"
                    show cali sit
                    cali "Theres hope for you yet. We can have you on a plane in an hour."
                    cali "Security will escort you to the Roosevelt room. You'll get everything you need."
                    jump jet_plane
label jet_plane: # The plane sequence that leads into
    play music "motif.mp3"
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
    nar "The flight is completely empty aside from you. You were on the only Ameowican flight allowed to cross into Pnglandia Airspace"
    nar "The Pnglandia Government dissolving had hit the news sooner than the President expected. He had an absolutely disasterous press conference you got to watch as you waited to board"
    nar "You wonder if that bodes well for the quality of the intelligence the US has on this.{p=3}Or maybe you don't, i'm not in charge of you."
    nar "You have an hour and a half until you touch down on the airport closest to the Pnglandia capitol, what do you want to do?"
    menu plane_choice: # The illusion of choice hahaha
        "Sleep":
            play sound "click.wav"
            nar "You let your eyes shut as you drift to sleep."
            nar "It's nice to get some rest before..."
            jump jet_plane_crash
        "Watch a show":
            play sound "click.wav"
            nar "You turn on you favorite show, 'The Mewsroom', and sit back."
            nar "Soon, you begin to feel your eyes drift shut"
            nar "Maybe it's a good idea to get some rest before..."
            jump jet_plane_crash
        "Watch the news":
            play sound "click.wav"
            # PLACEHOLDER // Maybe give them a variable for being studious that like... blue options.
            nar "You turn on the news, and sit back"
            nar "It's probably a good idea to get an idea of just how bad the current geopolitical climate before you go in and try to negotiate a treaty"
            nar "However despite your best efforts, after half an hour you begin to feel drowsy"
            nar "Soon, you begin to feel your eyes drift shut"
            nar "Maybe it's a good idea to get some rest before..."
            # PLACEHOLDER // add this background later
            jump jet_plane_crash

label jet_plane_crash:
    play music "planetense.ogg"
    show bg planewindow1:
        zoom .8
        xalign 0.5 ypos 400
    nar "You hear a loud bang from somewhere on your right. As you turn to look..."
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
    stop music
    play sound "planecrash.wav" # This is one of the funniest sound effects I've heard. It's so goofy its so so goofy. It just keeps going oh my god
    # PLACEHOLDER // ALARM BELLS, BABIES CRYING, WAAH WAAH WAAH, CARS CRASHING, PANDEMONIUM, WEEWOO WEEWOO, REPORTING LIVE FROM THE SCENE
    # PLACEHOLDER // Have it be fuzzy, a bit of them wavy lines. My mans got concuss ):
    mosk "What the hell was- They actually went down?"
    # PLACEHOLDER // Buzzy sound effects, make the text box blur and shake. The text is from a different dog saying this cats the sole survivor.
    garn "Both pilots are dead... The plane hit the ground nose first, there was no surviving that for them."
    garn "We have a survivor in the cabin! Looks like they might've been the only one in there..."
    mosk "Well, it looks like this plane didn't listen. {w=1} We have a survivor, and no other bodies."
    mosk "They're one of those damn cats. Grab them, lets see what a 'commerical' jet was doing over a no fly zone."
    nar "You feel yourself begin to wake up"
    show concussion:
        linear .5 alpha 0
    pause .5
    hide concussion
    play music "Jungle.mp3"
    show bg forest1:
        zoom 1
        xalign 0
        ypos 600
    menu dog_scary:
        "Stay limp, pretend you are unconscious":  # Option One, Neutral
            play sound "click.wav"
            hide concussion with dissolve
            mosk "Lets go. Theres no one else here to save."
            garn "Sir, we shouldn't take them back to our camp. There is no way a completely empty commercial flight just... crashes here."
            mosk "So what are you suggesting, then? The Ameowicans intentionally crashed a plane... to get access to the medical wing of our camp?"
            garn "No... but it's far too convenient. We need to keep them under guard, at- at least two, around the clock"
            mosk "There we go, that's better. We can bring them to Caine, he has some good medical equipment" # a little bit of teaching from Mischa here
            jump demo_exit
        "Wake up and fight! These dogs don't seem too friendly.": # Option Two, The Negative option, garner won't like you after this
            # Not Revamped, small edits done.
            play sound "click.wav"
            hide concussion with dissolve
            $ animalrep -= 1
            $ dogrep -= 2
            $ garnrep -= -2
            $ garn_hurt = True
            player "you twist around to smack the dog holding you with your claws"
            show bg forest1 with vpunch
            show garn standalert:
                ypos 600
                xpos 1000
                linear .3 yoffset -300
            show bg forest1:
                linear .3 yoffset -300
            pause 1
            garn "you BASTARD"
            garn "I'm going to-"
            show garn standalert:
                parallel:
                    linear .5 xalign .3
                parallel:
                    linear .5 zoom .8
            # PLACEHOLDER // find some way to make it clear Garner makes a go at you. Initialize a battle UI?
            show mosk stand:
                xalign 1
                yoffset 300
                linear .5 xalign .7    
            mosk "Hold on!"
            mosk "Let's see what they have to say for themselves."
            show mosk stand: #experiment with this type of dual dialogue system since their dialogue boxes are really similar
                linear .3 zoom .8
            show garn standalert:
                linear .3 zoom 1
            garn "Sir, we can't assume they have any good intentions. Especially if their first instict is to fight"
            show mosk stand:
                linear .3 zoom 1
            show garn standalert:
                linear .3 zoom .8
            mosk "We won't be, but look at how small they are. Do you think they are in any position to be much of a threat?"
            show mosk stand:
                linear .3 zoom .8
            show garn standalert:
                linear .3 zoom 1
            garn "No sir. They aren't."
            show mosk stand:
                linear .3 zoom 1
            show garn standalert:
                linear .3 zoom .8
            mosk "So, let's give them a chance. Cat, who are you?"
            # PLACEHOLDER // IMPORTANT // THIS NEEDS TO LINK SOMEWHERE ELSE EVENTUALLY. // Does it? Check back later.
            jump wake_up_calm_dog_confrontation
        "Wake up, but stay calm. These are the ones your supposed to be negotiating with, after all": # Option 3, the good option
            # Not Revamped
            play sound "click.wav"
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

menu wake_up_calm_dog_confrontation: # continues from the players meeting with the dog where they wake up and calmly expain
                "Lie: I'm just a random cat! I was on the flight before I heard about the split":
                    # Not Revamped
                    play sound "click.wav"
                    player "Look, I'm just so-some random cat. {w=1} I got on the flight before I heard about the split!"
                    $ moskrep -= 2
                    $ dogrep -= 1
                    $ animalrep -= 1
                    mosk "So... you, a random cat... Got on a commercial flight, and at least from what we can tell completely alone aside from one pilot"
                    mosk "Then your flight went into a pretty strict no-fly zone, and presumably planned to land "
                    mosk "So... either your lying to me, or you are one oblivious cat who managed to make their way here."
                    mosk "Personally, I think your lying. {w=1}So let's try that again, who are you, and what is your name"
                    menu mosk_who_are_you_really: # gives you the chance to double down or back out.
                        "Lie: My name is James Meowdisan. I just wanted to take a vacation.":
                            play sound "click.wav"
                            $ moskrep -= 1
                            mosk "Alright 'James'. Let's bring you back to camp, we can get your identity confirmed there, right?"
                            mosk "Follow us, wandering around the forest isn't very safe nowadays. We wouldn't want anything bad to happen to you"
                            jump lietold_jamesmeowdisan
                        "Truth: My name is [name]. I'm an ambassador from the United States of Ameowica.":
                            play sound "click.wav"
                            $ moskrep += 1
                            mosk "Thats better. At the very least it's more believable. {p=3}So, an Ameowican Ambassador crashes into our territory right after our country splits."
                            mosk "That's... at the very best unfortunate for you, assuming your telling the truth.{p=3}Luckily, i'd like to say you crashed in the right place."
                            mosk "Follow us. Believe me, you'll fare better than if you run around the forest alone."
                            jump lietold_truthtold
                    # PLACEHOLDER // Need continues
                "Lie: I'm one of yours! You hired me to tell you what the cats were up to!":
                    # Not Revamped
                    play sound "click.wav"
                    $ garnrep -= 2
                    $ moskrep -= 2
                    $ dogrep -= 2
                    $ animalrep -= 1 # you making some crazy enemies
                    # they hate this more than the lie about being someone random because you are pretending to be one of the
                    player "Okay! Okay! Look, I'm one of yours, you hired me to tell you what the cats were up to!"
                    mosk "Who hired you?"
                    player "They didn't tell me their name! Okay?"
                    garn "Captain, it's obvious their lying, I say we-"
                    mosk "I don't disagree with you. But why not bring them back to camp?"
                    mosk "Let's see how truthful they're being about this whole spy thing."
                    jump lietold_espionage
                    # PLACEHOLDER // Need continues

                "Truth: I'm an Ambassador from the United States of Ameowica! Let me go!":
                    # Not Revamped
                    play sound "click.wav"
                    $ moskrep += 1
                    $ garnrep += 1 #you get a rep boost in this one because garn likes your spunk
                    $ animalrep += 1
                    $ dogrep += 2
                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "What, they're sending fiesty children to negotiate in other countries now?"
                    garn "What an absolutely pathetic display, how do you expec-"
                    mosk "Wait just a second Garner, let's give this cat a {i}small{/i}chance. {w=3} They just got out of a plane crash, they are probably pretty injured beyond the adrenaline keeping them running."
                    mosk "Follow us. Not like you have much of a choice. These forests aren't safe nowadays."
                    # PLACEHOLDER // Need continues
                    jump truthtold_spunky
                "Truth: I'm an Ambassador from the United States of Ameowica. I don't want trouble, I'm here to help.":
                    # Not Revamped
                    play sound "click.wav"
                    $ moskrep += 1
                    $ animalrep += 1
                    $ dogrep += 2 # A small reward for choosing the peaceful option. 
                    garn "An Ambassador from Ameowica? How entertaining."
                    garn "They're sending children to try and fix other countries business now?"
                    garn "Absolutely patheti-"
                    mosk "Hold on Garner, let's give them {i}some{/i} kind of chance, they just survived a plane crash, {w=3} I imagine they might have some kind of concussion"
                    mosk "You're going to want to follow us. Much safer than wandering into those woods alone. We can also give you medical help, for free."
                    jump truthtold_calm