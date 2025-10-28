label lietold_jamesmeowdisan: # First Draft
    hide mosk
    hide garn
    show bg dogcampentrance:
        reset
        xoffset -200
        yoffset -600
        zoom .4
    nar "You trail behind Sobaka, keep your head down and maybe everything will be fine."
    nar "You look up to see a sprawling city, almost everywhere you look, theres movement."
    nar "As you walk in, flanked by two high ranking military members, that movement begins to still as heads turn toward you, and whispers spread through a small, but growing, crowd."
    nar "They don't look hostile, but theres a lot of them, and they are all much larger than you"
    jump demo_exit
    $ fast_end = True
label lietold_truthtold:
    jump demo_exit
    $ fast_end = True
label lietold_espionage: # First draft
    hide mosk
    hide garn
    show bg dogcampentrance:
        reset
        xoffset -200
        yoffset -600
        zoom .4
    jump demo_exit
label truthtold_spunky:
    $ fast_end = True
    jump demo_exit
label truthtold_calm: # First draft
    hide mosk
    hide garn
    show bg dogcampentrance:
        reset
        xoffset -200
        yoffset -600
        zoom .4
    nar "You trail behind Sobaka and Garner, hoping that by keeping your head down, everything will be fine" # they trust you to follow them in this one
    nar "Eventually you have to look up, and before you lays a sprawling city. At every turn and bank, theres movement"
    if garn_hurt == False:
        nar "As you walk in trailing two high ranking members of the military, you see curious stares begin to land on you"
    else:
        nar "As you walk in trailing two high ranking members of the military -- one having a nasty cut across his face -- you see curious stares land on you." #oh man I want to use emdashes but will they think I am robot man
    nar "They don't look hostile, and they seem to keep their distance from you, most seem eager to return to whatever they were doing beforehand."
    nar "Sobaka takes a look back at you..."
    if garn_hurt == True:
        mosk "We're going to get you... and Garner... some medical attention. "
    else:
        mosk "We're going to get you some medical attention. You look like you need it."
    show bg doctorsoffice: # HOW DID I FORGET THIS IM GOING TO CRASH OUT SO MUCH GOSH DARN IT
        ypos 300
    show caine sit: # hes kind of uncanny, why does he look like that? 
        zoom 1.4
        xpos 500
        ypos 300
    cain "Hm... you seem almost perfectly fine. Truthfully, I did not expect that considering everything."
    cain "In most circumstances I'd keep you for observation, but you have a lot of people who want to talk to you"
    cain "So I'm clearing you to leave. Do return if you feel any pain, light-headedness, or general issues with your head"
    jump demo_exit
return