init python:
    # Define the font used for bold and italic text
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", True, False] = ("fonts/lato/Lato-Bold.ttf", False, False)
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", False, True] = ("fonts/lato/Lato-Italic.ttf", False, False)

    # Define an alias for the font used for code text
    config.font_name_map["code"] = "fonts/roboto_mono/RobotoMono-Regular.ttf"
    config.font_replacement_map["fonts/roboto_mono/RobotoMono-Regular.ttf", True, False] = ("fonts/roboto_mono/RobotoMono-Bold.ttf", False, False)
    config.font_replacement_map["fonts/roboto_mono/RobotoMono-Regular.ttf", False, True] = ("fonts/roboto_mono/RobotoMono-Italic.ttf", False, False)

    # Define a custom text tag for code text
    def code_snippet_tag(tag, argument, contents):
        """
        Defines a custom text tag that changes the font of the text to a monospace font.
        """
        return [
            (renpy.TEXT_TAG, "size=30"),
            (renpy.TEXT_TAG, "font=code")
        ] + contents + [
            (renpy.TEXT_TAG, "/font"),
            (renpy.TEXT_TAG, "/size")
        ]

    config.custom_text_tags["code"] = code_snippet_tag
