import random
import pygame
pygame.init()

W=1000
H=500
gameBoard = pygame.display.set_mode((W,H))
red= 255,0 ,0
white = 255,255,255
blue = 0,0,255
yellow = 255,255,0
back = pygame.image.load("back.png")
back = pygame.transform.scale(back,(W,H))


frogImage = pygame.image.load("frog.png")
frogImage  = pygame.transform.scale(frogImage,(40,40))


audio = pygame.mixer.Sound("collision_sound.wav")
audio.set_volume(1)

def Snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(gameBoard,red,[snakeList[i][0],snakeList[i][1],40,40])

def Score(counter):
    font = pygame.font.SysFont(None,30)
    #anti-aliasing
    text = font.render(f"Score : {counter}",True,yellow)
    gameBoard.blit(text,(10,10))

def GameOver():
    font = pygame.font.SysFont(None,100)
    text_1 = font.render("GAME OVER",True,yellow)
    text_2 = font.render("PRess SPACE to restart",True,yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game()
        gameBoard.blit(text_1,(W//2-150,H//2-150))
        gameBoard.blit(text_2,(100,350))
        pygame.display.flip()


def Game():
    x = 0
    y = 0
    moveX = 0
    moveY=0
    frogX = random.randint(0,W - 40)
    frogY = random.randint(0,H -40)
    snakeLength = 1
    snakeList = []
    counter=0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moveX = -2
                    moveY=0
                elif event.key==pygame.K_RIGHT:
                    moveX = 2
                    moveY=0

                elif event.key == pygame.K_UP:
                    moveY = -2
                    moveX=0
                elif event.key==pygame.K_DOWN:
                    moveY = 2
                    moveX=0
                    
        gameBoard.fill(white)
       

        gameBoard.blit(back,(0,0))
        
        snake = pygame.draw.rect(gameBoard,red,[x,y,30,30])

        frog = pygame.Rect(frogX,frogY,40,40)

        gameBoard.blit(frogImage,(frogX,frogY))

        x += moveX
        y += moveY


        
        if snake.colliderect(frog):
            frogX = random.randint(0,W - 40)
            frogY = random.randint(0,H -40)
        
            audio.play(0)
            snakeLength+=20
            counter+=1
        
        Score(counter)
        snakeList.append([x,y])
        Snake(snakeList)

        if snakeLength < len(snakeList):
            del snakeList[0]
        
        for i in snakeList[:-1]:
            if snakeList[-1] == i:
                GameOver()
            
            
            
        
        if x > W:
            x = -50
        elif x< -50:
            x= W

        elif y > H:
            y = -50
        elif y < -50:
            y =  H
            
        #pygame.draw.circle(gameBoard,red,[200,200],50)
            
        pygame.display.flip()

#function calling  
Game()
