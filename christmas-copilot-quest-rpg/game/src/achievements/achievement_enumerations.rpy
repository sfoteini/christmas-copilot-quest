init -100 python in achievement_enumerations:
    """
    Enumerations for the achievements that a player can unlock in the game.
    """

    from enum import Enum

    class AchievementTitle(Enum):
        """
        The titles of the achievements that a player can unlock in the game.
        """

        LEARN_PROMPT_ENGINEERING_BEST_PRACTICES = _(
            "Understand the principles of communicating with GitHub Copilot: Single, Specific, Short, and Surround"
        )
        INSTALL_GITHUB_COPILOT_VSCODE_EXTENSION = _("Install the GitHub Copilot extension for Visual Studio Code")
        USE_GITHUB_COPILOT_AUTOCOMPLETIONS = _("Use GitHub Copilot to get code suggestions in your editor")
        ASK_FIRST_QUESTION_TO_GITHUB_COPILOT_CHAT = _("Ask your first question to GitHub Copilot in the chat")
        USE_GITHUB_COPILOT_KEYWORDS = _(
            "Use keywords to help GitHub Copilot understand your prompt: Chat participants, slash commands, and variables"
        )
        USE_GITHUB_COPILOT_INLINE_CHAT = _("Ask your first question to GitHub Copilot in the inline chat")
