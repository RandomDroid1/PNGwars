label demo_exit:
    show bg DemoBackground
    show dev sit:
        parallel:
            linear 1 xoffset 300
            linear 1 xoffset -300
            repeat
        parallel:
            linear 1 yoffset 300
            linear 1 yoffset -300
    player "Hello! As you might have anticipated, this screen means you've reached the end of the demo."
    player "It's not a super long game yet, but it's coming together."
    player "I hope you enjoyed it so far though."
    player "Oh and fun fact, if you poke around the files there are some note pages that have spoilers (and just general facts), so if you want that, it's there"
    player "Okay, well, see you."
    return