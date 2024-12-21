label ending:
    scene game_background white80 with dissolve
    pause 1
    show text _("{size=48}Thanks for playing {b}Christmas Copilot Quest{/b}!\n\n[gui.about_intro!t]{/size}")
    with dissolve
    show screen ctc() # click to continue
    pause
    hide text with dissolve
