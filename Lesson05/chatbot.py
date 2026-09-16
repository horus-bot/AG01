class Chatbot:

    def __init__(self,name):
        self.name = name 

    def chat(self,message):
        print("hey this is your chatbot")    


def ChatbotInterface():
    chatbot = Chatbot("harsh")
    while True:
        text = input("you : ")
        if (text=="exit"):
            break
        chatbot.chat(text)

ChatbotInterface()
