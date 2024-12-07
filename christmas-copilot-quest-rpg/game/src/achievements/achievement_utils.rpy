init 1 python:
    """
    Utility functions for managing achievements in the game.
    """

    from store.achievement_enumerations import AchievementTitle

    def add_achievement_and_display_notification(achievement_title: AchievementTitle) -> None:
        """
        Adds an achievement to the player's set of unlocked achievements and displays a notification to the player.

        :param achievement_title: The title of the achievement to add.
        """
        add_achievement(achievement_title)
        display_achievement_unlocked_notification(achievement_title)

    def add_achievement(achievement_title: AchievementTitle) -> None:
        """
        Adds an achievement to the player's set of unlocked achievements.

        :param achievement_title: The title of the achievement to add.
        """
        persistent.achievements.add(achievement_title.value)

    def display_achievement_unlocked_notification(achievement_title: AchievementTitle) -> None:
        """
        Displays a notification to the player when they unlock an achievement.

        :param achievement_title: The title of the achievement that was unlocked.
        """
        num_achievements_unlocked = get_number_of_unlocked_achievements()
        renpy.call_screen(
            'achievement_unlocked_notification',
            achievement_title.value,
            num_achievements_unlocked,
            num_achievements,
        )

    def get_number_of_unlocked_achievements() -> int:
        """
        Returns the number of achievements that the player has unlocked.

        :return: The number of achievements that the player has unlocked.
        """
        return len(persistent.achievements)
