from document import (FigureDoc, PawnDoc, RookDoc, 
              HorseDoc, ElephantDoc, QueenDoc, KingDoc)

class Figure:
	def __init__(self, pos_x, pos_y, color):
        #Numbers (числа)
		self.x = pos_x
		self.y = pos_y
        #Strings (строки)
		self.color = color
        #Dictionaries (словари)
		self.doc = {
            'Figure' : FigureDoc,
            'Pawn' : PawnDoc,
            'Rook' : RookDoc,
            'Horse' : HorseDoc,
            'Elephant' : ElephantDoc,
            'Queen' : QueenDoc,
            'King' : KingDoc
            }
        #Lists (списки)
		self.story = []
        #Tuples (кортежи)
		self.tuple_key = tuple('♟','♜','♞','♝','♛','♚',
                               '♙','♖','♘','♗','♕','♔')
        #Sets (множества)
		self.set1 = set(self.story)
        #Boolean (логический тип данных)
		self.condition = True

	def __str__(self):
		return self.doc[type(self).__name__]

	def __eq__(self, other):
		if (self.color == other.color):
			print('Color',self.color, 'matches')
			return True
		else:
			print('Color doesn''t match!')
			return False

	def __gt__(self, other):
		if(self.x != other.x | self.x != other.y):
			print('Move on X',other.x, 'Y', other.y)
			return other.x, other.y
		else:
			print('figure in place')


class Pawn(Figure):
    def __init__(self, pos_x, pos_y, color,):
        super().__init__(pos_x, pos_y, color)
        


class Rook(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

class Horse(Figure):
   def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

class Elephant(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

class Queen(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

class King(Figure):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

if __name__ == '__main__':
    f1 = Figure(4, 5, 'white')
    p1 = Pawn(2, 5, 'white')
    r1 = Rook(1, 3, 'black')
    h1 = Horse(4, 7, 'black')
    e1 = Elephant(1, 2, 'black')
    q1 = Queen(1, 1, 'white')
    k1 = King(2, 1, 'white')

    print(f1, p1, r1, h1, e1, q1, k1)
    f1 == p1
    r1 == q1
    f1 > r1
    f1 > f1