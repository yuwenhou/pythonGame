# 学习初始化游戏框架
# 学习绘制一个小球
import pygame # 2D游戏
import random
pygame.init() # 初始化
screen = pygame.display.set_mode((600, 500)) #设置窗口大小
pygame.display.set_caption("BALL")           #设置窗口名称
# ball_x = 0
# ball_y = 100
rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40 #小挡板的坐标和宽高
ball_x, ball_y = random.randint(0, 500), -50 #让小球从一个上面随pyga机的位置出现

# pygame.mixer.init()
# pygame.mixer.music.load("bg_music.mp3")          # Load background music
# pygame.mixer.music.set_volume(1)
# pygame.mixer.music.play(1,0.0)

while True:  # 不断循环
    for event in pygame.event.get(): # 循环发生的时间
        print(event)
        if event.type == pygame.QUIT:   # 发生事件的对应
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:  # 监听鼠标动作
            rect_x, _ = event.pos  # 让小挡板始终都和鼠标一起动
        # elif event.type == pygame.K_UP:
        #     rect_x += 10

    screen.fill((255, 255, 255))
    ball_y += 50
    if ball_y > 500:
        ball_x, ball_y = random.randint(0, 500), -50
    pygame.draw.circle(screen, (100, 40, 30), (ball_x, ball_y), 30, 0)
    pygame.draw.rect(screen, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
    pygame.display.update()   #刷新画面

pygame.quit() # 退出