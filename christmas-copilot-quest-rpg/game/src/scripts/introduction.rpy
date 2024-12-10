label introduction:
    scene company_bg with dissolve
    show felix with dissolve

    felix "Ah, you must be the new coder Santa called for! What's your name?"

    $ player_input = renpy.input(
        _("(Type your name and press Enter, or press Enter to use the default name, [character_name].)")
    )
    $ player_name = character_utils.determine_player_name(player_input)

    player "I'm [player_name]."

    felix "Nice to meet you, [player_name]! I'm Felix, a senior Software Engineer here at Santa's Lab."

    player "Nice to meet you too, Felix! It looks like a busy time here at the North Pole."

    felix "It's December, and we're working hard to get all the toys ready for Christmas. But there's a problem..."
    felix "The toy tracking system is down! We can't keep track of the toys we're making, and we're falling 
        behind schedule. Santa needs your help to fix it!"
    felix "So, are you ready to help us save Christmas?"

    player "Yes, I'm ready to help!"

    felix "Great! We need to build a quick toy tracking system to get us through the holiday season."
    felix "Santa understands there isn't much time for a fancy interface, but he stresses that the application
        must be reliable and easy to use."

    player "How much time do we have to build this system?"

    felix "We have a tight deadline of 3 days to create a temporary toy tracking system."

    player "Three days? That sounds impossible..."

    felix "Don't worry, you'll have some help. We'll be using GitHub Copilot, an AI-powered coding assistant, 
        to speed up the development process."

    menu:
        felix "Are you ready to get started?"

        "I guess I have no choice... Let's do this!":
            jump set_up_project
