import time
import random
import sys
import msvcrt
from tkinter import *
import keyboard 


MONSTER_ENEMY = ('Rei', 'Player')
MOODS = ('bad', 'avarage', 'good')
RANKS = ('low', 'medium', 'high')

enemy = 0
fighter = 0

player_health = 100
player_attack = 20

rei_love = 50
rei_health = 100
rei_attack = 30 

monster_health = 0
monster_attack = 0

class Monster:
    def init (self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)
    def info (self):
        global monster_health
        global monster_attack
        if self.rank == 'high' and self.mood == 'bad':
            monster_health = 400
            monster_attack = 60
            print ('Вы видите сверепого предводителя орков')
        elif self.rank == 'high' and self.mood == 'avarage':
            monster_health = 400
            monster_attack = 50
            print ('Вы видите предводителя орков')
        elif self.rank == 'high' and self.mood == 'good':
           monster_health = 400
           monster_attack = 30
           print ('Вы видите пьяного предводителя орков')
        elif self.rank == 'medium' and self.mood == 'bad':
           monster_health = 300
           monster_attack = 50
           print ('Вы видите сверепого орка')
        elif self.rank == 'medium' and self.mood == 'avarage':
            monster_health = 300
            monster_attack = 40
            print ('Вы видите орка')
        elif self.rank == 'medium' and self.mood == 'good':
           monster_health = 300
           monster_attack = 20
           print ('Вы видите пьяного орка')
        elif self.rank == 'low' and self.mood == 'bad':
           monster_health = 200
           monster_attack = 30
           print ('Вы видите сверепого гоблина')
        elif self.rank == 'low' and self.mood == 'avarage':
            monster_health = 200
            monster_attack = 20
            print ('Вы видите гоблина')
        elif self.rank == 'low' and self.mood == 'good':
           monster_health = 200
           monster_attack = 10
           print ('Вы видите пьяного гоблина')
        else:
           print ('БЕЛКА! У рабзработчика...')

def fight ():
    global player_health
    global monster_health
    global rei_health
    fighter = random.choice(MONSTER_ENEMY)
    while monster_health > 0 and player_health > 0 and rei_health > 0:
        print(
            'Рэй:' '''Нападай, скоре!'''
            )
        keyboard.wait('space') 
        if fighter == 'Player':
            print(
                'Одноврменно с Рэем, ты кидаешься на монстра голыми руками и вместе вы наносите {} урона!'
                .format(player_attack + rei_attack))
            monster_health -= (player_attack + rei_attack)
            keyboard.wait ('space') 
            print(
                'Монстр не стал ждать и нанёс вам {} урона'
                .format(monster_attack))
            player_health -= monster_attack
            keyboard.wait ('space')
        else:
             print(
                'Одноврменно с Рэем, ты кидаешься на монстра голыми руками и вместе вы наносите {} урона!'
                 .format(player_attack + rei_attack))
             monster_health -= (player_attack + rei_attack)
             keyboard.wait ('space') 
             print(
                 'Монстр не стал ждать и нанёс вам {} урона'
                 .format(monster_attack))
             rei_health -= monster_attack
             keyboard.wait ('space')
    if player_health > 0 and rei_health > 0:
        print ('Монстр уничтожен!')
        keyboard.wait ('space')
    else:
        if rei_health <= 0:
            print (
                'Рэй падает без сознания - это конец.'
                )
            keyboard.wait ('space')
        elif player_health <= 0:
             print (
                'Ты больше не можешь сражаться, тело слабеет и всё вокруг темнеет - это конец.'
                )
             keyboard.wait ('space')
            
def acquaintance ():
    print (
    ' Добро пожаловать в пробную версию текстового квеста "Rai".'
    )
    print (
    'Нажмите клавишу' ''' 'пробел' ''' 'для продолжения...'
    )
    keyboard.wait('space') 
    print (
    'Вы бежите во тьме, слыша за собой цокот копыт и скрежет метала, которые становятся всё громче.'
    )
    keyboard.wait('space')
    print (
    'Страх переполняет твоё сердце, ноги уже устали бежать, а руки порезаны о колючие кусты.'
    )
    keyboard.wait('space')
    print (
    'Внезапно кто-то хватает за руку и тянет наверх.'
    )
    keyboard.wait('space')
    print (
    'Незнакомец :' ''' 'Тссс! *шепотом* Сиди тихо и не дергайся.' '''
    )
    keyboard.wait('space')
    print (
    'Под вами пробежала огромная толпа монстров.'
    )
    keyboard.wait('space')
    print (
    'Гоблин на коне:' ''' 'Она не могла далеко уйти! Ищите! Вперед! Хозяин голоден!' '''
    )
    keyboard.wait('space')
    print (
    'Не теряя времени, монстры понеслись вперёд. Подождав, пока их не станет слышно ты и твой спаситель спустились вниз.'
    )
    keyboard.wait('space')
    print (
    'Незнакомец :' ''' 'Хозяин совсем обленился, вдимо, раз на охоту за девицей отправляет своих слуг. Как тебя зовут то?' '''
    )
    keyboard.wait('space')
    player_name = input(
        'Меня зовут: '
    )
    print (
    player_name,':' ''' А тебя? ''' ' '
    )
    keyboard.wait('space')
    print (
    'Незнакомец :' '''Рэй '''
    )
    keyboard.wait('space')
    print (
    'Внезапно из кустов вылез ещё один монстр. Ты оцениваешь его стороны и понимаешь, что: ' 
    , end= '')
    enemy = Monster()
    enemy.init()
    enemy.info()
    keyboard.wait('space')
    fight() 
    return 0

acquaintance()

