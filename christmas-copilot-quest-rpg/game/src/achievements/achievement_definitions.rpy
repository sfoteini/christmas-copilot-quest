init python:
    """
    Variables for the player's achievements that should be initialized at the start of the game.
    """

    from store.achievement_enumerations import AchievementTitle

    # Initialize the player's achievements if they have not been initialized yet
    if persistent.achievements is None:
        persistent.achievements = set()

    # Define the total number of achievements that the player can unlock
    num_achievements = len(AchievementTitle)
