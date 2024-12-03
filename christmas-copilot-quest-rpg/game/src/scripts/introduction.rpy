label introduction:
    show felix

    felix "Ah, you must be the new coder Santa called for! What's your name?"

    $ player_input = renpy.input(
        _("(Type your name and press Enter, or press Enter to use the default name, [character_name].)")
    )
    $ player_name = character_utils.determine_player_name(player_input)

    felix "Nice to meet you, [player_name]!"
    felix "It's December, and the North Pole is buzzing with activity. We're working hard to get all 
        the toys ready for Christmas. But there's a problem..."
    felix "The toy tracking system is down! We can't keep track of the toys we're making, and we're falling 
        behind schedule. Santa needs your help to fix it!"
    felix "So, are you ready to help us save Christmas?"

    player "Yes, I'm ready!"

    felix "Great! We need to build a quick toy tracking system to get us through the holiday season."
    felix "You have 3 days to develop a temporary solution that will allow us to track the toys we're making."

    player "Ah, I'm not sure I can do that in 3 days..."

    felix "Don't worry, you won't be alone! Our AI assistant, GitHub Copilot, will help you along the way."

    menu:
        felix "Are you ready to get started?"

        "I guess I have no choice... Let's do this!":
            jump set_up_project
