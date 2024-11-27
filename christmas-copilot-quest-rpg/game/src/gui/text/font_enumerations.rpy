init python in font_enumerations:
    from enum import Enum

    class BaseFont(Enum):
        """
        The file paths for the base fonts used in the game.
        """

        REGULAR = "fonts/lato/Lato-Regular.ttf"
        BOLD = "fonts/lato/Lato-Bold.ttf"
        ITALIC = "fonts/lato/Lato-Italic.ttf"

    class MonospaceFont(Enum):
        """
        The file paths for the monospace font used in the game.
        """

        REGULAR = "fonts/roboto_mono/RobotoMono-Regular.ttf"
        BOLD = "fonts/roboto_mono/RobotoMono-Bold.ttf"
        ITALIC = "fonts/roboto_mono/RobotoMono-Italic.ttf"
