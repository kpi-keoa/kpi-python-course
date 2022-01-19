FigureDoc = '''
                                                     _:_
                                                    '-.-'
                                           ()      __.'.__
                                        .-:--:-.  |_______|
                                 ()      \____/    \=====/
                                 /\      {====}     )___(
                      (\=,      //\\\      )__(      |   |
      __    |'-'-'|  //  .\    (    )    /____\     |   |
     /  \   |_____| (( \_  \    )__(      |  |      |   |
     \__/    |===|   ))  `\_)  /____\     |  |      |   |
    /____\   |   |  (/     \    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\    /____\    /_____\\
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
   (______)(_______)(_______)(________)(________)(_________)
| The "Shape" object defines one game unit                   |
| which does not have a class but can also have a color and  |
| coordinates. Thus it is possible to redefine killed figure | 
| and return to the game without creating a new one          |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
'''
PawnDoc = '''
       __
      /  \\
      \__/
     /____\\
      |  |
      |__|
     (====)
     }===={
    (______)
| Moves forward one space vertically. From source                             |
| position can also make the first move on two fields                         |
| forward. Hits one field diagonally forward. When                            |
| Making a move on two fields can be the next move                            |
| taken on the pass by the opponent's pawn. The only figure                   | 
| in chess, in which the usual move and a move with a capture                 |
| differ. If during the game the pawn reaches                                 |
| last horizontal, it turns into any shape                                    |
| at the request of the player, except for the king. As a rule, a pawn        |
| turns into the strongest figure - the queen, however                        |
| there are exceptions. At the beginning of the game, each player             |
| eight pawns, which are located on the second from the player                |
| Horizontal, covering the figures. The figure is the smallest of             |
| all included. Despite weakness, pawns are very important                    |
| in a chess game, as often form the basis                                    |
| defensive structure of the player, being a "filler"                         |
| field, and "cannon fodder." In the endgame, the role of pawns is many times |
| increases, usually due to the potential ability to achieve                  |
| last horizontal and turn into a strong figure.                              |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
RookDoc = '''
     |'-'-'|
     |_____|
      |===|
      |   |
      |   |
      )___(
     (=====)
     }====={
    (_______)
| Goes to any number of fields diagonally. In chaturanga and                   |
| shatranje walked through one field diagonally, being                         |
| like a horse, "jumping" figure (during the course of stepping over           |
| through their own and other people's figures standing in the way). In force  |
| coloring chessboard, the elephant moves only on                              |
| fields of the same color. |Depending on the color of the diagonal fields,    |
| on which this figure walks, the bishop is called light-squared               |
| Or blackfield.  At the beginning of the game, each player has                |
| two bishops - light-squared and dark-squared, white c1 and f1,               |
|black c8 and f8. Belongs to the class of "light figures"                      |
| (together with the horse). In a chess set, the height of the elephant        |
| usually below the king and queen. Its upper part looks like                  |
| drops (or hood) with a pointed upwards, represents                           |
| is a stylization of the attire of Catholic and Anglican bishops.             |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
HorseDoc = '''
      (\\=,
     //  .\\
    (( \_  \\
     ))  `\\_)
    (/     \\
     | _.-'|
      )___(
     (=====)
     }====={
    (_______)
|Может пойти на одно из полей, ближайших к тому, на котором      |
|он стоит, но не на той же самой горизонтали, вертикали или      |
|диагонали, то есть он ходит русской буквой «Г» (или латинской   |
|«L»).[1] Всегда попадает на поле противоположного цвета.        |
|Одна из двух фигур (вторая король), ход которой не изменился    |
|со времён чатуранги. В начале партии у каждого игрока два коня, |
|расположенные рядом с ладьями — белые кони b1 и g1, чёрные      |
|b8 и g8. Относится к «лёгким фигурам». В шахматном комплекте    |
|имеет вид конской головы на круглой подставке.                  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
ElephantDoc = '''
        ()
        /\\
       //\\\\
      (    )
       )__(
      /____\\
       |  |
       |  |
      /____\\
     (======)
     }======{
    (________)
| Goes to any number of fields vertically or horizontally. Can               |
| Participate in castling. | At the beginning of the game, each player has   |
| two rooks located on the extreme fields of the first or eighth             |
| horizontals - white rooks on a1 and h1, black on a8 and h8. How            |
| and the queen, is classified by theory as a "heavy piece". Figure          |
| usually looks like a stylized round fortress (or siege)                    |
| towers (which corresponds to its European name, - "tour" - with            |
| different languages ​​translated precisely as "fortress tower").             |
| In the old Russian chess sets looked like a stylized                       |
| ship (rook). | According to some assumptions, various                      |
| name of this figure associated with its original name                      |
| and view. | In chaturanga, it was called "chariot", that is, "rath".       |
| In Arabic shatranj, the name turned into "Rukh" (there was in              |
| mind Bird Roc). Her stylized images, supposedly                            |
| chess historians in Russia were mistaken for images visually               |
| similar Russian rook, from which came the Russian name of the piece.       | 
| In Europe, the image of the figure was associated with the name, consonant |
| with "rook" (cliff, tower), as a result of the corresponding European      |
| chess piece began to be depicted as a fortress tower.                      |
| Another name for the boat - "tour".                                        |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
QueenDoc = '''
        ()
     .-:--:-.
      \____/
      {====}
       )__(
      /____\\
       |  |
       |  |
       |  |
       |  |
      /____\\
     (======)
     }======{
    (________)
| The strongest piece, because it goes to any number of fields on           |
| vertical, horizontal or diagonal - combines the moves                     |
| rook and bishop. Initially (in the old Arabic shatranj) queen             |
| went only one square diagonally and was a weak piece.                     |
| The transformation of the queen into the most powerful figure has already |
| happened in European chess. In modern chess theory, the queen             |
| is a "heavy piece" (along with the rook). Appearance of the figure        |
| in traditional "staunton" chess is similar to the king, but               |
| The figure is crowned with a small ball and, unlike the king,             |
| somewhat lower (king, above the queen and crowned with a cross). Second,  |
| colloquial name of the queen - "queen".                                   |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
KingDoc = '''
        _:_
       '-.-'
      __.'.__
     |_______|
      \=====/
       )___(
       |   |
       |   |
       |   |
       |   |
       |   |
       |   |
      /_____\\
     (=======)
     }======={
    (_________)
| The most valuable figure, since the irremovable threat of capture (this |
| the situation is called "checkmate") means losing the game. Walks on    |
| one field vertically, horizontally or diagonally. In addition,          |
| may participate in castling. Included chess pieces king  the highest    | 
| figure, one of the two highest figures (the second - queen).            |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
