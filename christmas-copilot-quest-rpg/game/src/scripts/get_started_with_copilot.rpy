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

    gingerbot "To summarize, remember the four rules: {b}Single, Specific, Short, and Surround{/b}. Follow these 
        guidelines, and we'll make a great team!"

    player "Thanks, GingerBot! That makes a lot of sense. I'm ready to give it a try!"

    # TODO: Check if we can add an achievement for learning the rules

    gingerbot "Great to hear! But before we start coding, let's make sure you're set up to work with me."

    menu:
        gingerbot "Do you have a GitHub Copilot account?"

        "Yes, I have a GitHub Copilot account.":
            gingerbot "Perfect! You can use your GitHub Copilot account to complete the tasks in this game."
            jump install_github_copilot_in_ide

        "No, I don't have a GitHub Copilot account. How do I get one?":
            jump create_github_copilot_account

        "No, I don't have a GitHub Copilot account. But I will create one later.":
            gingerbot "No problem! You can create a GitHub Copilot account once you've completed this 
                learning journey."
            jump explore_github_copilot_features

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

    gingerbot "Now that you're all set up, let's explore some of the features of GitHub Copilot. Let me show you one 
        of my coolest features: autocompletions."

    player "Autocompletions? Like suggesting code as I type?"

    gingerbot "Exactly! As you type a line of code, a comment, or even add a blank line, I can predict what you 
        need and offer suggestions."

    player "That sounds really helpful! How do I use it?"

    gingerbot "It's simple. Just start typing, and when you see a suggestion you like, press the {code}Tab{/code} key 
        to accept it. If you're not sure about a suggestion, you can even browse alternatives."

    player "That's pretty neat! Can you show me an example?"

    gingerbot "Of course! First, create a new Python file. We are going to use Python for this example, however 
        other languages will work similarly."

    gingerbot "I provide suggestions for numerous languages and frameworks, but I work especially well with Python, 
        JavaScript, TypeScript, Ruby, Go, C#, and C++."

    menu:
        "I've created a new Python file. What's next?":
            pass

    # TODO Add a different font for code snippets

    gingerbot "Start typing the following function definition:
        \n{code}def calculate_days_between_dates(start_date, end_date):{/code}"

    gingerbot "As you type, I'll suggest the rest of the function in dimmed gray text. You can accept the 
        suggested code by pressing the {code}Tab{/code} key."

    menu:
        "I typed the function definition and saw a suggestion. What should I do next?":
            pass

        "I typed the function definition, but I didn't see a suggestion. What can I do?":
            gingerbot "No worries! If there's no suggestion, check the status of the Copilot extension in the 
                bottom-right corner of Visual Studio Code. Ensure it's active and connected to your account."

            gingerbot "If there's still no suggestion, try restarting or updating Visual Studio Code and the Copilot 
                extension. You can also check the GitHub Copilot documentation for help."

            gingerbot "Once you're ready, start typing the function definition again."

            menu:
                "I am ready to continue. What next?":
                    pass

    gingerbot "Great job! You've seen how autocompletions work. Now, let's take it further. I can suggest multiple 
        implementations for the same function."

    player "Wow, that sounds powerful! I'm ready to try it out."

    gingerbot "Delete the function body and press {code}Enter{/code} to add a new line after the function definition. 
        You should see a suggestion for the function body appear."

    gingerbot "If nothing shows up, don't worry! Just retype the function definition as you did before."

    gingerbot "Sometimes, I can suggest multiple ways to implement the same function. You can hover over a suggestion 
        to preview alternatives and pick the one that works best for you."

    gingerbot "To browse through the options, use the left and right arrows, or open the {b}Completions Panel{/b} 
        from the ellipsis (...) menu."

    player "That's really helpful! This could save me so much time."

    gingerbot "That's the idea! My goal is to speed things up for you."

    gingerbot "Just remember to review my suggestions before accepting them as they may not always be correct 
        or fit what you're trying to do."

    player "I see! Actually, I had a slightly different idea for how to implement the function. Can you still 
        help me with that?"

    gingerbot "Of course! Just give me some hints like type annotations, docstrings, or even a quick comment, and 
        I'll adjust my suggestions to match your needs."

    player "I'll keep that in mind."

    gingerbot "Why don't you give it a try now? Add one of these hints and see how I adjust my suggestions based 
        on your input."

    menu:
        "I added a hint and tried it out!":
            gingerbot "Awesome! You're getting the hang of this. Keep experimenting with different types of hints to 
                see how I adjust my suggestions."

        "I understand how it works, but I'll try it later.":
            gingerbot "You're doing great so far! Feel free to explore more features whenever you're ready."

        "I'm not sure how to add a hint.":
            gingerbot "No problem! Let's try it together. Suppose you want to specify that the start and end dates 
                are of type {code}datetime{/code}."

            gingerbot "Here's an example with type annotations:
                \n{code}def calculate_days_between_dates(start_date: datetime, end_date: datetime) -> int:{/code}"

            menu:
                "Got it! I'll give it a try now.":
                    pass

            menu:
                gingerbot "Would you like to see another example of adding a hint?"

                "Yes, show me another example.":
                    gingerbot "Sure! Let's try adding the following comment in a new line:
                        \n{code}# Function to calculate the days between two dates provided as strings in a specific format{/code}"

                    gingerbot "You will see how I adjust my suggestions based on the context you provide."

                "No, I'm good for now.":
                    gingerbot "Awesome! You're getting the hang of this. Keep experimenting with different types of 
                        hints to see how I adjust my suggestions."

    # TODO Add an achievement for learning about autocompletions

    # TODO In the middle of the conversation, add a tip about having open files for better suggestions
    # To give you relevant inline suggestions, Copilot looks at the current and open files in your editor to analyze
    # the context and create appropriate suggestions. Having related files open in VS Code while using Copilot helps
    # set this context and lets the Copilot see a bigger picture of your project.

