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

class Board:
    def __init__(self):
        self.board = [[None]*8 for i in range(8)]
        self.turn = Color.WHITE
        self.board[4][4] = Rook(Color.BLACK, 4, 4)
        self.board[4][6] = King(Color.BLACK, 4, 6)
    def move(self, x1, y1, x2, y2):
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = None
        self.board[x2][y2].x = x2
        self.board[x2][y2].y = y2
        self.turn = Color.WHITE if self.turn == Color.BLACK else Color.BLACK
    
    #def indexOfLocatio
    
    def display(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[x][y] != None:
                    print(self.board[x][y].letter + " ", end="")
                else:
                    print("_ ", end="")
            print()
    
class Knight:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = "N" if color == Color.WHITE else "n"
    
    def availableMoves(self, board):
        moves = []
        x = self.x
        y = self.y
        for a,b in [[x-2,y-1],[x-2,y+1],[x-1,y-2],[x-1,y+2],[x+1,y-2],[x+1,y+2],[x+2,y-1],[x+2,y+1]]:
            if 0<=a<=7 and 0<=b<=7 and board[a][b] != self.color:
                moves.append([a,b])
        return moves

class Rook:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = "R" if color == Color.WHITE else "r"
    
    def availableMoves(self, board):
        moves = []
        x = self.x
        y = self.y
        for i in range(x+1,8):
            if board[i][y] == None:
                moves.append([i,y])
            elif board[i][y].color != self.color:
                moves.append([i,y])
                break
            else:
                break
        for i in range(x-1,-1,-1):
            if board[i][y] == None:
                moves.append([i,y])
            elif board[i][y].color != self.color:
                moves.append([i,y])
                break
            else:
                break
        for i in range(y+1,8):
            if board[x][i] == None:
                moves.append([x,i])
            elif board[x][i].color != self.color:
                moves.append([x,i])
                break
            else:
                break
        for i in range(y-1,-1,-1):
            if board[x][i] == None:
                moves.append([x,i])
            elif board[x][i].color != self.color:
                moves.append([x,i])
                break
            else:
                break
        return moves

class King:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = "K" if color == Color.WHITE else "k"
        
    def availableMoves(self, board):
        moves = []
        x = self.x
        y = self.y
        for a,b in [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]:
            if 0<=a<=7 and 0<=b<=7 and (board[a][b] == None or board[a][b].color != self.color):
                moves.append([a,b])
        return moves

board = Board()
board.display()
print(board.board[4][6].availableMoves(board.board))
