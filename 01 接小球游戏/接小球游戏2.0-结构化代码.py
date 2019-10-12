# 学习结构化代码
# 学习绘制长方形，并且使用鼠标控制长方形的变化
import pygame
import random


def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))



def playGame(scr, lives, score):
    a = 0
    font1 = pygame.font.Font(None, 24)
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40  # 小挡板的坐标和宽高
    ball_x, ball_y = random.randint(0, 500), -50  # 让小球从一个上面随机的位置出现 vel_y = 4 #小球的初始下落速度
    while lives > 0:  # 循环条件改为当有命时才游戏 否则就结束游戏
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # 1.鼠标控制
            # elif event.type == pygame.MOUSEMOTION:  # 监听鼠标动作
            #     rect_x, _ = event.pos
            # 2.按键控制，需要释放
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            #         rect_x += -10
            #     if event.key == pygame.K_w:
            #         rect_x += +10
            #     elif event.key == pygame.K_UP:
            #         rect_y += -10
            #     elif event.key == pygame.K_DOWN:
            #         rect_y += +10
            # # 3.按键控制，持续按键
            elif key_pressed[pygame.K_LEFT]:
                a = a+10
                rect_x += -10-a
            elif key_pressed[pygame.K_RIGHT]:
                a = a+10
                rect_x += 10+a
        a = a-1
        scr.fill((255, 255, 255))

        if ball_y > 500:  # fallen
            ball_x = random.randint(0, 500)  # 小球随机出现
            ball_y = -50
            lives -= 1

        elif ball_y > rect_y:
            if rect_x < ball_x < rect_x + 120:
                score += 1
                ball_x = random.randint(0, 500)
                ball_y = -50


        ball_y += 10

        pygame.draw.circle(scr, (100, 40, 30), (ball_x, ball_y), 30, 0)
        pygame.draw.rect(scr, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        print_text(scr, font1, 0, 0, "live:" + str(lives))
        print_text(scr, font1, 500, 0, "score:" + str(score))
        pygame.display.update()


def main():

    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("BALL")
    lives = 300
    score = 0
    playGame(screen, lives, score)


if __name__ == '__main__':
    main()