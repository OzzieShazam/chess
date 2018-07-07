import tkinter
from tkinter import *
from win32api import GetSystemMetrics

boardArray = [[None]*8 for i in range(8)];
root = Tk();
screen = Frame(root);
def StartGame():
    root.title("Chess Board")
    sWidth = GetSystemMetrics(0);
    sHeight = GetSystemMetrics(1);
    root.geometry(str(sWidth)+"x"+str(sHeight))
    screen.place(relx=.5, rely=.5, anchor="center")
    boardArray = [['r','n','b','q','k','b','n','r'],['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],['R','N','B','Q','K','B','N','R']] 

    updateBoard(boardArray);
    root.mainloop()
    
    
def updateBoard(boardArray):
    for row in range(0,len(boardArray),1):
        for col in range(0,len(boardArray[row]),1):
            if(row%2==0 and col%2==1) or (row%2==1 and col%2==0):
                color = "#555555"
            else:
                color = "#ffffff"
            if(boardArray[row][col] == None):
                Button(screen, foreground=color, background=color, activeforeground=color, activebackground=color, width=6, height=3).grid(row=row,column=col)
            else:
                path = "images\"Color(boardArray[row][col]) + "_" + Pieces(boardArray[row][col]) + ".png"
                label = Label(screen)
                label.img = PhotoImage(file=path).subsample(6)
                photo = label.img
                Button(screen, foreground=color, background=color, activeforeground=color, activebackground=color, width=46, height=50, image=photo).grid(row=row,column=col)
                
def Pieces(p):
    return {
        'r': "rook",
        'n': "knight",
        'b': "bishop",
        'q': "queen",
        'k': "king",
        'p': "pawn"
    }[p.lower()]

def Color(c):
    return {
        True: "w",
        False: "b"
    }[c.isupper()]
    
StartGame()
