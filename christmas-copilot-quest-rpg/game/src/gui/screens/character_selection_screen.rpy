# TODO A simpler transform might be better
transform character_card_selection:
    on hover:
        easein 0.3 ypos 40
    on idle:
        easein 0.3 ypos 0


# The character selection screen allows the player to choose their preferred character from a list of available
# options. It is displayed when the player starts a new game.
screen character_selection_menu():
    tag character_selection_menu

    add "images/backgrounds/character_selection_screen.png"

    vbox:
        spacing 100
        xpos 160
        ypos 80

        # TODO Add better styling for the text
        text "Choose your character" size 50 color "#ffffff"

        hbox:
            spacing 125

            imagebutton:
                idle "images/characters/cards/noelle_card.png"
                hover "images/characters/cards/noelle_card.png"
                action [Function(character_utils.initialize_variables_for_noelle), Return()]
                at character_card_selection

            imagebutton:
                idle "images/characters/cards/malik_card.png"
                hover "images/characters/cards/malik_card.png"
                action [Function(character_utils.initialize_variables_for_malik), Return()]
                at character_card_selection

            imagebutton:
                idle "images/characters/cards/carey_card.png"
                hover "images/characters/cards/carey_card.png"
                action [Function(character_utils.initialize_variables_for_carey), Return()]
                at character_card_selection
