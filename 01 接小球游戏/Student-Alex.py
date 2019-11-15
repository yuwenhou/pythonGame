import pygame
from pygame.locals import *
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0,255,255)

Ball_x = random.randint(1,800)
Ball_y = 0
Ball_color = (255,0,0)
Ball_RADIUS = 45
Ball_speed_x = 10   # 横向速度
Ball_speed_y = 1   # 纵向速度

BANG_color = (0,0,0)
BANG_W = 300
BANG_H = 75

BANG_X = SCREEN_WIDTH/2-BANG_W/2
BANG_y = SCREEN_HEIGHT-BANG_H
BANG_speed_x=1

score =0

lives = 3

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('ball games')
gamefont = pygame.font.Font("ziti.ttf",30)
BALL = pygame.image.load("cai.png")  # 加载图片
BALL1 = pygame.image.load("ball1.png")
BALL2 = pygame.image.load("ball2.png")
BALL3 = pygame.image.load("ball3.png")


while True:
    if lives == 0:
        break

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_SPACE]:
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    sys.exit()
            imgMenu = gamefont.render("回到游戏模式请按 Esc" ,True,(255,255,255))
            screen.blit(imgMenu,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            pygame.display.update()

            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_SPACE]:
                break

    events = pygame.event.get()
    for e in events:
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.MOUSEMOTION:
            BANG_X,_ = e.pos

    screen.fill(BG_COLOR)
    # Ball_x += Ball_speed_x
    Ball_y += Ball_speed_y
    if Ball_x >SCREEN_WIDTH:
        Ball_speed_x = -1
    if Ball_x < 0:
        Ball_speed_x = 1
    if Ball_y > SCREEN_HEIGHT:
        Ball_x = random.randint(1,800)      # 随机下落
        Ball_y = 0
        lives = lives - 1

    if Ball_y < 0:
        Ball_speed_y = 1

    # pygame.draw.circle(screen,Ball_color,(Ball_x,Ball_y),Ball_RADIUS)
    if score < 5:
        screen.blit(BALL1, (Ball_x, Ball_y)) # 放置图片
    elif 10 > score >= 5  :
        screen.blit(BALL2, (Ball_x, Ball_y))
    else:
        screen.blit(BALL, (Ball_x, Ball_y))  # 放置图片

    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_LEFT]:
        BANG_X -=BANG_speed_x
    if key_pressed[K_RIGHT]:
        BANG_X += BANG_speed_x
    if BANG_X >SCREEN_WIDTH-BANG_W:
        BANG_X = SCREEN_WIDTH - BANG_W
    if BANG_X < 0:
        BANG_X = 0

    # 判断得分
    if BANG_X < Ball_x and Ball_x<(BANG_X+BANG_W) and BANG_y < Ball_y:
        Ball_x = random.randint(0,800)
        Ball_y = 0
        score += 1

    pygame.draw.rect(screen,BANG_color,(BANG_X,BANG_y,BANG_W,BANG_H))
    imlives = gamefont.render('命数{}'.format(lives),True,(255,0,0))

    imgScore = gamefont.render('得分{}'.format(score),True,(255,0,0))
    screen.blit(imgScore,(SCREEN_WIDTH-imgScore.get_width(),0))
    screen.blit(imlives, (0, 0))
    pygame.display.update()

