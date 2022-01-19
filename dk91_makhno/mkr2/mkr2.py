#!/usr/bin/env python3
import pygame
import time
import random
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("len", type=int)
args = parser.parse_args()

def play(file_name, len):
    

    pygame.init()
    song = pygame.mixer.music
    song.load("musdir/" + file_name)
    clock = pygame.time.Clock()
    song.play(0, random.randint(0, 120))

    while True:
        clock.tick(60)
        time.sleep(len)
        song.stop()
        break
    pygame.quit()

def game(name_song):
    n = 0
    list_songs = [name_song, random.choice(os.listdir("musdir")), random.choice(os.listdir("musdir")), random.choice(os.listdir("musdir"))]
    random.shuffle(list_songs)
    while n != 4:
        print((n + 1), list_songs[n])
        n = n + 1
    key = int(input("Сhoose the correct answer!  "))
    if name_song == list_songs[key-1]:
        return 1
    else:
        return 0


def main():
    score = -1
    i = 1
    while i != 0:
        score += i
        name_song = random.choice(os.listdir("musdir"))
        play(name_song, args.len)
        i = game(name_song)

    print("your score : ", score)

main()