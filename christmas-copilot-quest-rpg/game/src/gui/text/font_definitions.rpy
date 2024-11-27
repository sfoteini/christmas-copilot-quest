init 1 python:
    from store.font_enumerations import BaseFont, MonospaceFont
    from store.font_utils import install_font_family

    # Define the fonts used for bold and italic text
    install_font_family(BaseFont.REGULAR.value, BaseFont.BOLD.value, BaseFont.ITALIC.value)
    install_font_family(MonospaceFont.REGULAR.value, MonospaceFont.BOLD.value, MonospaceFont.ITALIC.value)
