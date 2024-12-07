# The achievements screen displays the achievements that the player has unlocked in the game.
# The screen is displayed in the game menu.
screen achievements():
    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "achievements"

        vbox:
            spacing 50

            vbox:
                spacing 15

                for achievement in achievement_enumerations.AchievementTitle:
                    if is_achievement_unlocked(achievement):
                        text '{icon=unlock} [achievement.value!t]'
                    else:
                        text _('{icon=lock} ? ? ?'):
                            color gui.insensitive_color

            $ num_achievements_unlocked = get_number_of_unlocked_achievements()
            text _('{icon=award} Number of Achievements Unlocked: [num_achievements_unlocked] / [num_achievements]')
