class cinema():
    def __init__(self, name, genre, duration):
        self.name = name
        self.genre
        self.duration

    def genreIs(self):
        print(f"{self.name} genre is {self.genre}")

class film(cinema):
    def __init__(self, name, genre, duration, parts):
        cinema.__init__(self, name, genre, duration)
        self.parts = parts

    def aboutFilm(self):
        print(f"{self.name}: {self.genre}, {self.duration} minutes")
        
    def numberOfParts(self):
        print(f"{self.name} contains {self.parts} parts")

class serial(cinema):
    def __init__(self, name, genre, season):
        cinema.__init__(self, name, genre)
        self.season = season

    def aboutSerial(self):
        print(f"{self.name}: {self.genre}, {self.season} seasons")
        
    def numberOfSeasons(self):
        print(f"{self.name} contains {self.season} seasons")

    def numberOfSeries(self):
        print(f"{self.name} contains {self.series} seasons")

class season(serial):
    def __init__(self, season, series=1):
        serial.__init__(self, season)
        self.series = series

    def seriesNumber(self, series):
        self.series = series

    def seasonInfo(self):
        print(f"{self.season} contains {self.series} series")

def main():
    c = cinema("Titanic", "Film-disaster", 184)
    c.genreIs()

    f = film("Ghost", "Fantasy/Drama", 127, 1)
    f.aboutFilm()
    f.numberOfParts()

    s = serial("Game of Trones", "Fantasy/Drama", 8)
    s.aboutSerial()
    s.numberOfSeasons()
    s.numberOfSeries()

    n = season(8)
    n.seriesNumber()
    n.seasonInfo()


if __name__ == '__main__':
    main()








    

