from enum import Enum
import tkinter
from tkinter import *
from win32api import GetSystemMetrics


class Color(Enum):
    WHITE = "w"
    BLACK = "b"

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
        self.inCheck = None
        self.blackKing = (4,0)
        self.whiteKing = (4,7)
        self.board[0][0] = Rook(Color.BLACK,0,0)
        self.board[1][0] = Knight(Color.BLACK,1,0)
        self.board[2][0] = Bishop(Color.BLACK,2,0)
        self.board[3][0] = Queen(Color.BLACK,3,0)
        self.board[4][0] = King(Color.BLACK,4,0)
        self.board[5][0] = Bishop(Color.BLACK,5,0)
        self.board[6][0] = Knight(Color.BLACK,6,0)
        self.board[7][0] = Rook(Color.BLACK,7,0)
        self.board[0][7] = Rook(Color.WHITE,0,7)
        self.board[1][7] = Knight(Color.WHITE,1,7)
        self.board[2][7] = Bishop(Color.WHITE,2,7)
        self.board[3][7] = Queen(Color.WHITE,3,7)
        self.board[4][7] = King(Color.WHITE,4,7)
        self.board[5][7] = Bishop(Color.WHITE,5,7)
        self.board[6][7] = Knight(Color.WHITE,6,7)
        self.board[7][7] = Rook(Color.WHITE,7,7)
        for i in range(8):
            self.board[i][1] = Pawn(Color.BLACK,i,1)
            self.board[i][6] = Pawn(Color.WHITE,i,6)
        
    def move(self, x1, y1, x2, y2):
        if self.board[x1][y1].letter.lower() == "k" or self.board[x1][y1].letter.lower() == "r":
            self.board[x1][y1].moved = True
        #if self.board[x1][y1].letter.lower() == "n":
            #if 
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
        print()
    
    def validMoveByCheck(self, x, y):
        kingColor = self.board[x][y].color
        
        #top check
        for i in range(1, y):
            if(self.board[x][y - i] != None and self.board[x][y - i].color == kingColor):
                break
            elif(self.board[x][y - i].letter == 'r' if kingColor == Color.WHITE else 'R') or (self.board[x][y - i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
        #bottom check
        for i in range(1, 7 - y):
            if(self.board[x][y + i] != None and self.board[x][y + i].color == kingColor):
                break
            elif(self.board[x][y + i].letter == 'r' if kingColor == Color.WHITE else 'R') or (self.board[x][y + i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
        #left check
        for i in range(1, x):
            if(self.board[x - i][y] != None and self.board[x - i][y].color == kingColor):
                break
            elif(self.board[x - i][y].letter == 'r' if kingColor == Color.WHITE else 'R') or (self.board[x - i][y].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
        #right check
        for i in range(1, 7 - x):
            if(self.board[x + i][y] != None and self.board[x + i][y].color == kingColor):
                break
            elif(self.board[x + i][y].letter == 'r' if kingColor == Color.WHITE else 'R') or (self.board[x + i][y].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
        #top left check
        for i in range(1, x if x < y else y):
            if(self.board[x - i][y - i] != None and self.board[x - i][y - i].color == kingColor):
                break
            elif (self.board[x - i][y - i].letter == 'b' if kingColor == Color.WHITE else 'B') or (self.board[x - i][y - i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
            elif kingColor == Color.WHITE and self.board[x - 1][y - 1].letter == 'p':
                return False
        #top right check
        for i in range(1, 7 - x if 7 - x < y else y): 
            if(self.board[x + i][y - i] != None and self.board[x + i][y - i].color == kingColor):
                break
            elif (self.board[x + i][y - i].letter == 'b' if kingColor == Color.WHITE else 'B') or (self.board[x + i][y - i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
            elif kingColor == Color.WHITE and self.board[x + 1][y - 1].letter == 'p':
                return False
        #bottom left check
        for i in range(1, x if x < 7 - y else 7 - y): 
            if(self.board[x - i][y + i] != None and self.board[x - i][y + i].color == kingColor):
                break
            elif (self.board[x - i][y + i].letter == 'b' if kingColor == Color.WHITE else 'B') or (self.board[x - i][y + i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
            elif kingColor == Color.BLACK and self.board[x - 1][y + 1].letter == 'P':
                return False
        #bottom right check
        for i in range(1, 7 - x if x > y else 7 - y): 
            if(self.board[x + i][y + i] != None and self.board[x + i][y + i].color == kingColor):
                break
            elif (self.board[x + i][y + i].letter == 'b' if kingColor == Color.WHITE else 'B') or (self.board[x + i][y + i].letter == 'q' if kingColor == Color.WHITE else 'Q'):
                return False
            elif kingColor == Color.BLACK and self.board[x + 1][y + 1].letter == 'P':
                return False
        for a,b in [[x-2,y-1],[x-2,y+1],[x-1,y-2],[x-1,y+2],[x+1,y-2],[x+1,y+2],[x+2,y-1],[x+2,y+1]]:
            if 0<=a<=7 and 0<=b<=7 and (self.board[a][b] != None and self.board[a][b].letter == 'n' if kingColor == Color.WHITE else 'N'):
                return False
        return True
    
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
            if 0<=a<=7 and 0<=b<=7 and (board[a][b] == None or board[a][b].color != self.color):
                moves.append([a,b])
        return moves

class Rook:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = "R" if color == Color.WHITE else "r"
        self.moved = False
    
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
        self.moved = False
        
    def availableMoves(self, board):
        moves = []
        x = self.x
        y = self.y
        for a,b in [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]:
            if 0<=a<=7 and 0<=b<=7 and (board[a][b] == None or board[a][b].color != self.color):
                moves.append([a,b])
        if not self.moved:
            if board[5][7 if self.color == Color.WHITE else 0] == None and board[6][7 if color == Color.WHITE else 0] == None and board[7][7 if self.color == Color.WHITE else 0] != None and board[7][7 if self.color == Color.WHITE else 0].letter.lower() == "r" and not board[7][7 if self.color == Color.WHITE else 0].moved:
                moves.append([0-0])
            if board[5][7 if self.color == Color.WHITE else 0] == None and board[6][7 if color == Color.WHITE else 0] == None and board[7][7 if self.color == Color.WHITE else 0] != None and board[7][7 if self.color == Color.WHITE else 0].letter.lower() == "r" and not board[7][7 if self.color == Color.WHITE else 0].moved:
                moves.append([0-0])
        return moves

class Pawn:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = 'P' if self.color == Color.WHITE else 'p'
        
    def availableMoves(self, board):
        moves = []
        if self.color == Color.BLACK:
            if board[self.x][self.y+1] == None:
                moves.append([self.x, self.y+1])
                if self.y == 1 and board[self.x][self.y+2] == None:
                    moves.append([self.x, self.y + 2])
            if self.x > 0 and board[self.x - 1][self.y + 1] != None and board[self.x - 1][self.y + 1].color == Color.WHITE:
                moves.append([self.x - 1, self.y + 1])
            if self.x < 7 and board[self.x + 1][self.y + 1] != None and board[self.x + 1][self.y + 1].color == Color.WHITE:
                moves.append([self.x - 1, self.y + 1])
        else:
            if board[self.x][self.y-1] == None:
                moves.append([self.x, self.y-1])
                if self.y == 6 and board[self.x][self.y-2] == None:
                    moves.append([self.x, self.y - 2])
            if self.x > 0 and board[self.x - 1][self.y - 1] != None and board[self.x - 1][self.y - 1].color == Color.BLACK:
                moves.append([self.x - 1, self.y - 1])
            if self.x < 7 and board[self.x + 1][self.y - 1] != None and board[self.x + 1][self.y - 1].color == Color.BLACK:
                moves.append([self.x + 1, self.y - 1])
        return moves
        
class Bishop:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = 'B' if self.color == Color.WHITE else 'b'
        
    def availableMoves(self, board):
        moves = []
        i = 1
        while self.x - i >= 0 and self.y - i >= 0:
            if board[self.x - i][self.y - i] == None:
                moves.append([self.x - i, self.y - i])
            elif board[self.x - i][self.y - i].color != self.color:
                moves.append([self.x - i, self.y - i])
                break
            else:
                break
            i += 1
        i = 1
        while self.x + i <= 7 and self.y - i >= 0:
            if board[self.x + i][self.y - i] == None:
                moves.append([self.x + i, self.y - i])
            elif board[self.x + i][self.y - i].color != self.color:    
                moves.append([self.x + i, self.y - i])
                break
            else:
                break
            i += 1
        i = 1
        while self.x - i >= 0 and self.y + i <= 7:
            if board[self.x - i][self.y + i] == None:
                moves.append([self.x - i, self.y + i])
            elif board[self.x - i][self.y + i].color != self.color:
                moves.append([self.x - i, self.y + i])
                break
            else:
                break
            i += 1
        i = 1
        while self.x + i <= 7 and self.y + i <= 7:
            if board[self.x + i][self.y + i] == None:
                moves.append([self.x + i, self.y + i])
            elif board[self.x + i][self.y + i].color != self.color:
                moves.append([self.x + i, self.y + i])
                break
            else:
                break
            i += 1
        return moves

class Queen():
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.letter = 'Q' if self.color == Color.WHITE else 'q'
        
    def availableMoves(self, board):
        moves = []
        i = 1
        x = self.x
        y = self.y
        while x - i >= 0 and y - i >= 0:
            if board[x - i][y - i] == None:
                moves.append([x - i, y - i])
            elif board[x - i][y - i].color != self.color:
                moves.append([x - i, y - i])
                break
            else:
                break
            i += 1
        i = 1
        while self.x + i <= 7 and self.y - i >= 0:
            if board[x + i][y - i] == None:
                moves.append([x + i, y - i])
            elif board[x + i][y - i].color != self.color:    
                moves.append([x + i][y - i])
                break
            else:
                break
            i += 1
        i = 1
        while x - i >= 0 and y + i <= 7:
            if board[x - i][y + i] == None:
                moves.append([x - i, y + i])
            elif board[x - i][y + i].color != self.color:
                moves.append([x - i, y + i])
                break
            else:
                break
            i += 1
        i = 1
        while x + i <= 7 and y + i <= 7:
            if board[x + i][y + i] == None:
                moves.append([x + i, y + i])
            elif board[x + i][y + i].color != self.color:
                moves.append([x + i, y + i])
                break
            else:
                break
            i += 1
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

class Game():
    def __init__(self):
        self.selected = []
        self.root = Tk()
        self.screen = Frame(self.root)
        self.root.title("Chess Board")
        self.board = Board()
        sWidth = GetSystemMetrics(0)
        sHeight = GetSystemMetrics(1)
        self.root.geometry(str(sWidth)+"x"+str(sHeight))
        self.screen.place(relx=.5, rely=.5, anchor="center")
        self.buttons = [[None] * 8 for i in range(8)]
        self.initializeBoard();
        self.root.mainloop()
    
    def initializeBoard(self):
        for row in range(0,len(self.board.board),1):
            for col in range(0,len(self.board.board[row]),1):
                if(row%2==0 and col%2==1) or (row%2==1 and col%2==0):
                    color = "#555555"
                else:
                    color = "#ffffff"
                if(self.board.board[col][row] == None):
                    b = Button(self.screen, relief=FLAT, foreground=color, background=color, activeforeground=color, activebackground=color, width=6, height=3, command= lambda row = row, col = col: self.handleButtonPress(col, row))
                    b.grid(row=row,column=col)
                else:
                    path = "images\\" + self.board.board[col][row].color.value + "_" + self.board.board[col][row].letter.lower() + ".png"
                    label = Label(self.screen)
                    label.img = PhotoImage(file=path).subsample(6)
                    photo = label.img
                    b = Button(self.screen, relief=FLAT, foreground=color, background=color, activeforeground=color, activebackground=color, width=46, height=50, image=photo, command = lambda row = row, col = col: self.handleButtonPress(col, row))
                    b.grid(row=row,column=col)
                self.buttons[col][row] = b
    
    def updateSquare(self, x, y):
        label = Label(self.screen)
        if self.board.board[x][y] != None:
            path = "images\\" + self.board.board[x][y].color.value + "_" + self.board.board[x][y].letter.lower() + ".png"
            label.img = PhotoImage(file=path).subsample(6)
        else:
            label.img = PhotoImage(file="").subsample(6)
        photo = label.img
        self.buttons[x][y].configure(width=46, height=50, image=photo)  
    def handleButtonPress(self, x, y):
        if len(self.selected)>0 and [x, y] in self.board.board[self.selected[0]][self.selected[1]].availableMoves(self.board.board):
            self.board.move(self.selected[0], self.selected[1], x, y)
            self.updateSquare(self.selected[0], self.selected[1])
            self.updateSquare(x, y)
            self.selected = []
        elif self.board.board[x][y] != None and self.board.board[x][y].color == self.board.turn:
            self.selected = [x, y]
            availableMoves = self.board.board[self.selected[0]][self.selected[1]].availableMoves(self.board.board)
            grid = self.buttons
            grid[x][y]["background"] = "#7a997a"
            grid[x][y]["image"] = tkimage
            for spotX,spotY in availableMoves:
                try:
                    grid[spotX][spotY]["background"] = "#7a997a"
                except IndexError:
                    continue
        else:
            self.selected = []
        #self.board.display()
                
Game()
'''
After each move check if that move gave check
Available moves do not include moves that keep the king in check
Always check if the combined available moves is greater than 0

Stalemate: when there are no available moves left to play
Checkmate: stalemate + check

'''
