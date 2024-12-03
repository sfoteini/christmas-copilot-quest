init:
    # Character definitions
    define player = Character("[player_name]", image="player")
    define felix = Character(_("Felix"), image="felix")
    define gingerbot = Character(_("GingerBot"))

    # Character images
    image felix = dynamic_blink.DynamicBlink("felix_eyes_open", "felix_eyes_closed")

    image noelle_eyes_blink = dynamic_blink.DynamicBlink("noelle_eyes_open", "noelle_eyes_closed")
    image malik_eyes_blink = dynamic_blink.DynamicBlink("malik_eyes_open", "malik_eyes_closed")
    image carey_eyes_blink = dynamic_blink.DynamicBlink("carey_eyes_open", "carey_eyes_closed")

    layeredimage player:
        if character_image == "noelle":
            "noelle_eyes_blink"
        elif character_image == "malik":
            "malik_eyes_blink"
        elif character_image == "carey":
            "carey_eyes_blink"

    image side player = LayeredImageProxy("player")
