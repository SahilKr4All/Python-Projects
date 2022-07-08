import random
import pygame
pygame.init()
width=1000
height=800
gameBoard = pygame.display.set_mode((width,height))
red= 255,0 ,0
white = 255,255,255
x = 0
y = 0
rectWidth = 50
rectHeight = 50
moveX = 0
moveY=0
mouseX = 0
mouseY = 0
while True:
    gameBoard.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            mouseX = event.pos[0]
            mouseY = event.pos[1]
        
            
    #surface , color , [x,y,width,height]
    pygame.draw.rect(gameBoard,red,[x,y,rectWidth,rectHeight])

    x = mouseX
    y = mouseY
    
        
    #pygame.draw.circle(gameBoard,red,[200,200],50)
        
    pygame.display.flip()
    
