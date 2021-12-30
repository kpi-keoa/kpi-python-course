#! /usr/bin/env python3

from pathlib import Path
from random import randint
from pydub import AudioSegment
from pydub.playback import play
import argparse

def game(highscore):

    r = randint(1, 5)
    i = 0
    
    pathlist = Path.home().glob('**/musdir/*.mp3')
    for path in pathlist:
        i = i + 1
        path_in_str = str(path)
        print(path_in_str)
        if(i == r):
            path_in_str = str(path)
            sound = AudioSegment.from_mp3(path_in_str)
            play(sound)
    
    print('What played out of this?')

    parser = argparse.ArgumentParser()
    """Positional arguments"""
    parser.add_argument('l', type=int, help='Track number: ')
    args = parser.parse_args()
    
    if(args.l == r):
        print('GOOD!')
        highscore = highscore + 1
        game(highscore)
    else:
        print('Highscore: ', highscore)

game(0)
