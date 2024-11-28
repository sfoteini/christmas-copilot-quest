init 1 python:
    from store.text_tag_utils import code_snippet_tag, icon_tag

    # Install the custom text tags
    config.custom_text_tags["code"] = code_snippet_tag
    config.self_closing_custom_text_tags["icon"] = icon_tag
