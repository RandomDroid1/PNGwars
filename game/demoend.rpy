label demo_exit:
    hide mosk
    hide garn
    hide pewt
    hide elea
    hide caine # is there a broad way to hide everything?
    show bg white:
        zoom 20
    player "Hello! As you might have anticipated, this screen means you've reached the end of the demo."
    if (fast_end == True):
        player "If your seeing this text, you got one of the earlier endings, and there is a decent amount more to look at."
        player "You were warned this game was early in development!"
    player "It's not a super long game yet, but it's coming together."
    player "I hope you enjoyed it so far though. This was my first interaction with Ren.py (and Python as a whole). It was very confusing but I've gotten the hang of it"
    player "Have a good day, and please return to this game one day since hopefully it will continue beyond this point."

return
