init python in font_utils:
    from renpy import config
    from typing import Optional

    def install_font_family(
        base_font: str, bold_font: Optional[str] = None, italic_font: Optional[str] = None
    ) -> None:
        """
        Installs a font family into the game. If bold_font or italic_font are not provided, the base_font will be used
        for those styles.

        :param base_font: The file path for the font used for regular text.
        :param bold_font: The file path for the font used for bold text (optional).
        :param italic_font: The file path for the font used for italic text (optional).
        """
        bold_font = bold_font or base_font
        italic_font = italic_font or base_font

        config.font_replacement_map[base_font, True, False] = (bold_font, False, False)
        config.font_replacement_map[base_font, False, True] = (italic_font, False, False)
