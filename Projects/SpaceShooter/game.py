import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
back =  pygame.image.load("images/background.jpg")
back =  pygame.transform.scale(back,(width,height))

myShip = pygame.image.load("images/ship_1.png")
myShip=pygame.transform.scale(myShip,(100,100))
myShipWidth = myShip.get_width()
myShipHeight = myShip.get_height()

enemyShip = pygame.image.load("images/enemy_2.png")
enemyShipWidth = enemyShip.get_width()
enemyShipHeight = enemyShip.get_height()

sound_1 = pygame.mixer.Sound('sounds/sound_1.wav')
sound_2 = pygame.mixer.Sound('sounds/sound_2.wav')
sound_3 = pygame.mixer.Sound('sounds/sound_3.wav')

def main():
    myShipX = width // 2 - myShipWidth // 2
    myShipY = height - myShipHeight
    moveShipX = 0

    enemyShipList = []
    row = 2
    col = width // enemyShipWidth
    for i in range(row):
        for j in range(col):
            enemyShipX = enemyShipWidth * j
            enemyShipY = enemyShipHeight * i
            enemyShipList.append((enemyShipX,enemyShipY))

    enemyShipRectList = []
    for i in range(len(enemyShipList)):
        enemyShipRectList.append(pygame.Rect(enemyShipList[i][0],enemyShipList[i][1],enemyShipWidth,enemyShipHeight))

    shoot = False

    bulletWidth = 8
    bulletHeight = 14
    bulletY = myShipY
    moveBullet = 0
    while True:
        
        if not shoot:
            bulletX = myShipX + myShipWidth / 2 - bulletWidth/2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveShipX = 3
                elif event.key == pygame.K_LEFT:
                    moveShipX = -3
                elif event.key == pygame.K_SPACE:
                    moveBullet = -3
                    shoot = True
                    sound_1.play()
            elif event.type == pygame.KEYUP:
                moveShipX = 0

        screen.fill(white)
        screen.blit(back,(0,0))
        bulletRect = pygame.draw.rect(screen, red, [bulletX, bulletY, bulletWidth, bulletHeight])

        screen.blit(myShip,(myShipX,myShipY))
        for i in range(len(enemyShipList)):
            screen.blit(enemyShip,(enemyShipList[i][0],enemyShipList[i][1]))

        myShipX += moveShipX
        
        bulletY += moveBullet

        for i in range(len(enemyShipRectList)):
            if enemyShipRectList[i].colliderect(bulletRect):
                del enemyShipRectList[i]
                del enemyShipList[i]
                moveBullet = 0
                bulletY = myShipY
                bulletX = myShipX + myShipWidth / 2 - bulletWidth / 2
                shoot = False
                sound_2.play()
                break

        if bulletY < 0:
            moveBullet = 0
            bulletY = myShipY
            bulletX = myShipX + myShipWidth / 2 - bulletWidth / 2
            shoot = False

        pygame.display.flip()

try:
    main()
except BaseException as ex:
    print(ex)
