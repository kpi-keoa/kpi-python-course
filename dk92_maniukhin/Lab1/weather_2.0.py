#!/usr/bin/env python3

'''
python3 -m timeit 'for i in range(10): print(i)'
-> result: 5000 loops, best of 5: 40.3 usec per loop

python3 -m timeit 'i=0' 'while i < 10: print(i); i+=1'
-> result: 5000 loops, best of 5: 42.6 usec per loop
'''

import pytz
from sys import argv, stderr
from datetime import datetime
from pyowm.owm import OWM

"""
This module was created to use the PyOWM API to get data about the weather in the city at the current time. Demo version.
"""

owm = OWM('d5f00b90f10766ad087532d4504376fd')
mgr = owm.weather_manager()


def get_city_timezone(city_name):
    """
    The function is designed to get the time zone by city name using the pytz library.

    Args:
        city_name (str): The name of the city which time zone is needed

    Returns:
        str: City time zone. Example: Europe/London
    """

    for country, cities in pytz.country_timezones.items():
        for city in cities:
            if city_name in city:
                city_time_zone = pytz.timezone(city)

                return city_time_zone


def get_current_weather(city_name):
    """
    The function to get information about the weather in the desired city.

    Args:
        city_name (str): The name of the city which weather information is needed

    Returns:
        dictionaries: Information about the weather in the city. Complete information on temperature, wind speed, humidity
    """

    place = mgr.weather_at_place(city_name)
    weather_info = place.weather

    return weather_info


def get_current_info(weather_info, /, user_temp_choice, *, user_wind_choice, kelvin_degree=273.15, miles=2.165):
    """
    The function to get information from dictionaries and print it.

    Args:
        weather_info (): Information about weather parameters in the form of dictionaries
        user_temp_choice(str): Used to select the user-selectable unit of measure for temperature
        user_wind_choice(str): Used to select a user-selectable unit of measure for speed.
        kelvin_degree(float): Used to convert temperature from degrees Kelvin to degrees Celsius
        miles(float): Used to convert speed from meter per seconds to miles per hour

    Returns:
        None: None
    """

    for key in weather_info.temp:
        if key == 'temp_kf':
            continue
        else:
            temps = weather_info.temp[key]
            print('-' * 25)
            if user_temp_choice == 'Celsius':
                output_temp = temps - kelvin_degree
                print(key, ' = ', round(output_temp, 1), '℃')

            elif user_temp_choice == 'Fahrenheit':
                output_temp = (temps - kelvin_degree) * 9 / 5 + 32
                print(key, ' = ', round(output_temp, 1), '°F')

    humidity = weather_info.humidity
    print('-' * 25)

    if user_wind_choice == 'mph':
        output_wind = weather_info.wind()['speed'] * miles
        print('wind_speed = ', round(output_wind, 1), 'mph', '\nhumidity = ', humidity, '%')
    else:
        output_wind = weather_info.wind()['speed']
        print('wind_speed = ', round(output_wind, 1), 'm/s', '\nhumidity = ', humidity, '%')


if len(argv) > 2 or len(argv) < 2:
    stderr.write('ERROR: Missed city name/You entered an invalid parameter.')
else:
    tz = get_city_timezone(argv[1])
    now = datetime.now(tz)
    time_now = now.strftime('%d-%m-%Y %H:%M')
    print('Weather current at ', time_now)
    get_current_info(get_current_weather(argv[1]), 'Fahrenheit', user_wind_choice='mph')
