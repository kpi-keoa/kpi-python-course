import random

class Cinema():
    def __init__(self, name, genre, years):
        self.name = name
        self.genre = genre
        self.years = years

    def genre_is(self):
        print(f"{self.name} genre is {self.genre}")


class Film(Cinema):
    def __init__(self, name, genre, years, duration, parts):
        super().__init__(name, genre, years)
        self.parts = parts
        self.duration = duration
                
    def number_of_parts(self):
        print(f"{self.name} contains {self.parts} parts")

    def about_film(self):
        if self.parts > 1:
            for part in range(1, self.parts + 1):
                print(f"{self.name} {part}: {self.genre}, {self.years} production year, {self.duration} minutes")
                self.years += 2
        else:
            print(f"{self.name}: {self.genre}, {self.years} production year, {self.duration} minutes")


class Serial(Cinema):
    def __init__(self, name, genre, years, season):
        super().__init__(name, genre, years)
        self.season = season
        
    def about_serial(self):
        if isinstance(self.season, int):
            print(f"{self.name}: {self.genre}, {self.years}, {self.season} seasons")
        else:
            print(f"Seasons amount must be a number!")


class Season(Serial):
    def __init__(self, name, genre, season, years, series=10):
        super().__init__(name, genre, season, years)
        self.years = years
        self.series = series
        self.season = season

    def season_info(self):
        self.season = random.randrange(1, self.season)
        for i in range(1, self.season):
            self.years += 1
        print(f"{self.name} {self.season}: {self.genre}, {self.years}, {self.series} series")


def main():
    c = Cinema("Titanic", "Film-disaster", 1997)
    c.genre_is()

    f = Film("Ghost", "Fantasy/Drama", 1990, 127, 1)
    f.number_of_parts()
    f.about_film()
    
    f = Film("Astral", "Horror", 2011, 80, 4)
    f.number_of_parts()
    f.about_film()

    s = Serial("Game of Trones", "Fantasy/Drama", "2011-2019", 8)
    s.about_serial()

    n = Season("Game of Trones", "Fantasy/Drama", 9, 2011)
    n.season_info()


if __name__ == '__main__':
    main()








    

