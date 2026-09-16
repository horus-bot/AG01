class Movie:
    title = "Avatar"
    director = "James Cameron"

    def info(self):
        print("Movie:", self.title)
        print("Director:", self.director)

film = Movie()
film.info()