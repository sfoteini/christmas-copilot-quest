init 1 python in character_utils:
    """
    Utility functions for managing characters in the game.
    """

    import renpy.store

    def determine_player_name(player_input: str) -> str:
        """
        Determines the player's name based on the input provided by the player and the default character name.
        If the player input is empty, the default character name is used.

        :param player_input: The input provided by the player.

        :return: The player's name.
        """
        return player_input.strip() or renpy.store.character_name

    def initialize_character_variables(character_name: str, character_image: str) -> None:
        """
        Initializes the character variables with the provided character name and image.

        :param character_name: The name of the character.
        :param character_image: The image of the character.
        """
        renpy.store.character_name = character_name
        renpy.store.character_image = character_image

    def initialize_variables_for_noelle() -> None:
        """
        Initializes the variables for the character Noelle.
        """
        initialize_character_variables("Noelle", "noelle")

    def initialize_variables_for_malik() -> None:
        """
        Initializes the variables for the character Malik.
        """
        initialize_character_variables("Malik", "malik")

    def initialize_variables_for_carey() -> None:
        """
        Initializes the variables for the character Carey.
        """
        initialize_character_variables("Carey", "carey")
