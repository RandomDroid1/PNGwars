label pewter_meeting:
    show pewt walkglare:
        xoffset 200
        yoffset 300
        zoom 1.2
    pewt "Hello."
    pewt "... We don't see very many cats around here."
    pewt "... Well, I suppose theres a few scattered between the factions, but I know them well enought to tell you aren't one."
    pewt "So... you must be that Ameowican Ambassador I've been hearing about"
    pewt "You look... rough, why don't you come with me and we'll get you patched up."
    show elea swoon:
        zoom .7
        yalign .45
        xalign .8
        yoffset 100
    show bg meetingroom with dissolve:
        reset
        zoom .5
        xoffset -600
        yoffset -500
    elea "Hello... You're with Vinick?" # Foreshadowing that she is a part of the rebels, but keeping plausible deniability
    pewt "They're the representative Ameowica sent over."
    jump demo_exit