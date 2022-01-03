import random, math, pygame

black=(0,0,0)
white=(255, 255, 255)
green=(0, 255, 0)
red=(255, 0, 0)
sydneyBlue=(249, 169, 202)
sydneyGreen=(123, 232, 199)
sydneySunk=(203, 194, 254)
width=10
length=10
widthS=100
heightS=100
margin=10
pygame.init()
windowSize=[(widthS+margin)*width+margin, (heightS+margin)*length+margin]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Battleship")
keepGoing=0
totalGuesses=0
global gameGuesses
gameGuesses=1
global totalGuessesSquared
totalGuessesSquared=0
global minAll
minAll=10000
global maxAll
maxAll=0
games=list()
#evilImage=pygame.image.load('C:\Jordan\Images\evilComputer.png').convert_alpha()
#evilImage.set_alpha(None)
#evilImageRect=evilImage.get_rect()
while keepGoing<1:
        shipSizes = [5,4,3,3,2]
        global pfiveCount
        global pfourCount
        global pthreeFcount
        global pthreeScount
        global ptwoCount
        global cfiveCount
        global cfourCount
        global cthreeFcount
        global cthreeScount
        global ctwoCount
        global narrowed1
        global narrowed2
        global narrowed3
        global narrowed4
        global direc
        global currentCoord
        global narrowed
        global traverse
        global switchUD
        global switchOE
        global row
        global RLvg 
        priority=[]
        cPossible=[]
        shipsUnder=[]
        populate=0
        while populate<100:
                cPossible.append(populate)
                populate+=1
        lastHit=[]
        coord=[]
        pguessed=[]
        cguessed=[]
        global end

        def createBoard(width, length, coord):
                global pfiveCount
                global pfourCount
                global pthreeFcount
                global pthreeScount
                global ptwoCount
                global cfiveCount
                global cfourCount
                global cthreeFcount
                global cthreeScount
                global ctwoCount
                global end
                global narrowed1
                global narrowed2
                global narrowed3
                global narrowed4
                global direc
                global currentCoord
                global narrowed
                global traverse
                global switchUD
                global switchOE
                global row
                global RL
                RL=0
                switchOE=0
                switchUD=0
                row=5
                switch=0
                traverse=0
                narrowed=0
                currentCoord=0
                direc=0
                narrowed1=False
                narrowed2=False
                narrowed3=False
                narrowed4=False
                pfiveCount=0
                pfourCount=0
                pthreeFcount=0
                pthreeScount=0
                ptwoCount=0
                cfiveCount=0
                cfourCount=0
                cthreeFcount=0
                cthreeScount=0
                ctwoCount=0
                end=False
                for row in range(10):
                    for column in range(10):
                        color = white
                        pygame.draw.rect(screen,
                                         color,
                                         [(margin + widthS) * column + margin,
                                          (margin + heightS) * row + margin,
                                          widthS,
                                          heightS])
                pygame.display.flip()
                i=0
                while i<len(shipSizes):
                        shipCheck=True
                        x=random.randint(0,width-1)
                        y=random.randint(0,length-1)
                        d=random.randint(0,3)
                        if d==0:
                                if y-shipSizes[i]-1<0:
                                        shipCheck=False
                                else:
                                        temp=0
                                        while temp<shipSizes[i]:
                                                cCount=0
                                                while cCount<len(coord):
                                                        if (x==coord[cCount] and y-temp==coord[cCount+1]):
                                                                shipCheck=False
                                                                break
                                                        cCount+=3
                                                temp+=1
                                if shipCheck:
                                        temp=1
                                        while temp<shipSizes[i]:
                                                coord.append(x)
                                                coord.append(y-temp)
                                                coord.append(i)
                                                temp+=1
                        elif d==1:
                                if x+shipSizes[i]-1>width-1:
                                        shipCheck=False
                                else:
                                        temp=0
                                        while temp<shipSizes[i]:
                                                cCount=0
                                                while cCount<len(coord):
                                                        if x+temp==coord[cCount] and y==coord[cCount+1]:
                                                                shipCheck=False
                                                                break
                                                        cCount+=3
                                                temp+=1
                                if shipCheck:
                                        temp=1
                                        while temp<shipSizes[i]:
                                                coord.append(x+temp)
                                                coord.append(y)
                                                coord.append(i)
                                                temp+=1
                        elif d==2:
                                if y+shipSizes[i]-1>length-1:
                                        shipCheck=False
                                else:
                                        temp=0
                                        while temp<shipSizes[i]:
                                                cCount=0
                                                while cCount<len(coord):
                                                        if x==coord[cCount] and y+temp==coord[cCount+1]:
                                                                shipCheck=False
                                                                break
                                                        cCount+=3
                                                temp+=1
                                if shipCheck:
                                        temp=1
                                        while temp<shipSizes[i]:
                                                coord.append(x)
                                                coord.append(y+temp)
                                                coord.append(i)
                                                temp+=1
                        else:
                                if x-shipSizes[i]-1<0:
                                        shipCheck=False
                                else:
                                        temp=0
                                        while temp<shipSizes[i]:
                                                cCount=0
                                                while cCount<len(coord):
                                                        if x-temp==coord[cCount] and y==coord[cCount+1]:
                                                                shipCheck=False
                                                                break
                                                        cCount+=3
                                                temp+=1
                                if shipCheck:
                                        temp=1
                                        while temp<shipSizes[i]:
                                                coord.append(x-temp)
                                                coord.append(y)
                                                coord.append(i)
                                                temp+=1
                        if shipCheck:
                                coord.append(x)
                                coord.append(y)
                                coord.append(i)
                                i+=1
                #print("done building")

        def printBoard(width, length, testing, guessed):
                x=0
                i=0
                topline="  "
                while i<width:
                        topline=topline+str(i)+" "
                        i+=1
                print(topline)
                while x<width:
                        y=0
                        line=str(x)+" "
                        while y<length:
                                if testing:
                                        i=0
                                        marked=False
                                        known=False
                                        while i<len(guessed):
                                                if x==int(guessed[i]) and y==int(guessed[i+1]):
                                                        c=0
                                                        while c<len(coord):
                                                                if int(guessed[i])==coord[c] and int(guessed[i+1])==coord[c+1]:
                                                                        if coord[c+2]==0:
                                                                                line=line+"A "
                                                                        elif coord[c+2]==1:
                                                                                line=line+"B "
                                                                        elif coord[c+2]==2:
                                                                                line=line+"C "
                                                                        elif coord[c+2]==3:
                                                                                line=line+"D "
                                                                        else:
                                                                                line=line+"E "
                                                                        marked=True
                                                                c+=3
                                                        if not marked:
                                                                line=line+"M "
                                                        known=True
                                                i+=2
                                        if marked==False and known==False:
                                                line=line+"O "
                                else:
                                        line=line+"O "
                                y+=1
                        print(line)
                        x+=1

        def gameOver(fiCount, foCount, tFcount, tScount, twCount, winner):
                global end
                global totalGuessesSquared
                global gameGuesses
                global totalGuesses
                global minAll
                global maxAll
                if fiCount==5 and foCount==4 and tFcount==3 and tScount==3 and twCount==2:
                        if winner == "p":
                                print("You Win", str(gameGuesses))
                        else:
                                print("Computer Won")
                        printBoard(width,length,True, cguessed)
                                
                        #cguessed.clear()
                        #printBoard(width, length, True, cguessed)
                        totalGuessesSquared+=gameGuesses**2
                        totalGuesses+=gameGuesses
                        if gameGuesses<minAll:
                                minAll=gameGuesses
                        if gameGuesses>maxAll:
                                maxAll=gameGuesses
                        if len(games)>0:
                                i=0
                                added=False
                                while i<len(games):
                                        if gameGuesses<=games[i]:
                                                games.insert(i, gameGuesses)
                                                added=True
                                                break
                                        i+=1
                                if not added:
                                        games.append(gameGuesses)
                        else:
                                games.append(gameGuesses)
                        gameGuesses=0
                        end=True
                        pygame.quit()
        
        def newPlay():
            global end
            global pfiveCount
            global pfourCount
            global pthreeFcount
            global pthreeScount
            global ptwoCount
            moveOn=False
            alreadyGuessed=False
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    end = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (widthS + margin)
                    row = pos[1] // (heightS+margin)
                    # Set that location to one
                    i=0
                    while i<len(pguessed):
                        if column==pguessed[i] and row==pguessed[i+1]:
                            print("already guessed")
                            alreadyGuessed=True
                            break
                        i+=2
                    if not alreadyGuessed:
                        pguessed.append(column)
                        pguessed.append(row)
                        c=0
                        while c<len(coord):
                            if column==coord[c+1] and row==coord[c]:
                                if coord[c+2]==0:
                                        pfiveCount+=1
