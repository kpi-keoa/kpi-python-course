class Musical_Group():
    def __init__ (self, group_name, singer, song):
        self.group_name = group_name
        self.singer = singer
        self.song = song

    def what_the_song (self):
        print(f"\n{self.singer} from the group '{self.group_name}', wrote a song called '{self.song}'.")


class Song(Musical_Group):
    def __init__(self, group_name, singer, song, topic, main_character):
            Musical_Group. __init__(self, group_name, singer, song)
            self.topic = topic
            self.main_character = main_character

    def name_of_song (self):
             print(f"{self.group_name} {self. singer} {self.song} {self.topic} {self.main_character}")

    def character (self):
               print(f"\nThe main character of this song, is a {self.main_character}.")


class Sense(Song):
     def __init__ (self, group_name, singer, song, topic, main_character, sense="passion and its consequences."):
            Song. __init__(self, group_name, singer, song, topic, main_character )
            self.sense = sense

     def print_sense(self):
         print(f"\nThe topic of song '{self.song}' is a {self.topic}, but which is more important, is the sense of a song. Namely {self.sense}")


if __name__ == '__main__':  
        group = Musical_Group("King and the Clown", "Andrew Knyazev (Knyaz)", "Joker")
        group.what_the_song()

        song = Song("King and the Clown", "Andrew Knyazev (Knyaz)", "Joker", "passion for gambling", "gambler")
        song.character()

        sen = Sense("King and the Clown", "Andrew Knyazev (Knyaz)", "Joker", "passion for gambling", "gambler")
        sen.print_sense()