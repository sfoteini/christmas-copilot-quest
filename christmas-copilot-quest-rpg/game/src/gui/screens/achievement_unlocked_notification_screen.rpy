# The achievement unlocked notification screen is shown when the player unlocks an achievement.
screen achievement_unlocked_notification(achievement_title, num_achievements_unlocked, num_achievements):
    frame:
        style_prefix "confirm"

        xfill True
        xsize 1000
        ypadding 30
        yalign .25

        vbox:
            style_prefix "achievement_unlocked_notification"
            xfill True
            spacing 25

            text _("Achievement Unlocked!"):
                style "achievement_unlocked_notification_title"

            text "{icon=award}":
                style "achievement_unlocked_notification_title"

            text _(achievement_title)

            text _("Number of Achievements Unlocked: [num_achievements_unlocked] / [num_achievements]")

            textbutton _("Let's Unlock Them All!"):
                xalign 0.5
                action Return()


style achievement_unlocked_notification_text:
    xalign 0.5
    text_align 0.5

style achievement_unlocked_notification_title is achievement_unlocked_notification_text:
    color gui.accent_color
    size gui.label_text_size
