#!/usr/bin/env python3

"""This module is responsible for music quiz."""

import random

import argparse
import time
import pygame

parser = argparse.ArgumentParser()
parser.add_argument(
    '--song',
    choices=[
        'небеса',
        'я тебе не верю',
        'младший лейтенант',
        'paparazzi',
        'women of the hour',
        'жить в кайф',
        'шантаж',
    ],
    type=str,
    help='Song title',
)
args = parser.parse_args()
songs = args.song
user_score = 0
music = [
    '1.mp3',
    '2.mp3',
    '3.mp3',
    '4.mp3',
    '5.mp3',
    '6.mp3',
    '7.mp3',
]


def welcome():
    """Return the greeting."""
    print('Welcome to Music Quiz!')


def variants():
    """Return the variants of answer."""
    print(
"""
The variants of answer:    
Валерий Меладзе - Небеса
Григорий Лепс - Я тебе не верю
Ирина Алегрова - Младший лейтенант
Kim Dracula - Paparazzi
Stela Cole - Woman of the hour
Макс Корж - Жить в кайф
Макс Корж - Шантаж
""",
    )


def ready():
    """Return the result of the module operation."""
    answer = input('Are you ready to play the Quiz?(Y/N): ')
    if answer.upper() == 'Y':
        play()
        game()
    else:
        again()


def play():
    """Return a random song."""
    filename = random.choice(music)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(random.uniform(0, 180))
    time.sleep(5)
    pygame.mixer.music.stop()


def game():
    """Return scores and check the user answer."""
    global user_score
    songs = input('Write the name of song: ')
    if (
        songs == 'небеса'
        or songs == 'я тебе не верю'
        or songs == 'младший лейтенант'
        or songs == 'paparazzi'
        or songs == 'women of the hour'
        or songs == 'жить в кайф'
        or songs == 'шантаж'
    ):
        user_score += 1
        print('Correct answer! Congratulations!')
        print('The user scores: ', user_score)
        play()
        game()
    else:
        print('Wrong answer!')
        print('The user score: ', user_score)
        again()


def file():
    """Return the higher scores."""
    with open('scores.txt', 'a') as file:
            data = str(user_score)
            file.write(data)
            file.write('\n')
    infile = open('scores.txt','r')
    print('The higher scores: ',max(infile))
        

def again():
    """Do the user survey."""
    calc_again = input(
        """
Do you want to play again?
Please type Y for YES or N for NO.
""",
)
    if calc_again.upper() == 'Y':
        play()
        game()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


if __name__ == '__main__':
    welcome()
    variants()
    ready()
    file()
