init 1 python in character_utils:
    import renpy.store

    def determine_player_name(player_input: str) -> str:
        """
        Determines the player's name based on the input provided by the player and the default character name.
        If the player input is empty, the default character name is used.

        :param player_input: The input provided by the player.

        :return: The player's name.
        """
        return player_input.strip() or renpy.store.character_name
