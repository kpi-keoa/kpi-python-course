

class ComputorGame:

  def __init__(self, station_name, release_name, developent_name):
      self.paltform_name = station_name
      self.release_game_name = release_name
      self.studio_development = developent_name

  def get_game_info(self):
      return (
          f"Имя платормы: {self.paltform_name}" 
          f"\nИмя игры: {self.release_game_name}" 
          f"\nИмя разработчика: {self.studio_development}"
     )
  #Створення обьекта батька від якого буде наслідування 


class Strategy(ComputorGame):

   def __init__(self, station_name, release_name, developent_name, number_of_players):
       super().__init__(station_name, release_name, developent_name)
       self.number_of_playerse = number_of_players


   def __eq__(self, other):
       return self.number_of_playerse == other.number_of_playerse

   def __lt__(self, other):
       return self.number_of_playerse < other.number_of_playerse

   def __le__(self, other):
       return self.number_of_playerse <= other.number_of_playerse

   def _repr_(self):
       return f"Игра была создана на {self.number_of_playerse} игроко"

   def get_game_info(self):
       return f"{super().get_game_info()} \nМаксимум игроков {self.number_of_playerse}\n"
   


class RPG(ComputorGame):

    def __init__(self,station_name, release_name, 
              developent_name, number_of_skills):
        super().__init__(station_name, release_name, developent_name)
        self.number_of_skills = number_of_skills

    def __str__(self):
        return f"В игре есть{self.number_of_skills} навыков"

    def get_game_info(self):
       return f"{super().get_game_info()} \nКоличство навыков {self.number_of_skills}\n"

class RTS(Strategy):

    def __init__(self,station_name, release_name,
              developent_name, number_of_players,map_size):
        super().__init__(station_name, release_name, developent_name, number_of_players)
        self.map_size = map_size

    def get_game_info(self):
       return f"{super().get_game_info()}Размер карт: {self.map_size}\n"
       

def work_check():
    print("Проверка работы!")

    civilization = Strategy("PC", "Civilization", "Sid Mair", 16)
    print(civilization.get_game_info())

    divinity = RPG("PC", "Divinity", "Biowar", 24)
    print(divinity.get_game_info())

    cac = RTS("PC","CaC","GSC",8,2)
    print(cac.get_game_info())

    civilization_2 = Strategy("PC","Civilization 2","Sid Mair",32)

    if(civilization_2 == civilization):
        print(civilization_2.release_game_name,"==",
                civilization.release_game_name)

    elif(civilization <= civilization_2):
        print(civilization.release_game_name,"<=",
                civilization_2.release_game_name)

    if(civilization < civilization_2):
        print(civilization.release_game_name,"<",
                civilization_2.release_game_name)


if __name__ == "__main__":

    work_check()