init python in text_tag_utils:
    from store.font_enumerations import MonospaceFont

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
