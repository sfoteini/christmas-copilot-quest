init python:
    # Define the font used for bold and italic text
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", True, False] = ("fonts/lato/Lato-Bold.ttf", False, False)
    config.font_replacement_map["fonts/lato/Lato-Regular.ttf", False, True] = ("fonts/lato/Lato-Italic.ttf", False, False)
