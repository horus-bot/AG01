class Celebrities:
    def job(self):
        print(self.name, "is a", self.profession)

person1 = Celebrities()
person2 = Celebrities()

person1.name = "Shahrukh Khan"
person2.name = "Taylor Swift"
person1.profession = "Actor"
person2.profession = "Singer"

person1.job()
person2.job()