#                                        if pfiveCount==5:
#                                                print("Ship Sunk")
                                elif coord[c+2]==1:
                                        pfourCount+=1
#                                        if pfourCount==4:
#                                                print("Ship Sunk")
                                elif coord[c+2]==2:
                                        pthreeFcount+=1
#                                        if pthreeFcount==3:
#                                                print("Ship Sunk")
                                elif coord[c+2]==3:
                                        pthreeScount+=1
#                                        if pthreeScount==3:
#                                                print("Ship Sunk")
                                else:
                                        ptwoCount+=1
#                                        if ptwoCount==2:
#                                                print("Ship Sunk")
                                break
                            c+=3
                        moveOn=True
                    #print("Click ", pos, "Grid coordinates: ", row, column)
                    
         
            # Set the screen background
            if moveOn:
                screen.fill(black)
                
            
                y=0
                while y<width:
                    x=0
                    while x<length:
                        i=0
                        color=white
                        hit=False
                        sunk=False
                        while i<len(pguessed):
                            if x==pguessed[i] and y==pguessed[i+1]:
                                c=0
                                while c<len(coord):
                                    if pguessed[i+1]==coord[c] and pguessed[i]==coord[c+1]:
                                        if coord[c+2]==0:
                                                if pfiveCount==5:
                                                        color=sydneySunk
                                                        sunk=True
                                        elif coord[c+2]==1:
                                                if pfourCount==4:
                                                        color=sydneySunk
                                                        sunk=True
                                        elif coord[c+2]==2:
                                                if pthreeFcount==3:
                                                        color=sydneySunk
                                                        sunk=True
                                        elif coord[c+2]==3:
                                                if pthreeScount==3:
                                                        color=sydneySunk
                                                        sunk=True
                                        else:
                                                if ptwoCount==2:
                                                        color=sydneySunk
                                                        sunk=True
                                        if not sunk:
                                            color=sydneyGreen
                                        hit=True
                                    c+=3
                                if not hit:
                                    color=sydneyBlue
                            i+=2
                        pygame.draw.rect(screen, color, [(margin+widthS)*x+margin, (margin+heightS)*y+margin, widthS, heightS])
                        x+=1
                    y+=1
                pygame.display.flip()
                gameOver(pfiveCount, pfourCount, pthreeFcount, pthreeScount, ptwoCount, "p")
                return True

        def checkGuessed(x, y, guessed):
                if x>9 or x<0 or y>9 or y<0:
                        return False
                i=0
                while i<len(guessed):
                        if x==guessed[i] and y==guessed[i+1]:
                                return False
                        i+=2
                return True

        def checkPrio(x, y):
                weight=100
                ns=False
                nsA=[]
                ew=False
                ewA=[]
                if len(priority)>2:
                        i=0
                        while i<len(priority):
                                z=i+2
                                while z<len(priority):
                                        if priority[i]==priority[z] and (checkGuessed(priority[i], priority[i+1]-1, cguessed) or checkGuessed(priority[i], priority[i+1]+1, cguessed)or checkGuessed(priority[z], priority[z+1]-1, cguessed) or checkGuessed(priority[z], priority[z+1]+1, cguessed)):
                                        
                                                ew=True
                                                if i not in ewA:
                                                        ewA.append(i)
                                                if z not in ewA:
                                                        ewA.append(z)
                                        if priority[i+1]==priority[z+1] and (checkGuessed(priority[i]-1, priority[i+1], cguessed) or checkGuessed(priority[i]+1, priority[i+1], cguessed)or checkGuessed(priority[z]-1, priority[z+1], cguessed) or checkGuessed(priority[z]+1, priority[z+1], cguessed)):
                                                ns=True
                                                if i not in ewA and i not in nsA:
                                                        nsA.append(i)
                                                if z not in ewA and z not in nsA:
                                                        nsA.append(z)
                                        z+=2
                                i+=2
                        if ns:
                                #if direc=="n":
                                i=0
                                while i<len(nsA):
                                        if (x==priority[nsA[i]]-1 and y==priority[nsA[i]+1]) or (x==priority[nsA[i]]+1 and y==priority[nsA[i]+1]):
                                                #print(x, y)
                                                return weight
                                        i+=1
