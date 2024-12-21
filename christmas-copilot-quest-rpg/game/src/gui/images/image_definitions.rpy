init python:
    """
    Definitions for the images used in the game.
    """

    # Define the default background image for the game and variations with overlays
    renpy.image("game_background", "gui/game_menu.png")
    renpy.image("game_background white70", Composite(
        (1920, 1080),
        (0, 0), 'game_background',
        (0, 0), '#ffffffb3')
    )
    renpy.image("game_background white80", Composite(
        (1920, 1080),
        (0, 0), 'game_background',
        (0, 0), '#ffffffcc')
    )
