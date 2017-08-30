#By: Elena Kostandin
import pygame,random, os
from pygame.locals import *
pygame.init()
##
##BOARDWIDTH=8
##BOARDHEIGHT=8
##
##
WINDOWWIDTH=600
WINDOWHEIGHT=600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
FRAMERATE=40
WHITE=(255,255,255)
GREY=(105,105,105)
BLUE=(0,0,255)
RED=(255,0,0)
##NAVY=(0,0,128)
GREEN=(34,139,34)

pygame.display.set_caption('Minesweeper')
##
BOMB=pygame.image.load('bomb.png')
BOMBS=12
##bombrect.top=windowSurface.get_rect().top
##bombrect.left=windowSurface.get_rect().left
EMPTY=pygame.image.load("empty.jpg")
SQUARE="square.png"
ALLSQUARES=144
ONE=pygame.image.load("1.jpg")
TWO=pygame.image.load("2.jpg")
THREE=pygame.image.load("3.jpg")
FOUR=pygame.image.load("4.jpg")
FIVE=pygame.image.load("5.jpg")
SIX=pygame.image.load("6.jpg")
SEVEN=pygame.image.load("7.jpg")
EIGHT=pygame.image.load("8.jpg")
FLAG=pygame.image.load("flag.png")


NUM=12
def terminate():
    """ This function is called when the user closes the window or presses ESC """
    pygame.quit()
    os._exit(1)

def maketable (num,bombs):
    table=[]
    temp=[]
    for x in range (0,num):
        new=[]
        temprow=[]
        for i in range (0,num):
            new.append(0)
            temprow.append(0)
        table.append(new)
        temp.append(temprow)
    for i in range (bombs):
        isbomb=False
        while isbomb==False:
            x=random.randrange(0,len(table))
            y=random.randrange(0,len(table))
            if table[x][y] !=9:
                table[x][y]=9
                temp[x][y]=9
                isbomb=True
    return table,temp

def fill(table): 
    for x in range (NUM):
        for y in range (NUM):
            count=0
            if table [x][y]!=9:
                if x<NUM-1:
                    if table[x+1][y]==9:
                        count=count+1
                if x>0:
                    if table[x-1][y]==9:
                        count=count+1
                if y<NUM-1:
                    if table[x][y+1]==9:
                        count=count+1
                if y>0:
                    if table[x][y-1]==9:
                        count=count+1
                if x<NUM-1 and y<NUM-1:
                    if table[x+1][y+1]==9:
                        count=count+1
                if x>0 and y>0:
                    if table[x-1][y-1]==9:
                        count=count+1
                if x>0 and y<NUM-1:
                    if table[x-1][y+1]==9:
                        count=count+1
                if x<NUM-1 and y>0:
                    if table[x+1][y-1]==9:
                        count=count+1
                table[x][y]=count
    return table 

"""pygame code"""

                    
def load_image(filename):
    """ Load an image from a file.  Return the image and corresponding rectangle """
    image = pygame.image.load(filename)
    #image = image.convert()        #For faster screen updating
    image = image.convert_alpha()   #Not as fast as .convert(), but works with transparent backgrounds
    return image, image.get_rect()

