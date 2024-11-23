label get_started_with_github_copilot:
    # TODO Add background image
    scene bg room

    gingerbot "Hello, [player_name]! I'm GingerBot, your AI assistant powered by GitHub Copilot. 
        I'm here to help you with your coding tasks."

    player "Nice to meet you, GingerBot! I'm glad you're here. I could really use some help with this project."

    gingerbot "I'm here to assist you with writing code, suggesting improvements, and answering your questions. 
        Just let me know how I can help!"

    player "Can you rewrite the entire application? Felix said the code is a bit messy and not working properly."

    gingerbot "Well, I can't write the entire application from scratch, but I can help you refactor the code 
        and make it more efficient."

    player "I thought you could do anything!"

    gingerbot "I can do a lot, but I still need your guidance and creativity to write the best code."

    gingerbot "Before we dive into the code, let's make sure you understand the basics of communicating with me. 
        There are four key rules to follow when interacting with me."

    player "Sounds good! What are the rules?"

    gingerbot "{b}Single, Specific, Short, and Surround.{/b} Let's break them down:"

    gingerbot "{b}Single{/b}: Focus on one clear and well-defined task at a time. Don't try to pack too many things 
        into one request. If you ask me too many things at once, it's harder for me to give you a precise answer."

    player "Got it! So, if I need help with multiple tasks, I should ask one at a time?"

    gingerbot "Exactly! The clearer the task, the more accurate my suggestions will be."

    gingerbot "Next is {b}Specific{/b}: Be as specific and detailed as possible when asking for help. 
        The more information you provide, the better I can understand your needs."

    player "So, I should give you all the details about what I want to achieve?"

    gingerbot "Yes! The more context you provide, the better. But don't overwhelm me with too much information; 
        that can make things confusing."

    gingerbot "{b}Short{/b}: Keep your requests concise and to the point. Avoid lengthy explanations or unnecessary 
        details, as they can confuse me."

    player "I should keep it short but still detailed, got it!"

    gingerbot "Exactly! It's all about balance."

    gingerbot "And finally, {b}Surround{/b}: Keep any related files open and use descriptive names. The more 
        context I have, the better I can understand what you're working on and provide accurate suggestions."

    player "So, you also consider other information besides what I type to understand the context?"

    gingerbot "Yes, I analyze the code you're working on in various ways to provide the best suggestions. 
        You will learn more about this as we progress through the game."

    gingerbot "To summarize, remember the four rules: Single, Specific, Short, and Surround. Follow these 
        guidelines, and we'll make a great team!"

    player "Thanks, GingerBot! That makes a lot of sense. I'm ready to give it a try!"

    # TODO: Check if we can add an achievement for learning the rules

    gingerbot "Great to hear! But before we start coding, let's make sure you're set up to work with me."

    menu:
        gingerbot "Do you have a GitHub Copilot account?"

        "Yes, I have a GitHub Copilot account.":
            jump user_has_github_copilot_account

        "No, I don't have a GitHub Copilot account. How do I get one?":
            jump create_github_copilot_account

        "No, I don't have a GitHub Copilot account. But I will create one later.":
            jump user_will_create_github_copilot_account_later

label user_has_github_copilot_account:
    gingerbot "Perfect! You can use your GitHub Copilot account to complete the tasks in this game."
    jump install_github_copilot_in_ide

label create_github_copilot_account:
    gingerbot "GitHub Copilot offers plans for individual developers, organizations, and academic use."

    menu:
        gingerbot "Which one best describes you?"

        "I'm an individual developer.":
            jump create_github_copilot_individual_account

        "I'm part of an organization.":
            jump get_github_copilot_business_account

        "I'm a student or educator.":
            jump create_github_copilot_individual_account

label create_github_copilot_individual_account:
    gingerbot "GitHub Copilot Individual is free for verified students, teachers, and maintainers of popular 
        open-source projects on GitHub."
    gingerbot "If you qualify, you can sign up for free using your GitHub account. If not, you can start with a 
        30-day free trial."

    player "Thanks for the information, GingerBot! I'll make sure to get my GitHub Copilot account set up."

    jump install_github_copilot_in_ide

label get_github_copilot_business_account:
    gingerbot "Great! You can contact your organization's administrator to get access to GitHub Copilot."
    player "Thanks for the information, GingerBot! I'll make sure to get my GitHub Copilot account set up."

    jump install_github_copilot_in_ide

label user_will_create_github_copilot_account_later:
    gingerbot "No problem! You can create a GitHub Copilot account once you've completed this learning journey."
    jump explore_github_copilot_features

label install_github_copilot_in_ide:
    player "What's next?"

    gingerbot "Next, let's install GitHub Copilot in your IDE. Did you know that I work with several popular IDEs?"

    player "Really? Which ones?"

    gingerbot "The main IDEs I support are: Visual Studio, Visual Studio Code, JetBrains IDEs, and Vim/Neovim."

    gingerbot "For this game, we'll use Visual Studio Code since it supports the most features."

    menu:
        gingerbot "Do you need help installing GitHub Copilot in Visual Studio Code?"

        "Yes, let's install GitHub Copilot in Visual Studio Code.":
            jump install_github_copilot_in_vscode

        "No, I'll figure it out on my own.":
            gingerbot "No problem! You can install GitHub Copilot whenever you're ready."
            jump explore_github_copilot_features

label install_github_copilot_in_vscode:
    gingerbot "Great! Here's what you need to do:"

    gingerbot "Open Visual Studio Code and go to the {b}Extensions{/b} view."

    gingerbot "Search for GitHub Copilot and select the 
        {a=https://marketplace.visualstudio.com/items?itemName=GitHub.copilot}GitHub Copilot extension{/a} authored  
        by GitHub. Click {b}Install{/b}. The GitHub Copilot Chat extension will also be installed automatically."

    gingerbot "After installation, you'll see a notification prompting you to sign in with your GitHub account. 
        Click the notification and follow the steps to authorize Visual Studio Code for your GitHub account."

    gingerbot "That's it! You're all set to start coding with GitHub Copilot."

    player "Thanks for the help! I will set it up now."

label explore_github_copilot_features:
    menu:
        "Let's start coding with GitHub Copilot!":
            pass
