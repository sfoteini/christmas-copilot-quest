init python in text_tag_utils:
    from store.feather_icons import get_feather_icon_from_name
    from store.font_enumerations import MonospaceFont, IconFont

    def code_snippet_tag(tag, argument, contents):
        """
        Defines a custom text tag that changes the font of the text to a monospace font.
        """
        return [
            (renpy.TEXT_TAG, "size=30"),
            (renpy.TEXT_TAG, f"font={MonospaceFont.REGULAR.value}"),
        ] + contents + [
            (renpy.TEXT_TAG, "/font"),
            (renpy.TEXT_TAG, "/size")
        ]

    def icon_tag(tag, icon):
        """
        Defines a custom text tag that displays an icon. Feather icons are used.
        """
        return [
            (renpy.TEXT_TAG, f"font={IconFont.FEATHER_ICONS.value}"),
            (renpy.TEXT_TEXT, get_feather_icon_from_name(icon)),
            (renpy.TEXT_TAG, "/font"),
        ]
