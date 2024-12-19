# The extra content screen displays the extra content that the player can access in the game, such as achievements
# and learning resources. The screen is displayed in the game menu.
screen extra_content():
    tag menu

    use game_menu(_("Extra Content"), scroll="viewport"):
        style_prefix "extra_content"

        vbox:
            spacing 20

            label _("Elf's Hub")
            textbutton _("{icon=award} Achievements") action ShowMenu("achievements")
            textbutton _("{icon=book} Learning Hub") action ShowMenu("learning_hub")

            null height 20
            label _("Behind the Code")
            textbutton _("{icon=github} Check out the Source Code on GitHub") action OpenURL("https://github.com/sfoteini/christmas-copilot-quest")
            # TODO Add link to the blog post


# The achievements screen displays the achievements that the player has unlocked in the game.
# The screen is displayed in the game menu.
screen achievements():
    tag menu

    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "achievements"

        vbox:
            spacing 50

            vbox:
                spacing 20

                for achievement in achievement_enumerations.AchievementTitle:
                    hbox:
                        spacing 10

                        if is_achievement_unlocked(achievement):
                            text _("{icon=unlock}")
                            text _("[achievement.value!t]")
                        else:
                            text _("{icon=lock}"):
                                color gui.insensitive_color
                            text "? ? ?":
                                color gui.insensitive_color

            $ num_achievements_unlocked = get_number_of_unlocked_achievements()
            text _("Number of Achievements Unlocked: [num_achievements_unlocked] / [num_achievements]")


# The learning hub screen displays links to learning resources about GitHub Copilot.
# The screen is displayed in the game menu.
screen learning_hub():
    tag menu

    use game_menu(_("Learning Hub"), scroll="viewport"):
        style_prefix "learning_hub"

        vbox:
            spacing 20

            label _("Documentation")
            textbutton _("{icon=bookmark} GitHub Copilot Documentation") action OpenURL("https://docs.github.com/copilot")
            textbutton _("{icon=bookmark} GitHub Copilot Chat Cookbook") action OpenURL("https://docs.github.com/copilot/example-prompts-for-github-copilot-chat")

            null height 20
            label _("Microsoft Learn Learning Paths")
            textbutton _("{icon=bookmark} GitHub Copilot Fundamentals") action OpenURL("https://learn.microsoft.com/training/paths/copilot?wt.mc_id=AI-MVP-5004971")
            textbutton _("{icon=bookmark} Accelerate app development by using GitHub Copilot") action OpenURL("https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot?wt.mc_id=AI-MVP-5004971")
            textbutton _("{icon=bookmark} GitHub Foundations") action OpenURL("https://learn.microsoft.com/training/paths/github-foundations?wt.mc_id=AI-MVP-5004971")

            null height 20
            label _("GitHub Copilot in Visual Studio Code")
            textbutton _("{icon=bookmark} Get started with GitHub Copilot in VS Code") action OpenURL("https://code.visualstudio.com/docs/copilot/overview")
            textbutton _("{icon=github} GitHub Copilot extension for VS Code") action OpenURL("https://marketplace.visualstudio.com/items?itemName=GitHub.copilot")
