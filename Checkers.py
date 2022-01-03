# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:59:58 2019

@author: User1
"""

import pygame
global selected
width=8
length=8
widthS=80
heightS=80
margin=10
black=(0, 0, 0)
red=(255, 166, 220)
green=(154, 228, 255)
white=(255, 255, 255)
blue=(62, 255, 147)
redKing=(202, 72, 253)
greenKing=(44, 95, 255)
pygame.init()
windowSize=[(widthS)*width, (heightS)*length]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Checkers")
boardState=[]
canTake=[]

def populateBoard(board, team, y, x):
    if y%2==0:
        if x%2==0:
            board[(width*y)+x]=team
        else:
            board[(width*y)+x]=0
    else:
        if x%2!=0:
            board[(width*y)+x]=team
        else:
            board[(width*y)+x]=0
def createBoard(board):
    global selected
    selected=None
    i=0
    while i<(width*length):
        boardState.append(0)
        i+=1
    y=0
    while y<length:
        x=0
        while x<width:
            if y<3:
                populateBoard(board, 1, y, x)
            elif y>4:
                populateBoard(board, 2, y, x)
            x+=1
        y+=1
                

def drawBoard(turn):
    global selected
    y=0
    while y<length:
        x=0
        while x<width:
            color=white
            if boardState[(y*8)+x]==0:
                if len(canTake)==0:
                    if turn%2==0:
                        if selected!=None:
                            if boardState[selected]==2:
                                if selected!=None and (selected==(y*8)+x+9 or selected==(y*8)+x+7) and y+1==int(selected/8):
                                    color=blue
                            else:
                                if selected!=None and (selected==(y*8)+x+9 or selected==(y*8)+x+7 or selected==(y*8)+x-7 or selected==(y*8)+x-9) and (y+1==int(selected/8) or y-1==int(selected/8)):
                                    color=blue
                    else:
                        if selected!=None:
                            if boardState[selected]==1:
                                if selected!=None and (selected==(y*8)+x-9 or selected==(y*8)+x-7) and y-1==int(selected/8):
                                    color=blue
                            else:
                                if selected!=None and (selected==(y*8)+x+9 or selected==(y*8)+x+7 or selected==(y*8)+x-7 or selected==(y*8)+x-9) and (y+1==int(selected/8) or y-1==int(selected/8)):
                                    color=blue
                else:
                    i=0
                    while i<len(canTake):
                        if selected==canTake[i] and (y*8+x)==canTake[i+2]:
                            color=blue
                        i+=3
                if color!=blue:
                    if y%2==0:
                        if x%2==0:
                            color=black
                        else:
                            color=white
                    else:
                        if x%2==0:
                            color=white
                        else:
                            color=black
            elif boardState[(y*8)+x]==1:
                color=red
            elif boardState[(y*8)+x]==3:
                color=redKing
            elif boardState[(y*8)+x]==2:
                color=green
            else:
                color=greenKing
            pygame.draw.rect(screen, color, [(widthS)*x, (heightS)*y, widthS, heightS])
            x+=1
        y+=1
    pygame.display.flip()
    
def play(turn):
    global selected
    if turn%2==0:
        if 2 not in boardState and 4 not in boardState:
            print("Pink Wins")
            pygame.quit() 
        curPlayer=2
        opponent=1
        shift1=9
        shift2=7
        shift3=1
        king=0
    else:
        if 1 not in boardState and 3 not in boardState:
            print("Blue Wins")
            pygame.quit() 
        curPlayer=1
        opponent=2
        shift1=-9
        shift2=-7
        shift3=-1
        king=7
        
    i=0
    while i<len(boardState):
        if boardState[i]==curPlayer+2:
            if i-2*shift1<len(boardState) and i-2*shift1>0:
                if (boardState[i-shift1]==opponent or boardState[i-shift1]==opponent+2) and int(i/8)==int((i-shift1)/8)+shift3 and boardState[i-2*shift1]==0 and int(i/8)==int((i-2*shift1)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift1)
                    canTake.append(i-2*shift1)
                if (boardState[i-shift2]==opponent or boardState[i-shift2]==opponent+2) and int(i/8)==int((i-shift2)/8)+shift3 and boardState[i-2*shift2]==0 and int(i/8)==int((i-2*shift2)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift2)
                    canTake.append(i-2*shift2)
            elif i-2*shift2<len(boardState) and i-2*shift2>0:
                if (boardState[i-shift2]==opponent or boardState[i-shift2]==opponent+2) and int(i/8)==int((i-shift2)/8)+shift3 and boardState[i-2*shift2]==0 and int(i/8)==int((i-2*shift2)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift2)
                    canTake.append(i-2*shift2)
            if i+2*shift1<len(boardState) and i+2*shift1>0:
                if (boardState[i+shift1]==opponent or boardState[i+shift1]==opponent+2) and int(i/8)==int((i+shift1)/8)-shift3 and boardState[i+2*shift1]==0 and int(i/8)==int((i+2*shift1)/8)-2*shift3:
                    canTake.append(i)
                    canTake.append(i+shift1)
                    canTake.append(i+2*shift1)
                if (boardState[i+shift2]==opponent or boardState[i+shift2]==opponent+2) and int(i/8)==int((i+shift2)/8)-shift3 and boardState[i+2*shift2]==0 and int(i/8)==int((i+2*shift2)/8)-2*shift3:
                    canTake.append(i)
                    canTake.append(i+shift2)
                    canTake.append(i+2*shift2)
            elif i+2*shift2<len(boardState) and i+2*shift2>0:
                if (boardState[i+shift2]==opponent or boardState[i+shift2]==opponent+2) and int(i/8)==int((i+shift2)/8)-shift3 and boardState[i+2*shift2]==0 and int(i/8)==int((i+2*shift2)/8)-2*shift3:
                    canTake.append(i)
                    canTake.append(i+shift2)
                    canTake.append(i+2*shift2)
        elif boardState[i]==curPlayer:
            if i-2*shift1<len(boardState) and i-2*shift1>0:
                if (boardState[i-shift1]==opponent or boardState[i-shift1]==opponent+2) and int(i/8)==int((i-shift1)/8)+shift3 and boardState[i-2*shift1]==0 and int(i/8)==int((i-2*shift1)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift1)
                    canTake.append(i-2*shift1)
                if (boardState[i-shift2]==opponent or boardState[i-shift2]==opponent+2) and int(i/8)==int((i-shift2)/8)+shift3 and boardState[i-2*shift2]==0 and int(i/8)==int((i-2*shift2)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift2)
                    canTake.append(i-2*shift2)
            elif i-2*shift2<len(boardState) and i-2*shift2>0:
                if (boardState[i-shift2]==opponent or boardState[i-shift2]==opponent+2) and int(i/8)==int((i-shift2)/8)+shift3 and boardState[i-2*shift2]==0 and int(i/8)==int((i-2*shift2)/8)+2*shift3:
                    canTake.append(i)
                    canTake.append(i-shift2)
                    canTake.append(i-2*shift2)
        i+=1
    while True:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (widthS)
                row = pos[1] // (heightS)
                if selected==None:
                    if boardState[(row*8)+column]==curPlayer:
                        selected=row*8+column
                        drawBoard(turn)
                elif boardState[selected]==curPlayer+2:
                    if len(canTake)==0:
                        if boardState[(row*8)+column]==0 and (selected==(row*8)+column+shift1 or selected==(row*8)+column+shift2 or selected==(row*8)+column-shift2 or selected==(row*8)+column-shift1) and (row+shift3==int(selected/8) or row-shift3==int(selected/8)):
                            boardState[selected]=0
                            boardState[(row*8)+column]=curPlayer+2
                            selected=None
                            drawBoard(turn)
                            return True
                    else:
                        if boardState[(row*8)+column]==curPlayer or boardState[(row*8)+column]==curPlayer+2:
                            selected=row*8+column
                            drawBoard(turn)
                        else:
                            i=0
                            while i<len(canTake):
                                if selected==canTake[i] and (row*8)+column==canTake[i+2]:
                                    boardState[selected]=0
                                    boardState[(row*8)+column]=curPlayer+2
                                    boardState[canTake[i+1]]=0
                                    selected=None
                                    drawBoard(turn)
                                    canTake.clear()
                                    pos=row*8+column
                                    if pos-2*shift1<len(boardState) and pos-2*shift1>0:
                                        if (boardState[pos-shift1]==opponent or boardState[pos-shift1]==opponent+2) and int(pos/8)==int((pos-shift1)/8)+shift3 and boardState[pos-2*shift1]==0 and int(pos/8)==int((pos-2*shift1)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift1)
                                            canTake.append(pos-2*shift1)
                                        if (boardState[pos-shift2]==opponent or boardState[pos-shift2]==opponent+2) and int(pos/8)==int((pos-shift2)/8)+shift3 and boardState[pos-2*shift2]==0 and int(pos/8)==int((pos-2*shift2)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift2)
                                            canTake.append(pos-2*shift2)
                                    elif pos-2*shift2<len(boardState) and pos-2*shift2>0:
                                        if (boardState[pos-shift2]==opponent or boardState[pos-shift2]==opponent+2) and int(pos/8)==int((pos-shift2)/8)+shift3 and boardState[pos-2*shift2]==0 and int(pos/8)==int((pos-2*shift2)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift2)
                                            canTake.append(pos-2*shift2)
                                    if pos+2*shift1<len(boardState) and pos+2*shift1>0:
                                        if (boardState[pos+shift1]==opponent or boardState[pos+shift1]==opponent+2) and int(pos/8)==int((pos+shift1)/8)-shift3 and boardState[pos+2*shift1]==0 and int(pos/8)==int((pos+2*shift1)/8)-2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos+shift1)
                                            canTake.append(pos+2*shift1)
                                        if (boardState[pos+shift2]==opponent or boardState[pos+shift2]==opponent+2) and int(pos/8)==int((pos+shift2)/8)-shift3 and boardState[pos+2*shift2]==0 and int(pos/8)==int((pos+2*shift2)/8)-2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos+shift2)
                                            canTake.append(pos+2*shift2)
                                    elif pos+2*shift2<len(boardState) and pos+2*shift2>0:
                                        if (boardState[pos+shift2]==opponent or boardState[pos+shift2]==opponent+2) and int(pos/8)==int((pos+shift2)/8)-shift3 and boardState[pos+2*shift2]==0 and int(pos/8)==int((pos+2*shift2)/8)-2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos+shift2)
                                            canTake.append(pos+2*shift2)
                                    if len(canTake)==0:
                                        return True
                                i+=1
                else:
                    if len(canTake)==0:
                        if boardState[(row*8)+column]==0 and (selected==(row*8)+column+shift1 or selected==(row*8)+column+shift2) and row+shift3==int(selected/8):
                            boardState[selected]=0
                            if row==king or boardState[selected]==curPlayer+2:
                                boardState[(row*8)+column]=curPlayer+2
                            else:
                                boardState[(row*8)+column]=curPlayer
                            selected=None
                            drawBoard(turn)
                            return True
                    else:
                        if boardState[(row*8)+column]==curPlayer or boardState[(row*8)+column]==curPlayer+2:
                            selected=row*8+column
                            drawBoard(turn)
                        else:
                            i=0
                            while i<len(canTake):
                                if selected==canTake[i] and (row*8)+column==canTake[i+2]:
                                    boardState[selected]=0
                                    if row==king or boardState[selected]==curPlayer+2:
                                        boardState[(row*8)+column]=curPlayer+2
                                    else:
                                        boardState[(row*8)+column]=curPlayer
                                    boardState[canTake[i+1]]=0
                                    selected=None
                                    drawBoard(turn)
                                    canTake.clear()
                                    pos=row*8+column
                                    if pos-2*shift1<len(boardState) and pos-2*shift1>0:
                                        if (boardState[pos-shift1]==opponent or boardState[pos-shift1]==opponent+2) and int(pos/8)==int((pos-shift1)/8)+shift3 and boardState[pos-2*shift1]==0 and int(pos/8)==int((pos-2*shift1)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift1)
                                            canTake.append(pos-2*shift1)
                                        if (boardState[pos-shift2]==opponent or boardState[pos-shift2]==opponent+2) and int(pos/8)==int((pos-shift2)/8)+shift3 and boardState[pos-2*shift2]==0 and int(pos/8)==int((pos-2*shift2)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift2)
                                            canTake.append(pos-2*shift2)
                                    elif pos-2*shift2<len(boardState) and pos-2*shift2>0:
                                        if (boardState[pos-shift2]==opponent or boardState[pos-shift2]==opponent+2) and int(pos/8)==int((pos-shift2)/8)+shift3 and boardState[pos-2*shift2]==0 and int(pos/8)==int((pos-2*shift2)/8)+2*shift3:
                                            canTake.append(pos)
                                            canTake.append(pos-shift2)
                                            canTake.append(pos-2*shift2)
                                    if len(canTake)==0:
                                        return True
                                i+=1
                                        
                if boardState[(row*8)+column]==curPlayer or boardState[(row*8)+column]==curPlayer+2:
                    selected=row*8+column
                    drawBoard(turn)
                
turn=0
createBoard(boardState)
drawBoard(turn)
while True:
    if play(turn):
        turn+=1
#pygame.time.delay(8000)
#pygame.quit()