##                                elif direc=="s":
##                                        i=0
##                                        while i<len(nsA):
##                                                if x==priority[nsA[i]]+1 and y==priority[nsA[i]+1]:
##                                                        return weight
##                                                i+=1
                                return 1
                        elif ew:
                                #if direc=="e":
                                i=0
                                while i<len(ewA):
                                        if (x==priority[ewA[i]] and y==priority[ewA[i]+1]-1) or (x==priority[ewA[i]] and y==priority[ewA[i]+1]+1):
                                                #print(x,y)
                                                return weight
                                        i+=1
##                                elif direc=="w":
##                                        i=0
##                                        while i<len(ewA):
##                                                if x==priority[ewA[i]] and y==priority[ewA[i]+1]+1:
##                                                        return weight
##                                                i+=1
                                return 1
                if len(priority)>0:
##                        if direc=="n":
##                                i=0
##                                while i<len(priority):
##                                        if x==priority[i]-1 and y==priority[i+1]:
##                                                return weight
##                                        i+=2
##                        elif direc=="s":
##                                i=0
##                                while i<len(priority):
##                                        if x==priority[i]+1 and y==priority[i+1]:
##                                                return weight
##                                        i+=2
##                        elif direc=="w":
##                                i=0
##                                while i<len(priority):
##                                        if x==priority[i] and y==priority[i+1]+1:
##                                                return weight
##                                        i+=2
##                        else:
##                                i=0
##                                while i<len(priority):
##                                        if x==priority[i] and y==priority[i+1]-1:
##                                                return weight
##                                        i+=2
                        i=0
                        while i<len(priority):
                                if (x==priority[i]-1 and y==priority[i+1])or(x==priority[i]+1 and y==priority[i+1])or(x==priority[i] and y==priority[i+1]-1)or(x==priority[i] and y==priority[i+1]+1):
                                        return weight
                                i+=2
                        return 1
                return 1

        def checkDirections(shipSize, x, y):
                curDir=0
                count=0
                addedLast=True
                ns=[]
                ew=[]
                hasPrio=False
                cap=checkPrio(x, y)
                if cap>1:
                        hasPrio=True
                while curDir<4:
                        i=1
                        if hasPrio:
                                shipSize-=(len(priority)-1)/2
                                if shipSize<2:
                                        shipSize==2
                                while i<shipSize:
                                        #print(str(curDir))
                                        if curDir==0:
                                                if x-i>-1 and checkGuessed(x-i, y, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ns=[x-i]+ns
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        elif curDir==1:
                                                if y+i<10 and checkGuessed(x, y+i, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ew.append(y+1)
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        elif curDir==2:
                                                if x+i<10 and checkGuessed(x+i, y, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ns.append(x+i)
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        else:
                                                if y-i>-1 and checkGuessed(x, y-i, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ew=[y-i]+ew
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        i+=1
                        else:
                                while i<shipSize:
                                        #print(str(curDir))
                                        if curDir==0:
                                                if x-i>-1 and checkGuessed(x-i, y, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ns=[x-i]+ns
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        elif curDir==1:
                                                if y+i<10 and checkGuessed(x, y+i, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ew.append(y+1)
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        elif curDir==2:
                                                if x+i<10 and checkGuessed(x+i, y, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ns.append(x+i)
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        else:
                                                if y-i>-1 and checkGuessed(x, y-i, cguessed) and addedLast:
                                                        temp=0
                                                        while temp<cap:
                                                                ew=[y-i]+ew
                                                                temp+=1
                                                else:
                                                        addedLast=False
                                        i+=1
                        curDir+=1
                        addedLast=True
                countNS=len(ns)+2-shipSize
                countEW = len(ew)+2-shipSize
                if countNS<0:
                        countNS=0
                if countEW<0:
                        countEW=0
                count=countNS+countEW
                return count
                                

        def heatMap():
                shipsUnder=[]
                i=0
                while i<100:
                        count=0
                        sTemp=str(i)
                        if len(sTemp)>1:
                                x=int(sTemp[0])
                                y=int(sTemp[1])
                        else:
                                x=0
                                y=int(sTemp[0])
                        if checkGuessed(x, y, cguessed):
                                ship=0
                                while ship<len(shipSizes):
                                        count+=checkDirections(shipSizes[ship], x, y)
                                        ship+=1
                                shipsUnder.append(count)
                                shipsUnder.append(x)
                                shipsUnder.append(y)
                                
                        i+=1
                #print(shipsUnder)
                maxShips=-1
                i=0
                while i<len(shipsUnder):
                        if shipsUnder[i]>maxShips:
                                maxShips=shipsUnder[i]
                                x=shipsUnder[i+1]
                                y=shipsUnder[i+2]
                        i+=3
                #print(priority)
                temp=str(x)+str(y)
                #print(temp)
                return temp
                                        

        def ai(cPossible, d, aicoord, nar):
                global cfiveCount
                global cfourCount
                global cthreeFcount
                global cthreeScount
                global ctwoCount
                global direc
                global currentCoord
                global narrowed
                currentCoord=aicoord
                direc=d
                x=0
                y=0
                narrowed=nar
##                if len(lastHit)>0:
##                        temp=sinkBoat(lastHit, direc, narrowed, x, y)
##                        #print(temp)
##                        x=int(temp[0])
##                        y=int(temp[1])
##                        narrowed=int(temp[2])
##                if len(lastHit)==0:
                newCoord=heatMap()
                x=int(newCoord[0])
                y=int(newCoord[1])
                temp=0
                
                while temp<len(coord):
                        if x==coord[temp] and y==coord[temp+1]:
                                #print("hit")
                                priority.append(x)
                                priority.append(y)
                                if narrowed==0:
                                        #print("narrowed=0")
                                        lastHit.append(x)
                                        lastHit.append(y)
                                        if len(lastHit)>2:
                                                narrowed=1
                                elif narrowed==1:
                                        #print("narrowed=1")
                                        lastHit[2]=x
                                        lastHit[3]=y
                                else:
                                        #print("narrowed=2")
                                        lastHit[0]=x
                                        lastHit[1]=y
                                if coord[temp+2]==0:
                                        cfiveCount+=1
                                        if cfiveCount==5:
                                                print("Computer Sunk 5 Ship")
#                                                i=1
#                                                t=0
#                                                while i>-1:
#                                                    evilImage.set_alpha(i)
#                                                    screen.blit(evilImage, evilImageRect)
#                                                    if t==0:
#                                                        i+=1
#                                                    else:
#                                                        i-=1
#                                                    if i>=255 and t==0:
#                                                        t=1
#                                                    #print(evilImage.get_alpha())
#                                                    pygame.display.flip()
#                                                    pygame.time.delay(30)
                                                #printBoard(width,length,True, cguessed)
                                                shipSizes.remove(5)
                                                direc=0
                                                lastHit.clear()
                                                narrowed=0
                                                indexRemove=[]
                                                restart=[]
                                                alreadyChecked=[]
                                                i=0
                                                while i<len(priority):
                                                        if priority[i]==x and priority[i+1]==y:
                                                                indexRemove.append(i)
                                                                restart.append(i)
                                                        i+=2
                                                while len(indexRemove)<5:
                                                        i=0
                                                        while i<len(priority):
                                                                z=0
                                                                if len(indexRemove)==1 and direc==0:
                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="n"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="s"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="e"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="w"
                                                                                        indexRemove.append(i)
                                                                        z+=1
                                                                else:
                                                                        while z<len(indexRemove):
                                                                                if direc=="n":
                                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<5:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="s":
                                                                                        if priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<5:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="e":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<5:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="w":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<5:
                                                                                                                indexRemove.append(i)
##                                                                                else:
##                                                                                        indexRemove=restart
##                                                                                        if direc=="n":
##                                                                                                direc="s"
##                                                                                        elif direc=="s":
##                                                                                                direc="n"
##                                                                                        elif direc=="w":
##                                                                                                direc="e"
##                                                                                        elif direc=="e":
##                                                                                                direc="w"
                                                                                z+=1
##                                                                print(indexRemove, priority)
##                                                                printBoard(width,length,True, cguessed)
                                                                i+=2
                                                        if len(indexRemove)<5:
                                                                indexRemove=restart
                                                                if direc=="n":
                                                                        direc="w"
                                                                elif direc=="s":
                                                                        direc="e"
                                                                elif direc=="w":
                                                                        direc="s"
                                                                elif direc=="e":
                                                                        direc="n"
                                                indexRemove.sort(reverse=True)
                                                i=0
                                                while i<len(indexRemove):
                                                        priority.pop(indexRemove[i]+1)
                                                        priority.pop(indexRemove[i])
                                                        i+=1
                                elif coord[temp+2]==1:
                                        cfourCount+=1
                                        if cfourCount==4:
                                                print("Computer Sunk 4 Ship")
#                                                i=1
#                                                t=0
#                                                while i>0:
#                                                    evilImage.set_alpha(i)
#                                                    screen.blit(evilImage, evilImageRect)
#                                                    pygame.time.delay(30)
#                                                    if t==0:
#                                                        i+=1
#                                                    else:
#                                                        i-=1
#                                                    if i>=255 and t==0:
#                                                        t=1
#                                                    pygame.display.update()
                                                #screen.blit(evilImage, (0,0))
                                                #printBoard(width,length,True, cguessed)
                                                shipSizes.remove(4)
                                                direc=0
                                                lastHit.clear()
                                                narrowed=0
                                                indexRemove=[]
                                                restart=[]
                                                alreadyChecked=[]
                                                i=0
                                                while i<len(priority):
                                                        if priority[i]==x and priority[i+1]==y:
                                                                indexRemove.append(i)
                                                                restart.append(i)
                                                        i+=2
                                                while len(indexRemove)<4:
                                                        i=0
                                                        while i<len(priority):
                                                                z=0
                                                                if len(indexRemove)==1 and direc==0:
                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="n"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="s"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="e"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="w"
                                                                                        indexRemove.append(i)
                                                                        z+=1
                                                                else:
                                                                        while z<len(indexRemove):
                                                                                if direc=="n":
                                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<4:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="s":
                                                                                        if priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<4:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="e":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<4:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="w":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<4:
                                                                                                                indexRemove.append(i)
##                                                                                else:
##                                                                                        indexRemove=restart
##                                                                                        if direc=="n":
##                                                                                                direc="s"
##                                                                                        elif direc=="s":
##                                                                                                direc="n"
##                                                                                        elif direc=="w":
##                                                                                                direc="e"
##                                                                                        elif direc=="e":
##                                                                                                direc="w"
                                                                                z+=1
##                                                                print(indexRemove, priority)
##                                                                printBoard(width,length,True, cguessed)
                                                                i+=2
                                                        if len(indexRemove)<4:
                                                                indexRemove=restart
                                                                if direc=="n":
                                                                        direc="w"
                                                                elif direc=="s":
                                                                        direc="e"
                                                                elif direc=="w":
                                                                        direc="s"
                                                                elif direc=="e":
                                                                        direc="n"
                                                indexRemove.sort(reverse=True)
                                                i=0
                                                while i<len(indexRemove):
                                                        priority.pop(indexRemove[i]+1)
                                                        priority.pop(indexRemove[i])
                                                        i+=1
                                elif coord[temp+2]==2:
                                        cthreeFcount+=1
                                        if cthreeFcount==3:
                                                print("Computer Sunk 3 Ship")
#                                                i=1
#                                                t=0
#                                                while i>0:
#                                                    evilImage.set_alpha(i)
#                                                    screen.blit(evilImage, evilImageRect)
#                                                    pygame.time.delay(30)
#                                                    if t==0:
#                                                        i+=1
#                                                    else:
#                                                        i-=1
#                                                    if i>=255 and t==0:
#                                                        t=1
#                                                    pygame.display.update()
                                                #screen.blit(evilImage, (0,0))
                                                #printBoard(width,length,True, cguessed)
                                                shipSizes.remove(3)
                                                direc=0
                                                lastHit.clear()
                                                narrowed=0
                                                indexRemove=[]
                                                restart=[]
                                                alreadyChecked=[]
                                                i=0
                                                while i<len(priority):
                                                        if priority[i]==x and priority[i+1]==y:
                                                                indexRemove.append(i)
                                                                restart.append(i)
                                                        i+=2
                                                while len(indexRemove)<3:
                                                        i=0
                                                        while i<len(priority):
                                                                z=0
                                                                if len(indexRemove)==1 and direc==0:
                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="n"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="s"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="e"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="w"
                                                                                        indexRemove.append(i)
                                                                        z+=1
                                                                else:
                                                                        while z<len(indexRemove):
                                                                                if direc=="n":
                                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="s":
                                                                                        if priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="e":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="w":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
##                                                                                else:
##                                                                                        indexRemove=restart
##                                                                                        if direc=="n":
##                                                                                                direc="s"
##                                                                                        elif direc=="s":
##                                                                                                direc="n"
##                                                                                        elif direc=="w":
##                                                                                                direc="e"
##                                                                                        elif direc=="e":
##                                                                                                direc="w"
                                                                                z+=1
##                                                                print(indexRemove, priority)
##                                                                printBoard(width,length,True, cguessed)
                                                                i+=2
                                                        if len(indexRemove)<3:
                                                                indexRemove=restart
                                                                if direc=="n":
                                                                        direc="w"
                                                                elif direc=="s":
                                                                        direc="e"
                                                                elif direc=="w":
                                                                        direc="s"
                                                                elif direc=="e":
                                                                        direc="n"
                                                indexRemove.sort(reverse=True)
                                                i=0
                                                while i<len(indexRemove):
                                                        priority.pop(indexRemove[i]+1)
                                                        priority.pop(indexRemove[i])
                                                        i+=1
                                elif coord[temp+2]==3:
                                        cthreeScount+=1
                                        if cthreeScount==3:
                                                print("Computer Sunk 3 Ship")
#                                                i=1
#                                                t=0
#                                                while i>0:
#                                                    evilImage.set_alpha(i)
#                                                    screen.blit(evilImage, evilImageRect)
#                                                    pygame.time.delay(30)
#                                                    if t==0:
#                                                        i+=1
#                                                    else:
#                                                        i-=1
#                                                    if i>=255 and t==0:
#                                                        t=1
#                                                    pygame.display.update()
                                                #screen.blit(evilImage, (0,0))
                                                #printBoard(width,length,True, cguessed)
                                                shipSizes.remove(3)
                                                direc=0
                                                lastHit.clear()
                                                narrowed=0
                                                indexRemove=[]
                                                restart=[]
                                                alreadyChecked=[]
                                                i=0
                                                while i<len(priority):
                                                        if priority[i]==x and priority[i+1]==y:
                                                                indexRemove.append(i)
                                                                restart.append(i)
                                                        i+=2
                                                while len(indexRemove)<3:
                                                        i=0
                                                        while i<len(priority):
                                                                z=0
                                                                if len(indexRemove)==1 and direc==0:
                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="n"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="s"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="e"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="w"
                                                                                        indexRemove.append(i)
                                                                        z+=1
                                                                else:
                                                                        while z<len(indexRemove):
                                                                                if direc=="n":
                                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="s":
                                                                                        if priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="e":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="w":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<3:
                                                                                                                indexRemove.append(i)
##                                                                                else:
##                                                                                        indexRemove=restart
##                                                                                        if direc=="n":
##                                                                                                direc="s"
##                                                                                        elif direc=="s":
##                                                                                                direc="n"
##                                                                                        elif direc=="w":
##                                                                                                direc="e"
##                                                                                        elif direc=="e":
##                                                                                                direc="w"
                                                                                z+=1
##                                                                print(indexRemove, priority)
##                                                                printBoard(width,length,True, cguessed)
                                                                i+=2
                                                        if len(indexRemove)<3:
                                                                indexRemove=restart
                                                                if direc=="n":
                                                                        direc="w"
                                                                elif direc=="s":
                                                                        direc="e"
                                                                elif direc=="w":
                                                                        direc="s"
                                                                elif direc=="e":
                                                                        direc="n"
                                                indexRemove.sort(reverse=True)
                                                i=0
                                                while i<len(indexRemove):
                                                        priority.pop(indexRemove[i]+1)
                                                        priority.pop(indexRemove[i])
                                                        i+=1
                                else:
                                        ctwoCount+=1
                                        if ctwoCount==2:
                                                print("Computer Sunk 2 Ship")
#                                                i=1
#                                                t=0
#                                                while i>0:
#                                                    evilImage.set_alpha(i)
#                                                    screen.blit(evilImage, evilImageRect)
#                                                    pygame.time.delay(30)
#                                                    if t==0:
#                                                        i+=1
#                                                    else:
#                                                        i-=1
#                                                    if i>=255 and t==0:
#                                                        t=1
#                                                    pygame.display.update()
                                                #screen.blit(evilImage, (0,0))
                                                #printBoard(width,length,True, cguessed)
                                                shipSizes.remove(2)
                                                direc=0
                                                lastHit.clear()
                                                narrowed=0
                                                indexRemove=[]
                                                restart=[]
                                                alreadyChecked=[]
                                                i=0
                                                while i<len(priority):
                                                        if priority[i]==x and priority[i+1]==y:
                                                                indexRemove.append(i)
                                                                restart.append(i)
                                                        i+=2
                                                while len(indexRemove)<2:
                                                        i=0
                                                        while i<len(priority):
                                                                z=0
                                                                if len(indexRemove)==1 and direc==0:
                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="n"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="s"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="e"
                                                                                        indexRemove.append(i)
                                                                        elif priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                if i not in indexRemove:
                                                                                        direc="w"
                                                                                        indexRemove.append(i)
                                                                        z+=1
                                                                else:
                                                                        while z<len(indexRemove):
                                                                                if direc=="n":
                                                                                        if priority[i]+1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<2:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="s":
                                                                                        if priority[i]-1==priority[indexRemove[z]] and priority[i+1]==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<2:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="e":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]+1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<2:
                                                                                                                indexRemove.append(i)
                                                                                elif direc=="w":
                                                                                        if priority[i]==priority[indexRemove[z]] and priority[i+1]-1==priority[indexRemove[z]+1]:
                                                                                                if i not in indexRemove:
                                                                                                        if len(indexRemove)<2:
                                                                                                                indexRemove.append(i)
##                                                                                else:
##                                                                                        indexRemove=restart
##                                                                                        if direc=="n":
##                                                                                                direc="s"
##                                                                                        elif direc=="s":
##                                                                                                direc="n"
##                                                                                        elif direc=="w":
##                                                                                                direc="e"
##                                                                                        elif direc=="e":
##                                                                                                direc="w"
                                                                                z+=1
##                                                                print(indexRemove, priority)
##                                                                printBoard(width,length,True, cguessed)
                                                                i+=2
                                                        if len(indexRemove)<2:
                                                                indexRemove=restart
                                                                if direc=="n":
                                                                        direc="w"
                                                                elif direc=="s":
                                                                        direc="e"
                                                                elif direc=="w":
                                                                        direc="s"
                                                                elif direc=="e":
                                                                        direc="n"
                                                indexRemove.sort(reverse=True)
                                                i=0
                                                while i<len(indexRemove):
                                                        priority.pop(indexRemove[i]+1)
                                                        priority.pop(indexRemove[i])
                                                        i+=1
                                break
                        temp+=3
                
                cguessed.append(x)
                cguessed.append(y)
                #printBoard(width,length,True, cguessed)              
                gameOver(cfiveCount, cfourCount, cthreeFcount, cthreeScount, ctwoCount, "c")
                
                
                
                        
        createBoard(width, length, coord)
        #printBoard(width, length, True, pguessed)
        #print()
        while not end:
                #print("Guess: ",gameGuesses)
                if newPlay():
                        ai(cPossible, direc, currentCoord, narrowed);
                        gameGuesses+=1
##                try:
##                        ai(cPossible, direc, currentCoord, narrowed)
##                except KeyboardInterrupt:
##                        print(priority, shipsUnder)
##                        printBoard(width,length,True, cguessed)
##                gameGuesses+=1
        keepGoing+=1
        print(keepGoing)
#print("next Game")
mean=float(totalGuesses)/keepGoing
deviation=math.sqrt((float(totalGuessesSquared)/keepGoing)-((float(totalGuesses)/keepGoing)**2))
print(games)
if len(games)%2==1:
        median=games[int(len(games)/2)]
else:
        median=(games[int(len(games)/2)-1]+games[int(len(games)/2)])/2
print(str(mean), str(deviation),str(median), str(minAll), str(maxAll))
                        
        


