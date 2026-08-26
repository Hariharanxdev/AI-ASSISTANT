import time

from chatbot import Chatbot
from config import GROQ_API_KEY
from prompts import PROMPTS
from logger import logger


def main():
    if not GROQ_API_KEY:
        print("Error: GROQ_API_KEY is missing from .env")
        return

    try:

        chatbot = Chatbot()

        print("AI Assistant")
        print("Available roles:")

        for key, role in PROMPTS.items():
            print(f"{key}. {role['name']}")

        print("Type 'exit' to quit.")
        print("Type 'role' to change role.")
        print()

        while True:

            question = input("You: ").strip()

            # Exit
            if question.lower() == "exit":
                print("Goodbye!")
                break

            # Change role
            if question.lower() == "role":

                print("\nChoose a role:")

                for key, role in PROMPTS.items():
                    print(f"{key}. {role['name']}")

                choice = input("Enter choice: ").strip()

                if choice in PROMPTS:

                    chatbot.set_role(choice)

                    print(
                        f"Role changed to "
                        f"{PROMPTS[choice]['name']}"
                    )

                else:

                    print("Invalid role.")

                continue

            # Return to normal assistant
            if question.lower() == "normal":

                chatbot.set_role(None)

                print("Role changed to Normal Assistant.")

                continue

            # Empty prompt
            if not question:

                print("Please enter a question.")

                continue

            # Prompt length
            if len(question) > 2000:

                print(
                    "Prompt is too long. "
                    "Please keep it under 2000 characters."
                )

                continue

            # Ask AI
            start_time = time.time()

            answer = chatbot.ask(question)

            response_time = time.time() - start_time

            print(f"AI: {answer}\n")

            # Logging
            logger.info(
                "Role=%s | Question=%s | Response=%s | Response Time=%.2f seconds",
                (
                    PROMPTS[chatbot.current_role]["name"]
                    if chatbot.current_role
                    else "Normal Assistant"
                ),
                question,
                answer,
                response_time
            )

    except KeyboardInterrupt:

        print("\n\nAI: Application stopped by user.")


if __name__ == "__main__":
    main()