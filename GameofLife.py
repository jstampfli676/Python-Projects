import pygame, random, time


black=(0,0,0)
white=(255, 255, 255)
width=100
length=100
widthS=10
heightS=10
margin=1
pygame.init()
windowSize=[(widthS+margin)*width+margin, (heightS+margin)*length+margin]
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Game of Life")

cells=[]
##for i in range(width):
##    for x in range(length):
##        cells.append(random.randint(0, 1)) fill cells randomly
for i in range(width):
    for x in range(length):
        cells.append(0)
cellsTemp=cells.copy()

def drawBoard(cells):
    for row in range(width):
        for column in range(length):
            if cells[row*width+column]==0:
                color=black
            else:
                color=white
            pygame.draw.rect(screen,
                             color,
                             [(margin + widthS) * column + margin,
                              (margin + heightS) * row + margin,
                              widthS,
                              heightS])
    pygame.display.flip()
    
def pause(cells):
    drawBoard(cells)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                return cells 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (widthS + margin)
                row = pos[1] // (heightS+margin)
                singleCell=column+row*width
                if cells[singleCell]==0:
                    cellsTemp[singleCell]=1
                else:
                    cellsTemp[singleCell]=0
                cells=cellsTemp.copy()
                drawBoard(cells)
    
def neighborCount(pos):
    count=0
    x=[-1*width, 0, 1*width]
    y=[-1, 0, 1]
    for i in x:
        for z in y:
            if i+z!=0 and pos+i+z>-1 and pos+i+z<len(cells):
                if cells[pos+i+z]==1:
                    count+=1
    return count
    
def iterate(cells):
    for row in range(width):
        for column in range(length):
            pos=row*width+column
            liveCount=neighborCount(pos)
            if cells[pos]==0:
                if liveCount==3:
                    cellsTemp[pos]=1
            else:
                if liveCount<2 or liveCount>3:
                    cellsTemp[pos]=0
    cells=cellsTemp.copy()
    return cells

cells=pause(cells)

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_p:
                cells=pause(cells)
    drawBoard(cells)
    time.sleep(.25)
    cells=iterate(cells)
    