def opensq(chart,x,y):
        
        if x>NUM-1 or y>NUM-1 or x<0 or y<0:
            
            return 0
        if chart[x][y]!=0 :
            if chart[x][y]!='o':
                if chart[x][y]==1:
                    windowSurface.blit(ONE,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==2:
                    windowSurface.blit(TWO,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==3:
                    windowSurface.blit(THREE,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==4:
                    windowSurface.blit(FOUR,(x*50,y*50))
                    chart[x][self.y]='o'
                    return 1
                elif chart[x][y]==5:
                    windowSurface.blit(FIVE,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==6:
                    windowSurface.blit(SIX,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==7:
                    windowSurface.blit(SEVEN,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
                elif chart[x][y]==8:
                    windowSurface.blit(EIGHT,(x*50,y*50))
                    chart[x][y]='o'
                    return 1
        
            return 0
            
        
        if chart[x][y]==0:
            windowSurface.blit(EMPTY,(x*50,y*50))
            
            chart[x][y]='d'
            
    
            count=1+opensq(chart,x,y-1)+ opensq(chart,x-1,y-1)+opensq(chart,x-1,y)+opensq(chart,x+1,y)+ opensq(chart,x,y+1)+ opensq(chart,x+1,y+1)+ opensq(chart,x-1,y+1)+opensq(chart,x+1,y-1)
            return count
        
 
class layer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image,self.rect=load_image(SQUARE)
        
        
def drawText(text, font, surface, x, y, textcolour):
    """ Draws the text on the surface at the location specified """
    textobj = font.render(text, 1, textcolour)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)    


class Game():
    def __init__(self):
        self.gameover=False
        table,temp= maketable(NUM,BOMBS)
        
        self.final=fill(table)
        self.temp=fill(temp)
        self.x=-1
        self.y=-1
        self.m=-1
        self.n=-1
        self.count=0
        self.visib= True
        for m in range (NUM):
            for n in range (NUM):
                print self.final[m][n],
            print

        self.win=False
        self.alllayer = pygame.sprite.Group()
        
        x=0
        for i in range (NUM):
            y=0
            for m in range (NUM):
                asquare = layer()
                asquare.rect.left=x
                asquare.rect.top=y
                self.alllayer.add(asquare)
               
                y=y+50
            x=x+50
       
            
    def process_events(self, windowSurface):
        """ Process all of the keyboard and mouse events.  """
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type==MOUSEBUTTONDOWN and event.button==1 and self.gameover==False:
                self.x=event.pos[0]/50
                self.y=event.pos[1]/50
 
                return True
            if event.type==MOUSEBUTTONDOWN and event.button==3 and self.gameover==False:
                self.m=event.pos[0]/50
                self.n=event.pos[1]/50
             
                return True
            if self.gameover==True and event.type==MOUSEBUTTONDOWN:
                windowSurface.fill(GREY)
                self.__init__()
                self.alllayer.draw(windowSurface)
                pygame.display.update()
        return False
                

    def runlogic(self,windowSurface):
        
        
        if self.count==(ALLSQUARES-BOMBS-1):
            self.win=True
            
            return True
        
                

    def display(self, windowSurface):
        
        if self.win:
            x = WINDOWWIDTH / 2 - 120
            y = WINDOWHEIGHT / 2 - 20
            basicFont = pygame.font.SysFont("Comic Sans MS", 20)
            windowSurface.fill(WHITE)
            drawText("YOU WIN!, click to restart", basicFont, windowSurface, x ,y, BLUE)
            self.gameover=True
        else:
           
            if self.m==-1 and self.n==-1:
                if self.final[self.x][self.y]!=9 and self.final[self.x][self.y]!=0:
                   
                    if self.final[self.x][self.y]==1:
                        windowSurface.blit(ONE,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==2:
                        windowSurface.blit(TWO,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==3:
                        windowSurface.blit(THREE,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==4:
                        windowSurface.blit(FOUR,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==5:
                        windowSurface.blit(FIVE,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==6:
                        windowSurface.blit(SIX,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==7:
                        windowSurface.blit(SEVEN,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1
                    elif self.final[self.x][self.y]==8:
                        windowSurface.blit(EIGHT,(self.x*50,self.y*50))
                        self.final[self.x][self.y]='d'
                        self.count=self.count+1

                elif self.final[self.x][self.y]==0:
                    
                    #self.count=self.count+
                    
                    self.count=self.count+opensq(self.final,self.x,self.y)
                    
                    #if self.final[self.x][self.y]!='d':

                        #self.count=self.count+1
                        #self.final[self.x][self.y]='d'
                                                   
                            
                elif self.final[self.x][self.y]==9:
                   
                    for n in range (NUM):
                        for m in range (NUM):
                            if self.final[n][m]==9:
                                windowSurface.blit(BOMB,(n*50,m*50))
                                
                               
                                x = WINDOWWIDTH / 2 - 120
                                y = WINDOWHEIGHT / 2 - 20
                                basicFont = pygame.font.SysFont("Comic Sans MS", 20)
                                
                                drawText("Game Over, click to restart", basicFont, windowSurface, x ,y, BLUE)
                                self.gameover=True
                             
                                

                               
            else:
               
                if self.final[self.m][self.n]!='*' :
                    windowSurface.blit(FLAG,(self.m*50,self.n*50))
                    self.final[self.m][self.n]='*'
                else:
                    self.final[self.m][self.n]=self.temp[self.m][self.n]
                    windowSurface.blit(pygame.image.load(SQUARE),(self.m*50,self.n*50))
                    
               
                self.m=-1
                self.n=-1


        pygame.display.update()

def main():
        
    
    windowSurface.fill(GREY)
    
    mainClock = pygame.time.Clock()
    #display_menu(windowSurface)
    game=Game()
    game.alllayer.draw(windowSurface)
    pygame.display.update()
    while True:
       
        if game.process_events(windowSurface)==True:
            game.runlogic(windowSurface)
            game.display(windowSurface)
     
    mainClock.tick(FRAMERATE)          


main()