label explore_github_copilot_chat:
    player "Yeah, it's impressive how flexible the suggestions can be!"

    player "But honestly, manually adding docstrings or temporary comments feels a bit tedious. Is there a better way 
        to guide the code suggestions?"

    gingerbot "I can understand your frustration. That's where GitHub Copilot Chat comes in."

    player "GitHub Copilot Chat? What's that?"

    gingerbot "It's like having a coding assistant in your editor who can answer questions, explain code, suggest 
        fixes, and even write documentation for you."

    player "That sounds amazing! How is it different from regular autocompletions?"

    gingerbot "Great question! While GitHub Copilot suggests code as you type, GitHub Copilot Chat takes it to the 
        next level. You can actually {i}talk{/i} to me and receive answers to coding-related questions directly 
        within Visual Studio Code."

    player "Wait, so I can just ask you to explain a piece of code or suggest a fix for a bug and you'll help me 
        out?"

    gingerbot "Exactly! Just highlight any code, and I can provide explanations, suggest improvements, or even 
        generate unit tests for it."

    gingerbot "If you're stuck on a bug, trying to improve your code's performance, or just want to understand 
        how something works, I'm here to help."
    
    player "{i}(This could save so much time and automate all those boring tasks!){/i}"

    player "And it's all within Visual Studio Code?"

    gingerbot "Yep! There's a dedicated chat panel where you can interact with me."

    menu:
        gingerbot "Would you like to try it out now?"

        "Yes, let's give it a try!":
            pass

        "No, I'm good for now.":
            gingerbot "Oh, come on! You can't escape me that easily. Let's give it a try!"
            player "{i}(I guess I can't say no to GingerBot... Let's see how this goes.){/i}"

    gingerbot "Alright [player_name]! First, let's explore the chat panel. This interface allows for an in-depth 
        conversation between you and me."

    gingerbot "I know you like examples, so let's select the function you wrote earlier and ask me to explain it."

    player "Sounds good! I'll highlight the function and ask for an explanation."

    menu how_to_ask_github_copilot_to_explain_function:
        player "{i}(I've learned about the rules when interacting with GitHub Copilot... What should I ask to get the 
            best explanation?){/i}"

        "Explain.":
            gingerbot "Although that's a valid request, it's a bit too vague and might not provide the best answer 
                when working in a complex codebase."
            gingerbot "Try to be more specific and provide context to get the most accurate explanation, for example, 
                'Explain the selected code.'."

        "Explain the selected code.":
            gingerbot "Great choice! This will help me understand what you're looking for."

        "What's Santa's favorite programming language?":
            gingerbot "Haha, nice try! Let's focus on the function for now."
            jump how_to_ask_github_copilot_to_explain_function

        "Tell me a joke.":
            gingerbot "Oh, [player_name], you're trying to trick me! Let's focus on the function for now."
            jump how_to_ask_github_copilot_to_explain_function

    # TODO Add an achievement for learning about GitHub Copilot Chat

