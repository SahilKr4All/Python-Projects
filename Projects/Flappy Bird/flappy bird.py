import pygame
import random
pygame.init()

bg1 = pygame.image.load("bg.png")
bg2 = pygame.image.load("bg.png")
H = bg1.get_height()
W = bg1.get_width()

gameBoard = pygame.display.set_mode((W,H)) 
audio = pygame.mixer.Sound("collision_sound.wav")

pillar = pygame.image.load("pipe-red.png")
pillarW = pillar.get_width()
pillarH = pillar.get_height()-170
pillar = pygame.transform.scale(pillar,(pillarW,pillarH))
bird = pygame.image.load("bird.png")
bg3 = pygame.image.load('bg3.jpg')
bg3 = pygame.transform.scale(bg3,(W,H))




blue = 0,0,255
red = 255,0,0
fly = False


def Lives(encounter):
    
    font = pygame.font.SysFont(None,30)
    text = font.render(f"LIVES : {encounter}",True,blue)
    gameBoard.blit(text,(10,10))

def GameOver():
    font = pygame.font.SysFont(None,20)
    text_1 = font.render("GAME OVER",True,blue)
    text_2 = font.render("PRess SPACE to restart",True,red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # mainflapbird()
                    restartgame()
        gameBoard.blit(text_1,(W//2-100,H//2-150))
        gameBoard.blit(text_2,(W//2-300,350))
        pygame.display.flip()

def restartgame():
    font = pygame.font.SysFont(None,100)
    text_5 = font.render("RESTART GAME",True,blue)
    text_6 = font.render("PRESS ENTER TO RESTART GAME",True,red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        gameBoard.blit(bg3,(0,0))
            
        gameBoard.blit(text_5,(W//2-100,H//2-150))
        gameBoard.blit(text_6,(100,350))
        
        pygame.display.flip()


def startgame():
    font = pygame.font.SysFont(None,30)
    text_5 = font.render("START GAME",True,blue)
    text_6 = font.render("PRESS ENTER TO START GAME",True,red)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        gameBoard.blit(bg3,(0,0))
            
        gameBoard.blit(text_5,(W//2-100,H//2-150))
        gameBoard.blit(text_6,(100,350))
        
        pygame.display.flip()


def Score(counter):
    font = pygame.font.SysFont(None,30)
    #anti-aliasing
    text = font.render(f"Score : {counter}",True,blue)
    gameBoard.blit(text,(W-200,10))

def main():

    birdY = H//2-65

    bg_x1=0
    bg_y1=0
    bg_x2=W
    bg_y2 = 0
    updown = [0,H/2-35]
    py = random.choice(updown)
    px = W
    encounter = 3
    counter = 0
    FPS = 80 #fps value must be always greator than 60
    clock = pygame.time.Clock()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    birdY -= 10



                
        birdY +=0.5
        gameBoard.blit(bg1,(bg_x1,bg_y1))
        gameBoard.blit(bg2,(bg_x2,bg_y2))
        bg_x1-=2
        bg_x2-=2

    

        gameBoard.blit(bird,(200,birdY))
        birdRect = pygame.Rect(200,birdY,bird.get_width(),bird.get_height())
        
        gameBoard.blit(pillar,(px,py))
        pillarRect = pygame.Rect(px,py,pillarW,pillarH)
        px-=1

        Lives(encounter)

       
        if birdRect.colliderect(pillarRect) or birdY > 600:

            encounter -= 1
            birdY= -100

            audio.play()


            
            if encounter == 0:
                Lives(0)
                GameOver()
            
            
        

       

        if px == 150:
            counter+=1
        Score(counter)


        if px<-100:
            px = W
            py = random.choice(updown)



        if bg_x1 < -W:
            bg_x1 = W
        

        if bg_x2 < -W:
            bg_x2 = W

        clock.tick(FPS)
        pygame.display.flip()

startgame()
