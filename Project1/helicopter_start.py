import os, sys
import pygame 
import random
import alsaaudio, time, audioop
from pygame.locals import *

def load_image(name):
    try:
        image = pygame.image.load(name)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    return image, image.get_rect()


class Helicopter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('icon.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 50
        self.move = [0,0]
        self.jump=0

    def update(self):
        if self.jump:
            self.move[1] += -.15
        else:
            self.move[1] += .15

        if abs(self.move[1]) <= .15:
            if self.jump:
                self.move[1]=-1
            else:
                self.move[1] = 1

        elif self.rect.top<self.area.top or self.rect.bottom>self.area.bottom:
            self.rect.topleft = 10, 50 #Restart Position
            self.move[1] = 0            #Set velocity to 0

        self.rect = self.rect.move(self.move)

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('wall.png')    
        self.rect.topright = 0, 0
        self.length=self.rect.bottom
        self.move=[-3,0]
    def update(self):
        self.rect=self.rect.move(self.move)
        if self.rect.right<0:
            self.restart()
    def restart(self):
        self.rect.topleft=self.area.right,random.randint(0,self.area.bottom-self.length)

def main():
    #audio initialization
    inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
    inp.setchannels(1)
    inp.setrate(8000)
    inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
    inp.setperiodsize(160)

    pygame.init()

    #Screen Setup
    xres=1000   
    yres=600
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Is it... helicopter?')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #Game Mechanics Setup
    helicopter = Helicopter()
    wall1=Wall()
    wall2=Wall()
    wall2.rect.topright=xres/2,50
    lives = 100
    score = 0

    allsprites = pygame.sprite.RenderPlain((helicopter, wall1,wall2))
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

        l,data = inp.read()
        if l:
            loudness=audioop.max(data, 2)
        if loudness>=1000:
            helicopter.jump=1
        else:
            helicopter.jump=0

            # elif event.type == KEYDOWN and event.key == K_SPACE:
            #     helicopter.jump=1
            # elif event.type == KEYUP and event.key == K_SPACE:
            #     helicopter.jump=0
                     
        hitbox = helicopter.rect.inflate(-5, -5)
        if hitbox.colliderect(wall1.rect) or hitbox.colliderect(wall2.rect):
            print 'HIT'
            lives -= 1
        else:
            print 'MISS'

        font = pygame.font.Font(None, 36)
        loudCounter = font.render("Loudness: " + str(audioop.max(data, 2)), 1, (10, 10, 10))
        liveCounter = font.render("Lives: " + str(lives), 1, (10, 10, 10))
        scoreCounter = font.render("Score: " + str(score), 1, (10, 10, 10))
        
        if lives <= 0:
            pygame.quit()

        score += 1

        allsprites.update()
        screen.blit(background, (0, 0))
        screen.blit(loudCounter, (810, 570))
        screen.blit(liveCounter, (610, 570))
        screen.blit(scoreCounter, (410, 570))
        allsprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()