# The click to continue screen is shown when text finishes displaying to prompt the player to click to continue.
screen ctc(arg=None):
    zorder 100
    style_prefix "click_to_continue"

    hbox:
        at ctc_appear
        xalign 0.96
        yalign 0.96
        spacing 10

        if not renpy.variant("small"):
            text _("Click to continue"):
                style "click_to_continue_text"

        text "{icon=chevrons-down}" at ctc_arrow_animation:
            style "click_to_continue_arrow"


style click_to_continue_text:
    font gui.interface_text_font
    size gui.notify_text_size
    xalign 0.94
    yalign 0.96
    color gui.accent_color

style click_to_continue_arrow:
    size gui.interface_text_size
    color gui.accent_color


# This transform is used to make the click to continue screen appear after a delay.
transform ctc_appear:
    alpha 0.0
    pause 0.5
    linear 0.3 alpha 1.0

# This transform is used to blink the click to continue arrow.
transform ctc_arrow_animation:
    alpha 0.2

    block:
        linear 1.0 alpha .9
        pause 0.2
        linear 1.0 alpha .2
        pause 0.2
        repeat