label intro_to_github_copilot_chat_keywords:
    gingerbot "As you remember from the rules to follow when interacting with me..."

    menu copilot_rules_reminder:
        player "{i}(Oh, the rules... What were they again?){/i}"

        "Single, Short, Specific":
            player "{i}(I think I've missed one of the rules... Let's try again.){/i}"
            jump copilot_rules_reminder

        "Bring cookies!":
            player "{i}(Cookies are always a good idea, but not for the rules... Let's try again.){/i}"
            jump copilot_rules_reminder

        "Single, Specific, Short, Santa":
            player "{i}(I'm pretty sure Santa wasn't one of the rules... Let's try again.){/i}"
            jump copilot_rules_reminder
        
        "Single, Specific, Short, Surround":
            player "{i}(That's it! I remember now.){/i}"

    gingerbot "Being specific and providing context will help me give you the best explanation. Chat participants, 
        slash commands, and chat variables can help me understand your prompt."

    player "Participants, slash commands, and chat variables? What are those?"

    gingerbot "Let's break it down."

    gingerbot "Participants are like experts specializing in specific domains. They can perform actions or answer 
        questions tailored to their expertise. You can mention a participant using the {code}@{/code} symbol."

    # TODO Add tip: GitHub Copilot may infer a relevant chat participant based on the context of your question even
    # if you haven't explicitly mentioned the participant you want to use in your prompt.

    gingerbot "I support several participants, such as the {code}@workspace{/code} which has context about the code 
        in your workspace, or the {code}@terminal{/code} participant that has context about the integrated terminal 
        and its contents."

    player "I got it! Participants help you understand the context and intent of the question."

    player "{i}(I can see the supported participants by typing {code}@{/code} in the chat... This is getting 
        interesting!){/i}"

    # TODO Check if a quiz about chat participants can be added here

    gingerbot "Slash commands are shortcuts to specific functionality provided by chat participants and help me 
        understand your intent. To use a slash command, type {code}/{/code} followed by the command name."

    player "So, I can use slash commands to avoid typing long sentences for common actions!"

    player "{i}(Oh, I could use a slash command to get the explanation faster...){/i}"

    menu slash_command_for_code_explanation:
        player "{i}(What command could I have used to get the explanation previously?){/i}"

        "@terminal /explain":
            player "{i}(That seems like a good guess, but not quite right... I am not in the terminal. 
                Let's try again.){/i}"
            jump slash_command_for_code_explanation

        "@workspace /describe":
            player "{i}(Oh, it seems that it's not a valid command... I feel like I'm close. I'll try again.){/i}"
            jump slash_command_for_code_explanation

        "@santa /makeCookies":
            player "{i}(Cookies are always a good idea, but not for a slash command... Let's try again.){/i}"
            jump slash_command_for_code_explanation

        "@workspace /explain":
            player "{i}(That's it! I could have used the {code}/explain{/code} command to get the explanation. 
                I'll remember that.){/i}"

    gingerbot "That's the idea! Shash commands help you interact with me more efficiently. Try using {code}/tests{/code} 
        or {code}/new{/code} to see what happens."

    gingerbot "Chat variables add additional context to your question. You can use chat variables to refer to 
        specific parts of your code or terminal contents."

    player "And I can see the available chat variables by typing {code}#{/code} in the chat, right?"

    gingerbot "That's right! You're doing great."

    menu chat_variable_for_selection:
        gingerbot "Which chat variable would you use to refer to the highlighted code in the editor?"

        "#file":
            gingerbot "Not quite right. The {code}#file{/code} variable includes a specific file as context in the chat. 
                Let's try again."
            jump chat_variable_for_selection

        "#cookie":
            gingerbot "I like where your head is at, but the {code}#cookie{/code} variable doesn't exist. Let's try again."
            jump chat_variable_for_selection

        "#selection":
            gingerbot "That's correct! The {code}#selection{/code} variable refers to the current selection in the active editor. 
                You're doing great!"

        "#editor":
            gingerbot "Close enough. The {code}#editor{/code} variable adds the visible source code in the active editor as context 
                in the chat. Let's try again."
            jump chat_variable_for_selection

    # TODO Add an achievement for learning about GitHub Copilot Chat keywords

label explore_github_copilot_inline_chat:
    gingerbot "Great job, [player_name]! Now, let's try the Inline Chat. I couldn't be your pair programmer without it."

    player "Can I talk to you directly in the code editor?"

    gingerbot "Yes! You can ask me questions, get explanations, and receive suggestions directly in the code editor."

    gingerbot "With Inline Chat, you can preview code suggestions directly within your code without switching to the 
        chat panel."

    player "That sounds really convenient! I could quickly ask a question and continue coding without interruptions."

    gingerbot "And you can also use some of the chat commands and variables we discussed earlier to give me more context."

    player "{i}(I should try this out!){/i}"

    player "{i}(I can select the code, open the chat using {code}Ctrl+I{/code} and ask for an explanation...){/i}"

    player "{i}(I can even use the {code}/explain{/code} command to get the explanation faster.){/i}"

    gingerbot "To make it easier to use Copilot features, there are Smart Actions that provide quick access to common tasks."

    gingerbot "You can select a piece of code, right-click, and choose your desired action from the {b}Copilot{/b} menu."

    player "That's really handy! I can ask for an explanation with just a few clicks."

label explore_github_copilot_quick_chat:
    menu github_copilot_quick_chat:
        gingerbot "There's one more place where you can find me in Visual Studio Code. Can you spot it?"

        "In the Christmas tree?":
            gingerbot "Haha, not quite! But good guess. Let's try again."
            jump github_copilot_quick_chat

        "In the Smart Chat?":
            gingerbot "Close! But not quite... There's no Smart Chat. Let's try again."
            jump github_copilot_quick_chat

        "In a Cookie?":
            gingerbot "I wish! But no, I'm not in a cookie. Let's try again."
            jump github_copilot_quick_chat

        "In the Quick Chat?":
            gingerbot "Bingo! You found me in the Quick Chat."

    gingerbot "The Quick Chat is a convenient way to ask me a quick question and get back to coding without interruptions."

# TODO Add outro for this section
