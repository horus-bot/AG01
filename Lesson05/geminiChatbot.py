# 
from google import genai


class Chatbot:

    def __init__(self, name):
        self.name = name
        # self.client = genai.Client(api_key="")

    def chat(self, message):

        interaction = self.client.interactions.create(
            model="gemini-3.8-flash",
            input=message
        )

        print(self.name, ":", interaction.output_text)


def ChatbotInterface():

    chatbot = Chatbot("Harsh")

    while True:

        text = input("You : ")

        if text.lower() == "exit":
            break

        chatbot.chat(text)


ChatbotInterface()