class StudyAgent:
    
    def search(self):
        
        print(self.name, "is searching for information")

    def summarize(self):
        print(self.name, "is summarizing information")

    def create_quiz(self):
        print(self.name, "is creating a quiz")

agent = StudyAgent()
agent.name = "Jarvis"
agent.search()
agent.summarize()
agent.create_quiz()