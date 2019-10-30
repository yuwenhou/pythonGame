import random
import pygame
from pygame.locals import *
pygame.init()  # 1.游戏初始化
screen = pygame.display.set_mode((700,600)) # 2.创建一个窗口，设置大小
pygame.display.set_caption("接小球游戏")
ball_x,ball_y = 0,0
ban_x, ban_y ,ban_width, ban_height = 400,550,220,100
font = pygame.font.Font('ziti.ttf',24)
ball_true = pygame.image.load("ball.bmp")
score=0
hp = 3
pygame.mixer.init()


# pygame.mixer.music.load("bg_music.mp3")          # Load background music
# pygame.mixer.music.set_volume(0.3)               # Set volume for music
# pygame.mixer.music.play(-1)
hit = pygame.mixer.Sound("hit_wall.wav")          # Load other sounds
hit.set_volume(0.4)
new_life = pygame.mixer.Sound("new_life.wav")       #
new_life.set_volume(0.5)

# 10.20 判定是否是结束
game_over = True
def print_text(font,x,y,text,color = (0,0,0)):
    imgText = font.render(text, True, color)  # 创建字体，三个参数是文本.抗锯齿.颜色
    screen.blit(imgText, (x, y))  # built screen 创建文本窗口


while True:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            ban_x,_ = event.pos
        elif event.type == pygame.MOUSEBUTTONUP: # 鼠标抬起
            if game_over:
                game_over = False
                score = 0
                hp = 3
                new_life.play()
                # 2.py按键控制，需要释放
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                ban_x += -10
            if event.key == pygame.K_RIGHT:
                ban_x += +10
            elif event.key == pygame.K_UP:
                ban_y += -10
            elif event.key == pygame.K_DOWN:
                ban_y += +10

    screen.fill((255, 255, 255))

    if game_over:
        print_text(font, 100,200,'点击开始游戏')
    else:
        ball_y = ball_y+30
        # 没接到小球的判定
        if ball_y>600:
            ball_x = random.randint(0,600)
            ball_y = 0
            hp=hp-1
            if hp == 0:
                game_over = True
        # 接到小球的判定结果
        if ban_x <=ball_x<=ban_x+220 and ban_y <=ball_y<=ban_y+100:
            hit.play()
            score = score+1
            ball_x = random.randint(0, 600)
            ball_y = 0
    imgtext = font.render('分数：%d'%score,True,(0,0,0)) # 设置文字参数，内容，锯齿话，颜色
    screen.blit(imgtext,(0,0)) # 将文字放在屏幕上
    imgtext2 = font.render("生命值：%d"%hp,True,(150,162,22))
    screen.blit(imgtext2,(580,0))

    # pygame.draw.circle(screen,(100,255,0),(ball_x,ball_y),30,0)
    screen.blit(ball_true,(ball_x,ball_y))
    pygame.draw.rect(screen,(100,255,0),(ban_x, ban_y ,ban_width, ban_height),0)
    pygame.display.update() #3.不断循环




