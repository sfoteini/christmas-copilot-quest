init python in font_enumerations:
    """
    Enumerations for the fonts used in the game.
    """

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

    class IconFont(Enum):
        """
        The file paths for the icon font used in the game.
        """

        FEATHER_ICONS = "fonts/feather_icons/FeatherIcons.ttf"
