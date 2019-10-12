# 将图片导入
# 通过点击开始，点击结束
import sys, pygame, random  # 导入库
from pygame.locals import *


def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)  # 创建字体，三个参数是文本.抗锯齿.颜色
    screen.blit(imgText, (x, y))  # built screen 创建文本窗口


pygame.init()  # init 初始化

# 窗口设置
screen = pygame.display.set_mode((600, 500))  # screen-size 窗口大小设置
pygame.display.set_caption('BallFall')  # title 窗口标题
font1 = pygame.font.Font('ziti.ttf', 24)  # font,size 字体类型（None为pygame默认字体）.字体大小
pygame.mouse.set_visible(False)  # mouse-visible 光标可视

# 颜色设置
white = 255, 255, 255  # rgb
red = 220, 50, 50
yellow = 230, 230, 50
blue = 0, 0, 100

# 计数设置
lives = 3  # 初始生命
score = 0  # 初始分数

# 初始化设置
game_over = True  # 游戏结束判断
mouse_x = mouse_y = 0  # 光标初始化
pos_x = 300  # 挡板位置初始化
pos_y = 460
bomb_x = random.randint(0, 500)  # 小球位置随机初始化
bomb_y = -50  # 小球下落高度初始化
vel_y = 10  # 小球下落速度

bg = pygame.image.load("ball.bmp")


while True:
    for event in pygame.event.get():  # 事件判断
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:  # 鼠标运动
            mouse_x, mouse_y = event.pos
        elif event.type == MOUSEBUTTONUP:  # 鼠标抬起
            if game_over:
                game_over = False
                lives = 3
                score = 0

    keys = pygame.key.get_pressed()  # 获取键盘
    if keys[K_ESCAPE]:  # 键盘右上角esc键
        pygame.quit()
        sys.exit()

    screen.fill(blue)  # 背景颜色

    if game_over:
        print_text(font1, 100, 200, '点击开始游戏')
    else:  # 判断小球运行轨迹
        bomb_y += vel_y
        if bomb_y > 500:  # fallen
            bomb_x = random.randint(0, 500)  # 小球随机出现
            bomb_y = -50
            lives -= 1
            if lives == 0:
                game_over = True
        elif bomb_y > pos_y:
            if bomb_x > pos_x and bomb_x < pos_x + 120:
                score += 1
                bomb_x = random.randint(0, 500)
                bomb_y = -50

    # pygame.draw.circle(screen, yellow,(bomb_x, int(bomb_y)), 30, 0)  # 绘制圆形 五个参数为屏幕.颜色.位置.实心半径.空心半径
    screen.blit(bg, (bomb_x, int(bomb_y)))
    pos_x = mouse_x  # 挡板位置变化设置
    if pos_x < 0:
        pos_x = 0
    elif pos_x > 500:
        pos_x = 500

    pygame.draw.rect(screen, red, (pos_x, pos_y, 120, 40), 0)  # 绘制矩形 参数跟圆形一样

    print_text(font1, 0, 0, '生命值:' + str(lives))  # 文字显示
    print_text(font1, 500, 0, '分数:' + str(score))

    pygame.display.update()  # 更新










