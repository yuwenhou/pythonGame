import random
import pygame
import sys


def figure(screen, photo, x, y):
    content = pygame.image.load(photo)
    screen.blit(content, (x, y))


def ziti(screen, text, x, y, size=24, color=(232, 206, 144)):
    font = pygame.font.Font("ziti.ttf", size)
    img_text = font.render(text, True, color)  # 设置文字参数，内容，锯齿话，颜色
    screen.blit(img_text, (x, y))  # 将文字放在屏幕上


# 按钮
def button(text, x, y, w, h, color, screen):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font('ziti.ttf', 20)
    textRender = font.render(text, True, (232, 206, 144))
    textRect = textRender.get_rect()
    textRect.center = ((x + w / 2), (y + h / 2))
    screen.blit(textRender, textRect)


def run():
    screen_w, screen_h = 640, 480
    score = 0
    hp = 3
    speed = 1
    ball_x, ball_y = 400, 0
    ban_x, ban_y, ban_width, ban_height = 400, screen_h - 40, 220, 100
    bg_volume = 0.3
    sound_volume = 0.4
    start_x, start_y, start_w, start_h = 100, 200, 200, 50
    rank_x, rank_y, rank_w,rank_h = 400,200,200,50
    start = "请点击开始游戏"
    result = ""
    title = "接亚瑟"

    sound_score = "hit_wall.wav"
    ball_figure = "ball.bmp"
    bj_figure = "cover.jpeg"
    bg_music = "bgm.wav"
    ban = "ban5.png"
    game_over = True
    if_rank = False
    # 检测按键是不是按着不放
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    screen = pygame.display.set_mode((screen_w, screen_h))  # 2.创建一个窗口，设置大小
    pygame.display.set_caption(title)
    hit = pygame.mixer.Sound(sound_score)  # 加载音乐
    hit.set_volume(sound_volume)  # 设置音量
    pygame.mixer.music.load(bg_music)
    pygame.mixer.music.set_volume(bg_volume)
    pygame.mixer_music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                mouse_pos = pygame.mouse.get_pos()
                # 若点击了喜欢按钮，停止 while 循环
                if start_x + start_w > mouse_pos[0] > start_x and \
                        start_y + start_h > mouse_pos[1] > start_y:
                    game_over = False
                    score = 0
                    hp = 4
                if rank_x + rank_w > mouse_pos[0] > rank_x and \
                        rank_y + rank_h > mouse_pos[1] > rank_y:
                    if_rank = True
            elif event.type == pygame.MOUSEMOTION:
                ban_x, _ = event.pos

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    moving_down = False

        figure(screen, bj_figure, 0, 0)
        if game_over:
            if if_rank:
                ziti(screen,"测试啦啦啦",300,300,50)
            ziti(screen, start, 100, screen_h / 2, 50)
            ziti(screen, result, 100, screen_h / 2 + 50, 50)
            button("开始游戏", start_x, start_y, start_w, start_h, (0, 0, 0), screen)
            button("排行榜",rank_x, rank_y, rank_w,rank_h,(0,0,0),screen)
        else:

            ball_y = ball_y + speed
            if moving_right:
                ban_x += 30
            elif moving_left:
                ban_x -= 30
            elif moving_down:
                ban_y += 30
            elif moving_up:
                ban_y -= 30

            # 没接到小球的判定
            if ball_y > screen_h:
                ball_x = random.randint(0, screen_w)
                ball_y = 0
                hp = hp - 1
                speed = 1
                if hp == 0:
                    start = "重新开始请点击屏幕"
                    result = "你击杀了%d个小球" % score
                    game_over = True

            # 接到小球的判定结果
            if ban_x <= ball_x <= ban_x + ban_width and ban_y <= ball_y <= ban_y + ban_height:
                score = score + 1
                speed = speed + 1
                hit.play()
                ball_x = random.randint(0, 600)
                ball_y = 0
            ziti(screen, '分数：%d' % score, 0, 0)
            ziti(screen, "生命值：%d" % hp, screen_w - 120, 0)
            figure(screen, ball_figure, ball_x, ball_y)
            pygame.draw.rect(screen, (100, 255, 0), (ban_x, ban_y, ban_width, ban_height), 0)
        pygame.display.update()  # 3.不断循环


def main():
    pygame.init()  # 1.游戏初始化
    pygame.mixer.init()  # 2.音乐初始化
    run()


if __name__ == '__main__':
    main()
