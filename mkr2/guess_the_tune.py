#!/usr/bin/env python3
from Resources.songs import songs
from Resources.users import users
from musdir import musdir
import random
import pickle

def main():
    username = login()
    print('hello', username, 'welcome to the music quiz')
    guessed_wrong_twice = False
    result = None
    while not guessed_wrong_twice:
        result = start_quiz()
        guessed_wrong_twice = result[1]
    score = result[0]
    print('you scored', score)
    leaderboard = leaderboard_updating(username, int(result[0]))
    print('The leaderboard:\n', leaderboard)

main()



def login():
    logged_in = False
    entered_username = None
    while not logged_in:
        entered_username = input("please enter username: ")
        if entered_username in users:
            entered_password = input('please enter password: ')
            if entered_password == users[entered_username]:
                logged_in = True
        else:
            print("password or username incorrect try again")
            logged_in = False

    return entered_username

def start_quiz():
    score = 0
    guessed_wrong_twice = False
    song_chosen = choosing_song()
    print('artists name is', song_chosen[1])
    first_letter = song_chosen[0][0]
    guess = input("the song begins with" + first_letter)
    if guess.lower == song_chosen[0]:
        score += 3
    else:
        guess = input("the song begins with " + first_letter)
        if guess.lower == song_chosen[0]:
            score += 1
        elif guess != song_chosen[0]:
            guessed_wrong_twice = True
    return score, guessed_wrong_twice


def choosing_song():
    song_chooser = random.randint(1, 3)
    song_artist = songs[song_chooser][1]
    song_name = songs[song_chooser][0]
    return song_name, song_artist

def leaderboard_updating(username, score=0):

    leaderboard = pickle.load(open("leaderboard.pickle", "rb"))

    index_row_list = [leaderboard.index(row) for row in leaderboard if username in row]
    index_row = int(index_row_list[0])
    if leaderboard[index_row][1] < score:
        leaderboard[index_row][1] = score

    leaderboard = sorted(leaderboard, key=lambda x: x[1])

    pickle.dump(leaderboard, open("leaderboard.pickle", "wb"))
    return leaderboard
