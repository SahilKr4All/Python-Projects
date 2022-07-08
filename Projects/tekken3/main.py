import pygame
from pygame.locals import *
from os import path
import time
Width =1000
Height=500
FPS=60
clock = pygame.time.Clock()
white = 255,255,255
red = 255,0,0
blue = 0,0,255
black = 0,0,0
green = 0,255,0
yellow=255,255,0

img_dir = path.join(path.dirname(__file__),'img')
snd_dir = path.join(path.dirname(__file__),'snd')

class SpriteSheet():
    def __init__(self,file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name
        
    def getImage(self,x,y,width,height):
        image = pygame.Surface((width,height))
        image.blit(self.spriteSheet,(0,0),(x,y,width,height))
        image.set_colorkey(black)
        
        return image
    
class Player_1(pygame.sprite.Sprite):
    
    standingFrames=[]
    walkingFrames=[]
    sidekickFrames=[]
    upperkickFrames=[]
    leftpunchFrames=[]
    player_sprite = None
    isAttack = False
    health=450
    strength=0
    # straightkickFrames=[]
    # onkneeslidekickFrames=[]
    # rightpunchFrames=[]
    # onkneerightpunchFrames= []

    def __init__(self,player_sprite):
        super().__init__()
        self.player_sprite = player_sprite
        sprite = SpriteSheet(player_sprite)
        self.image=sprite.getImage(41,2,59,92)               
        self.standingFrames.append(self.image)                            #standingFrames=[]
        
        self.image=sprite.getImage(432,2,59,92)
        self.standingFrames.append(self.image)


        self.image=sprite.getImage(41,2,59,92)               
        self.walkingFrames.append(self.image)                            #standingFrames=[]
        
        self.image=sprite.getImage(432,2,59,92)
        self.walkingFrames.append(self.image)


        self.image=sprite.getImage(432,2,59,92)
        self.sidekickFrames.append(self.image)                            #sidekickFrames=[]

        self.image=sprite.getImage(157,2,59,92)
        self.sidekickFrames.append(self.image)

        self.image=sprite.getImage(221,2,59,92)
        self.sidekickFrames.append(self.image)

        self.image=sprite.getImage(41,2,59,96)
        self.upperkickFrames.append(self.image)                           #upperkickFrames=[]

        self.image=sprite.getImage(2,96,59,96)
        self.upperkickFrames.append(self.image)

        self.image=sprite.getImage(56,96,59,96)
        self.upperkickFrames.append(self.image)
        
        
        
        
        self.image=sprite.getImage(41,2,59,92)
        self.leftpunchFrames.append(self.image)                         #leftpunchFrames=[]

        self.image=sprite.getImage(432,2,59,92)
        self.leftpunchFrames.append(self.image)

        self.image=sprite.getImage(487,2,59,92)
        self.leftpunchFrames.append(self.image)



        self.rect = self.image.get_rect()
        self.rect.center=(Width/2-250,Height/2-100)
        self.rect.width = self.rect.width*4
        self.rect.height = self.rect.height*4

        self.punchActive=0
        self.sideKickActive=0
        self.upperKickActive=0
        self.moving=0
    
    def update(self):
        self.speedX=0
        self.speedY=0
        self.hit = pygame.sprite.groupcollide(ken,ryo,False,False)
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_d]:
            self.speedX=8
            self.moving=True
            if self.rect.x > Width or self.hit:
                self.speedX =0
                self.moving=False
        elif keypressed[pygame.K_a]:
            self.speedX=-8
            self.moving=True
            if self.rect.x < 0:
                self.speedX =0
                self.moving=False
        elif keypressed[pygame.K_s]:
            self.punch=True
            
        elif keypressed[pygame.K_w]:
            self.upperKick =True
        
        elif keypressed[pygame.K_f]:
            self.sideKick=True
        else:
            self.punch=False
            self.sideKick=False
            self.upperKick=False
    
        self.rect.y+= self.speedY
        
        if self.moving==True:
            self.rect.x+=self.speedX
            
        pos = self.rect.x
        
        pun=self.punchActive
        sidekickFrame = self.sideKickActive
        upperKickFrame = self.upperKickActive
        
        frame= (pos//30)%(len(self.walkingFrames))
        self.image=self.walkingFrames[frame]
        
        if self.punch ==True:
            frame = (pun//30)%(len(self.leftpunchFrames))
            self.image=self.leftpunchFrames[frame]
            
            if self.hit:
                player_2.strength -=1
                player_2.isAttack = True
                punchSound.play()
                
                
        elif self.sideKick ==True:
            frame = (sidekickFrame//30)%(len(self.sidekickFrames))
            self.image=self.sidekickFrames[frame]
            
            if self.hit:
                player_2.strength -=4
                player_2.isAttack = True        
                punchSound.play()
                
        elif self.upperKick ==True:
            frame = (upperKickFrame//30)%(len(self.upperkickFrames))
            self.image=self.upperkickFrames[frame]
            
            if self.hit:
                player_2.strength -=8
                player_2.isAttack = True
                punchSound.play()
                
        else:
            player_2.isAttack=False
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*4,self.image.get_height()*4))
        
        
class Player_2(pygame.sprite.Sprite):
    
    standingFrames=[]
    walkingFrames=[]
    sidekickFrames=[]
    upperkickFrames=[]
    leftpunchFrames=[]
    
    hitFrames=[]
    cpu_moves=[]
    isAttack = False
    health=450
    strength=0
    punch = None
    player_sprite_2 = None
    
    # straightkickFrames=[]
    # onkneeslidekickFrames=[]
    # rightpunchFrames=[]
    # onkneerightpunchFrames= []

    def __init__(self,player_sprite_2):
        super().__init__()
        self.player_sprite_2 = player_sprite_2
        sprite = SpriteSheet(player_sprite_2)
        self.image=sprite.getImage(662,2,59,92)               
        self.standingFrames.append(self.image)                            #standingFrames=[]
        
        self.image=sprite.getImage(270,2,59,92)
        self.standingFrames.append(self.image)

        self.image=sprite.getImage(662,2,59,92)               
        self.walkingFrames.append(self.image)                            #standingFrames=[]
        
        self.image=sprite.getImage(270,2,59,92)
        self.walkingFrames.append(self.image)


        self.image=sprite.getImage(662,2,59,92)
        self.sidekickFrames.append(self.image)                            #sidekickFrames=[]

        self.image=sprite.getImage(546,2,59,92)
        self.sidekickFrames.append(self.image)

        self.image=sprite.getImage(458,2,59,92)
        self.sidekickFrames.append(self.image)

        self.image=sprite.getImage(662,2,59,96)
        self.upperkickFrames.append(self.image)                           #upperkickFrames=[]

        self.image=sprite.getImage(709,96,59,96)
        self.upperkickFrames.append(self.image)

        self.image=sprite.getImage(632,96,59,96)
        self.upperkickFrames.append(self.image)


        self.image=sprite.getImage(194,190,56,81)
        self.hitFrames.append(self.image)

        self.image=sprite.getImage(243,200,55,71)
        self.hitFrames.append(self.image)

        self.image=sprite.getImage(664,5,60,92)
        self.hitFrames.append(self.image)
        
        
                
        self.image=sprite.getImage(41,2,59,92)
        self.leftpunchFrames.append(self.image)                         #leftpunchFrames=[]

        self.image=sprite.getImage(432,2,59,92)
        self.leftpunchFrames.append(self.image)

        self.image=sprite.getImage(487,2,59,92)
        self.leftpunchFrames.append(self.image)


        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width*4
        self.rect.height = self.rect.height
        self.rect.center=(Width/2+50,Height/2-100)
        self.punchActive=0
        self.sideKickActive=0
        self.upperKickActive=0
        self.moving=0
        
    
    
    def update(self):
        self.speedX=0
        self.speedY=0
        self.hit = pygame.sprite.groupcollide(ken,ryo,False,False)
        
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_j]:
            self.speedX=-4
            self.moving =True
            if self.rect.x < 0 or self.hit:
                self.speedX =0
                self.moving =False
                
        elif keypressed[pygame.K_l]:
            self.speedX=4
            self.moving =True
            
            if self.rect.x > Width or self.hit:
                self.speedX =0
                self.moving = False
        
        elif keypressed[pygame.K_k]:
            self.punch=True
        elif keypressed[pygame.K_i]:
            self.upperKick =True
        
        elif keypressed[pygame.K_h]:
            self.sideKick=True
        else:
            self.punch=False
            self.sideKick=False
            self.upperKick=False
    
        self.rect.y+= self.speedY

        if self.moving==True:
            self.rect.x+=self.speedX
            
        pos = self.rect.x
        pun=self.punchActive
        sidekickFrame = self.sideKickActive
        upperKickFrame = self.upperKickActive
        
        frame= (pos//30)%(len(self.walkingFrames))
        self.image=self.walkingFrames[frame]
        
        self.hit = pygame.sprite.groupcollide(ken,ryo,False,False)
        
        if self.punch == True:
            frame = (pun//30)%(len(self.leftpunchFrames))
            self.image=self.leftpunchFrames[frame]
            self.isAttack=False    
            if self.hit:
                player.strength -=1
                player.isAttack = True
                punchSound.play()
                        
                
        if self.sideKick ==True:
            frame = (sidekickFrame//30)%(len(self.sidekickFrames))
            self.image=self.sidekickFrames[frame]
            self.isAttack=False
            
            if self.hit:
                player.strength -=4
                player.isAttack = True
                punchSound.play()

                
        if self.upperKick ==True:
            frame = (upperKickFrame//30)%(len(self.upperkickFrames))
            self.image=self.upperkickFrames[frame]
            self.isAttack=False
            if self.hit:
                player.strength -=8
                player.isAttack = True
                punchSound.play()

        if self.isAttack==True:
            frame = (sidekickFrame//30)%len(self.hitFrames)
            self.image = self.hitFrames[frame]
            player.isAttack=False

        else:
            player.isAttack=False
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*4,self.image.get_height()*4))
        

def GameOverScreen(p1_win,p2_win):
    font = pygame.font.SysFont(False,100)
    text2 = font.render("Game OVer",True,white)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        if p1_win>p2_win:
            text1 = font.render("You Win",True,white)
        else:
            text1 = font.render("Opponent Win",True,white)
                        
        screen.blit(text1,(Width/2-100,Height/2-100))
        screen.blit(text2,(Width/2-150,Height/2-150))
        
        pygame.display.update()





def healthBarPlayer_1(playerName,health,p1_win,p2_win):
    
    font = pygame.font.SysFont(False,30)
    text1 = font.render(playerName,True,white)
    screen.blit(text1,(10,50))

    if health > 300:
        col=green
    elif health >150:
        col=yellow
    else:
        col = red

    
        
    pygame.draw.rect(screen,col,(0,10,health,40))
    


def healthBarPlayer_2(playerName,health,p1_win,p2_win):
    font = pygame.font.SysFont(False,30)
    text1 = font.render(playerName,True,white)
    screen.blit(text1,(Width-50,50))
    
    if health > 300:
        col=green
    elif health >150:
        col=yellow
    else:
        col = red
    
    
        
        
    

    pygame.draw.rect(screen,col,(550,10,health,40))
    
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Street fighter")
 
background = pygame.image.load(path.join(img_dir,'bg1.jpg')).convert()


bg = pygame.image.load('img/bg.jpg')
bg = pygame.transform.scale(bg,(Width,Height))
splash_bg = pygame.image.load('img/splash.jpg')
splash_bg = pygame.transform.scale(splash_bg,(Width,Height))
ryukenImg = pygame.image.load('img/kenryu.png')
ryukenImg = pygame.transform.scale(ryukenImg,(Width,Height))


punchSound = pygame.mixer.Sound('punch.wav')
themeSound = pygame.mixer.Sound('theme.mp3')
splashSound = pygame.mixer.Sound('splash.mp3')
pygame.time.set_timer(USEREVENT,1000)

        
def HomeScreen():
    screen.fill(white)
    themeSound.play(-1)
    font = pygame.font.SysFont(False,50)
    text1 = font.render("***Press Space to Start***",True,black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    themeSound.stop()
                    return
                    
        screen.blit(bg,(0,0))
        screen.blit(text1,(Width/2-200,Height-30))
        pygame.display.update()
        
def splashScreen(name1,name2):
    splashSound.play(-1)
    font = pygame.font.SysFont(False,50)
    text1 = font.render("***Press Space to Start***",True,yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    splashSound.stop()
                    main(name1,name2)
                    
        screen.blit(splash_bg,(0,0))
        screen.blit(text1,(Width/2-200,Height-30))
        pygame.display.update()


def main(name1,name2):
    #game Loop
    running =True
    
    p1_win=0
    p2_win=0
    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            

        player.punchActive +=7
        player.sideKickActive+=7
        player.upperKickActive+=7
        
        player_2.punchActive += 10
        player_2.sideKickActive +=5
        player_2.upperKickActive +=7        

        all_sprite.update()
        screen.fill(black)
        screen.blit(background,(0,0))
        all_sprite.draw(screen)
        health = 450+player.strength
        health1 = 450+player_2.strength
        
        
    

    


        if health==10:
            p2_win+=1
        if health1==10:
            p1_win+=1
        
        if(health<10) or ((health1<10)):
            
            GameOverScreen(health,health1)

        print(health,health1)
        
            
        

        healthBarPlayer_1(name1,health,p1_win,p2_win)
        healthBarPlayer_2(name2,health1,p1_win,p2_win)
        
        pygame.display.update()


def choosePlayer():
    screen.fill(white)
    font = pygame.font.SysFont(False,30)
    text1 = font.render("Press R to Choose Ryu",True,black)
    text2 = font.render("Press K to Choose Ken ",True,black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    im1 = 'fighter_1.gif'
                    im2 =  'fighter_2.png'
                    name1 = 'RYU'
                    name2 = 'KEN'
                    return im1,im2,name1,name2
                elif event.key == pygame.K_k:
                    im1 = 'fighter_2.png'
                    im2 = 'fighter_1.gif'
                    name2 = 'RYU'
                    name1 = 'KEN'
                    return im1,im2,name1,name2
        screen.blit(ryukenImg,(0,0))              
        screen.blit(text1,(Width/2+50,Height-30))
        screen.blit(text2,(150,Height-30))
        
        pygame.display.update()
        
HomeScreen()
im1,im2,name1,name2 = choosePlayer()
player_sprite = pygame.image.load(path.join(img_dir,im1)).convert_alpha()
player_sprite_2 = pygame.image.load(path.join(img_dir,im2)).convert_alpha()
player_sprite_2=pygame.transform.flip(player_sprite_2,True,False)
player = Player_1(player_sprite)
player_2 = Player_2(player_sprite_2)
all_sprite = pygame.sprite.Group()
ken = pygame.sprite.Group()
ken.add(player)
ryo = pygame.sprite.Group()
ryo.add(player_2)
all_sprite.add(player)
all_sprite.add(player_2)
splashScreen(name1,name2)
