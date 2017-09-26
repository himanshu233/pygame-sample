import pygame
import time
import random
pygame.init()
d_w=800
d_h=600
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
gameDisplay=pygame.display.set_mode((d_w,d_h))
pygame.display.set_caption('a bit racey')
clock=pygame.time.Clock()
carimage=pygame.image.load('one.jpg')
def score(count):
    f=pygame.font.SysFont(None,25)
    text=f.render('score='+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def thing(x,y,w,h,c):
    pygame.draw.rect(gameDisplay,c,[x,y,w,h])



def t_o(text,font):
    textsurface=font.render(text, True, red)
    return textsurface, textsurface.get_rect()



def message_display(text):
    lt=pygame.font.Font('freesansbold.ttf',115)
    rects, rectt=t_o(text,lt)
    rectt.center=((d_w/2),(d_h/2))
    gameDisplay.blit(rects,rectt)
    pygame.display.update()
    time.sleep(2)
    gameloop()


def car(x,y):
    gameDisplay.blit(carimage,(x,y))


def crash():
    message_display('you crashed')


def gameloop():
    t_x = random.randrange(0, d_w)

    t_y = -600
    x=(d_w*0.40)
    y=(d_h*0.70)
    x_c=0
    count=0
    speed=5
    gameExit = False
    t_w=100
    t_h=100
    while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_c=-5
                    if event.key== pygame.K_RIGHT:
                        x_c=5
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                        x_c=0
            x=x+x_c
            gameDisplay.fill(white)
            t_y=t_y+speed
            thing(t_x,t_y,t_w,t_h,black)
            car(x,y)
            score(count)
            if x > (d_w-105) or x < -30:
                crash()
            if(t_y>d_h):
                t_y=0-t_h
                t_x=random.randrange(0,d_w)
                count+=1
                speed=speed*1.05
                t_w=t_w*1.1
            if y+15<t_y+t_h:
                if x>=t_x and x<=t_x+t_w or x+141>=t_x and x+141<=t_x+t_w:
                    crash()
                if x<t_x and x+141>t_x+t_w:
                    crash()
            pygame.display.update()
            clock.tick(60)
gameloop()

pygame.quit()

quit()