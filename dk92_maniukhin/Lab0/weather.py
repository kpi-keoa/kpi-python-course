from pyowm import OWM

owm = OWM("d5f00b90f10766ad087532d4504376fd")
mgr = owm.weather_manager()

def getTown():
    town = mgr.weather_at_place(town_name)
    weatherInfo = town.weather

    return weatherInfo

def getTemp(weatherInfo):
    temperature = weatherInfo.temperature('celsius')
    t = temperature['temp']
    t_fl = temperature['feels_like']
    t_max = temperature['temp_max']
    t_min = temperature['temp_min']

    return print('Температура: ' + str(t), 'Ощущается: ' + str(t_fl), 'Максимальная: ' + str(t_max), 'Минимальная: ' + str(t_min), sep ='°C\n')

def getHumWind(weatherInfo):
    wind = weatherInfo.wind()['speed']
    humidity = weatherInfo.humidity

    return print('Скорость ветра: ' + str(wind) + str(' м/с'), 'Влажность: ' + str(humidity) + str('%'), sep ='\n')

town_name = input("Введите название города: ")
info = getTown()
getTemp(info)
getHumWind(info)
