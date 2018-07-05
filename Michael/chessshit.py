from enum import Enum

class Color(Enum):
    WHITE = 0
    BLACK = 1
    
class Piece(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5
    
class Pawn:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = 'P' if self.color == Color.WHITE else 'p'
        
    def availableMoves(self, board):
        moves = []
        if self.color == Color.BLACK:
            if self.y == 1:
                moves.append([self.x, self.y + 2])
            if self.y != 7:
                moves.append([self.x, self.y + 1])
            if board[self.x - 1][self.y + 1] != None:
                moves.append([self.x - 1, self.y + 1])
            if board[self.x + 1][self.y + 1] != None:
                moves.append([self.x - 1, self.y + 1])
        else:
            if self.y == 6:
                moves.append([self.x, self.y - 2])
            if self.y != 0:
                moves.append([self.x, self.y - 1])
            if board[self.x - 1][self.y - 1] != None:
                moves.append(self.x - 1, self.y - 1)
            if board[self.x + 1][self.y - 1] != None:
                moves.append([self.x + 1, self.y - 1])
        return moves
        
class Bishop:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
    def availableMoves(self, board):
        moves = []
        i = 1
        while self.x - i >= 0 and self.y - i >= 0:
            if board[self.x - i][self.y - i] == None or board[self.x - i][self.y - i].color != self.color:
                moves.append([self.x - i, self.y - i])
            elif board[self.x - i][self.y - i].color == self.color:
                break
            i += 1
        i = 1
        while self.x + i <= 7 and self.y - i >= 0:
            if board[self.x + i][self.y - i] == None or board[self.x + i][self.y - i].color != self.color:
                moves.append([self.x + i, self.y - i])
            elif board[self.x + i][self.y - i].color == self.color:
                break
            i += 1
        i = 1
        while self.x - i >= 0 and self.y + i <= 7:
            if board[self.x - i][self.y + i] == None or board[self.x - i][self.y + i].color != self.color:
                moves.append([self.x - i, self.y + i])
            elif board[self.x - i][self.y + i].color == self.color:
                break
            i += 1
        i = 1
        while self.x + i <= 7 and self.y + i <= 7:
            if board[self.x + i][self.y + i] == None or board[self.x + i][self.y + i].color != self.color:
                moves.append([self.x + i, self.y + i])
            elif board[self.x + i][self.y + i].color == self.color:
                break
            i += 1
        return moves
class Board:
    def __init__(self):
        self.board = []
        self.turn = Color.WHITE