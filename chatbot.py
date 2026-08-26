from openai import OpenAI
from openai import APIConnectionError, APITimeoutError

from config import GROQ_API_KEY
from prompts import PROMPTS


class Chatbot:

    def __init__(self):
        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )

        # No role selected initially
        self.current_role = None

        self.conversation_history = []

    def set_role(self, role):
        self.current_role = role

        # Start fresh conversation when changing role
        self.conversation_history = []

    def ask(self, question):

        self.conversation_history.append({
            "role": "user",
            "content": question
        })

        # Keep latest 10 messages
        self.conversation_history = self.conversation_history[-10:]

        messages = []

        # Add system prompt only when a role is selected
        if self.current_role:

            messages.append({
                "role": "system",
                "content": PROMPTS[self.current_role]["prompt"]
            })

        messages.extend(self.conversation_history)

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = self.client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=messages,
                    timeout=10.0
                )

                answer = response.choices[0].message.content

                self.conversation_history.append({
                    "role": "assistant",
                    "content": answer
                })

                # Keep latest 10 messages
                self.conversation_history = (
                    self.conversation_history[-10:]
                )

                return answer

            except APITimeoutError:

                print("The AI service request timed out.")
                print(
                    f"Retrying... ({attempt + 1}/{max_retries})"
                )

            except APIConnectionError:

                print(
                    "Network error. "
                    "Please check your internet connection."
                )

                print(
                    f"Retrying... ({attempt + 1}/{max_retries})"
                )

            except Exception as error:

                print(
                    f"Request failed. "
                    f"Retrying... ({attempt + 1}/{max_retries})"
                )

        return "Sorry, I couldn't connect to the AI service."