import pygame
from pygame.locals import *

#----------------------------Classes-----------------------------------
class Ground(pygame.sprite.Sprite):
    def __init__(self, position, size, color):
        super(Ground,self).__init__()
        self.xPos = position[0]
        self.yPos = position[1]
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.x = self.xPos
        self.rect.y = self.yPos


class Entity(pygame.sprite.Sprite):
    def __init__(self, position, color):
        super(Entity, self).__init__()
        self.xPos = position[0]
        self.yPos = position[1]
        self.surf = pygame.Surface((25,25))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()

class Player(Entity):
    def __init__(self, position, color):
        super(Player, self).__init__(position,color)


#-----------------------------Vars---------------------------------
def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))

# Player attributes/ initialization
    player = Player((100,100), (45,185,185))
    walkSpeed = 8
    yVelocity = 0
    gravity = .7
    jumpHeight = 15
    
    onGround = False
    doubleJump = True
    
    canDash = True
    dashing = False
    facing = "right"
    dashLength = .1
    dashSpeed = 14
    dashTime = 0

    ground = [Ground((0,500), (800,100), (40,180,40)),
              Ground((550,350), (150,25), (40,180,40)),
              Ground((100,350), (150,25), (40,180,40)),
              Ground((325,200), (150,25), (40,180,40))]

    moveLeft = False
    moveRight = False

    #-----------------------------Game Loop-----------------------------
    running = True
    while running:
        clock.tick(60)
        initialX = player.xPos
        initialY = player.yPos

        # Ground collision detection
        for x in ground:
            if player.rect.colliderect(x.rect):
                onGround = True
                doubleJump = True
                player.yPos = x.yPos - 24
                yVelocity = 0
                break
            else:
                onGround = False

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    running = False
                elif event.key == K_a:
                    moveLeft = True
                    facing = "left"
                elif event.key == K_d:
                    moveRight = True
                    facing = "right"
                elif event.key == K_SPACE and onGround:
                    yVelocity = -jumpHeight
                elif event.key == K_SPACE and doubleJump:
                    yVelocity = -jumpHeight
                    doubleJump = False
                elif event.key == K_LSHIFT:
                    dashing = True

            
            if event.type == KEYUP:       
                if event.key == K_a:
                    moveLeft = False
                elif event.key == K_d:
                    moveRight = False
    # Player horizontal movement       
        if moveLeft and not dashing:
            player.xPos -= walkSpeed
        if moveRight and not dashing:
            player.xPos += walkSpeed

    # Dashing
        if dashing:
            if facing == "right" and dashTime < dashLength:
                player.xPos += dashSpeed
            elif dashTime < dashLength:
                player.xPos -= dashSpeed
            else:
                dashing = False
                dashTime = 0
            dashTime += .01              
        else:
            yVelocity += gravity
            player.yPos += yVelocity

        player.rect.x = player.xPos
        player.rect.y = player.yPos

        displayScreen(screen, ground, player)

        if onGround:
            ground[1].surf.fill("blue")
        else:
            ground[1].surf.fill("red")
        
def displayScreen(screen, ground, player):
    screen.fill("black")
    
    for x in ground:
        screen.blit(x.surf, (x.xPos, x.yPos))
    screen.blit(player.surf, (player.xPos, player.yPos))
    pygame.display.flip()

main()
