init python in font_utils:
    from renpy import config
    from typing import Optional

    def install_font_family(
        base_font: str, bold_font: Optional[str] = None, italic_font: Optional[str] = None
    ) -> None:
        """
        Installs a font family into the game.

        :param base_font: The file path for the font used for regular text.
        :param bold_font: The file path for the font used for bold text (optional).
        :param italic_font: The file path for the font used for italic text (optional).
        """
        if bold_font:
            config.font_replacement_map[base_font, True, False] = (bold_font, False, False)

        if italic_font:
            config.font_replacement_map[base_font, False, True] = (italic_font, False, False)
